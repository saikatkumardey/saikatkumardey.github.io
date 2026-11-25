// Write: a menu bar app for the blog editor.
// Build with ./build.sh (needs Xcode Command Line Tools).
import Cocoa
import ServiceManagement
import WebKit

enum Config {
    static let port = 4321
    static let url = URL(string: "http://127.0.0.1:4321/")!
    static let logPath = NSString(string: "~/Library/Logs/Write.log").expandingTildeInPath
}

final class AppDelegate: NSObject, NSApplicationDelegate, NSWindowDelegate, WKNavigationDelegate {
    var statusItem: NSStatusItem!
    var window: NSWindow?
    var webView: WKWebView?
    var server: Process?
    var pageLoaded = false
    var pendingJS: String?

    // MARK: launch

    func applicationDidFinishLaunching(_ notification: Notification) {
        buildMainMenu()
        statusItem = NSStatusBar.system.statusItem(withLength: NSStatusItem.squareLength)
        if let button = statusItem.button {
            button.image = NSImage(systemSymbolName: "square.and.pencil", accessibilityDescription: "Write")
            button.image?.isTemplate = true
        }
        let menu = NSMenu()
        menu.addItem(withTitle: "Open Editor", action: #selector(openEditor), keyEquivalent: "")
        menu.addItem(withTitle: "New Post", action: #selector(newPost), keyEquivalent: "")
        menu.addItem(withTitle: "Open in Browser", action: #selector(openInBrowser), keyEquivalent: "")
        menu.addItem(.separator())
        if #available(macOS 13.0, *) {
            let item = menu.addItem(withTitle: "Open at Login", action: #selector(toggleLogin(_:)), keyEquivalent: "")
            item.state = SMAppService.mainApp.status == .enabled ? .on : .off
        }
        menu.addItem(withTitle: "Show Log", action: #selector(showLog), keyEquivalent: "")
        menu.addItem(.separator())
        menu.addItem(withTitle: "Quit Write", action: #selector(quit), keyEquivalent: "q")
        for item in menu.items { item.target = self }
        statusItem.menu = menu
        startServer()
    }

    func applicationWillTerminate(_ notification: Notification) {
        server?.terminate()
    }

    // MARK: server

    func repoPath() -> String? {
        guard let p = Bundle.main.path(forResource: "repo-path", ofType: nil),
              let s = try? String(contentsOfFile: p, encoding: .utf8) else { return nil }
        return s.trimmingCharacters(in: .whitespacesAndNewlines)
    }

    func startServer() {
        guard let repo = repoPath() else {
            alert("Blog folder unknown", "Rebuild the app with tools/editor/mac/build.sh.")
            return
        }
        let script = (repo as NSString).appendingPathComponent("tools/editor/write.py")
        guard FileManager.default.fileExists(atPath: script) else {
            alert("Editor not found", "Expected \(script). Rebuild the app from your blog folder.")
            return
        }
        let p = Process()
        p.executableURL = URL(fileURLWithPath: "/usr/bin/env")
        p.arguments = ["python3", script, String(Config.port), "--no-open"]
        p.currentDirectoryURL = URL(fileURLWithPath: repo)
        var env = ProcessInfo.processInfo.environment
        env["PATH"] = "/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:" + (env["PATH"] ?? "")
        env["PYTHONUNBUFFERED"] = "1"
        env["GIT_TERMINAL_PROMPT"] = "0"  // never hang on a password prompt
        p.environment = env
        FileManager.default.createFile(atPath: Config.logPath, contents: nil)
        if let log = FileHandle(forWritingAtPath: Config.logPath) {
            p.standardOutput = log
            p.standardError = log
        }
        do {
            try p.run()
            server = p
        } catch {
            alert("Could not start the editor", error.localizedDescription)
        }
    }

    /// Polls the local server, then runs `done` on the main thread.
    func whenReady(_ done: @escaping @MainActor () -> Void) {
        Task { @MainActor in
            for _ in 0..<80 {
                var req = URLRequest(url: Config.url)
                req.timeoutInterval = 1
                if let result = try? await URLSession.shared.data(for: req),
                   (result.1 as? HTTPURLResponse)?.statusCode == 200 {
                    done()
                    return
                }
                try? await Task.sleep(nanoseconds: 250_000_000)
            }
            self.alert("The editor did not start", "Details are in \(Config.logPath).")
        }
    }

    // MARK: window

    @objc func openEditor() { showWindow(then: nil) }

    @objc func newPost() { showWindow(then: "save().then(newPost)") }

    @objc func openInBrowser() { whenReady { NSWorkspace.shared.open(Config.url) } }

    @objc func showLog() { NSWorkspace.shared.open(URL(fileURLWithPath: Config.logPath)) }

    func showWindow(then js: String?) {
        NSApp.activate(ignoringOtherApps: true)
        if let w = window {
            w.makeKeyAndOrderFront(nil)
            if let js = js { run(js) }
            return
        }
        pendingJS = js
        let web = WKWebView(frame: .zero, configuration: WKWebViewConfiguration())
        web.navigationDelegate = self
        let w = NSWindow(
            contentRect: NSRect(x: 0, y: 0, width: 980, height: 760),
            styleMask: [.titled, .closable, .miniaturizable, .resizable],
            backing: .buffered, defer: false)
        w.title = "Write"
        w.titlebarAppearsTransparent = true
        w.backgroundColor = .white
        w.appearance = NSAppearance(named: .aqua)  // always black on white
        w.isReleasedWhenClosed = false
        w.minSize = NSSize(width: 480, height: 360)
        w.delegate = self
        w.contentView = web
        w.center()
        w.setFrameAutosaveName("WriteEditor")
        w.makeKeyAndOrderFront(nil)
        window = w
        webView = web
        whenReady { web.load(URLRequest(url: Config.url)) }
    }

    func run(_ js: String) {
        guard pageLoaded, let web = webView else { pendingJS = js; return }
        web.evaluateJavaScript(js, completionHandler: nil)
    }

    func windowWillClose(_ notification: Notification) {
        run("save()")
    }

    // MARK: navigation: keep the editor inside, open other links in the browser

    func webView(_ webView: WKWebView, decidePolicyFor navigationAction: WKNavigationAction) async -> WKNavigationActionPolicy {
        guard let url = navigationAction.request.url else { return .cancel }
        if url.host == "127.0.0.1" || url.scheme == "about" { return .allow }
        if ["http", "https", "mailto"].contains(url.scheme ?? "") {
            NSWorkspace.shared.open(url)
        }
        return .cancel
    }

    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        pageLoaded = true
        if let js = pendingJS {
            pendingJS = nil
            Task { @MainActor in
                try? await Task.sleep(nanoseconds: 400_000_000)  // let the page open its last post first
                self.run(js)
            }
        }
    }

    // MARK: login item and quit

    @objc func toggleLogin(_ sender: NSMenuItem) {
        guard #available(macOS 13.0, *) else { return }
        do {
            if SMAppService.mainApp.status == .enabled {
                try SMAppService.mainApp.unregister()
            } else {
                try SMAppService.mainApp.register()
            }
            sender.state = SMAppService.mainApp.status == .enabled ? .on : .off
        } catch {
            alert("Could not change Open at Login", error.localizedDescription)
        }
    }

    @objc func quit() {
        run("save()")
        Task { @MainActor in
            try? await Task.sleep(nanoseconds: 600_000_000)  // give the last save time to land
            NSApp.terminate(nil)
        }
    }

    // MARK: helpers

    func alert(_ title: String, _ text: String) {
        NSApp.activate(ignoringOtherApps: true)
        let a = NSAlert()
        a.messageText = title
        a.informativeText = text
        _ = a.runModal()
    }

    /// A main menu makes copy, paste, undo and close shortcuts work in the web view.
    func buildMainMenu() {
        let main = NSMenu()

        let appItem = NSMenuItem()
        let appMenu = NSMenu()
        appMenu.addItem(withTitle: "Quit Write", action: #selector(quit), keyEquivalent: "q").target = self
        appItem.submenu = appMenu
        main.addItem(appItem)

        let editItem = NSMenuItem()
        let edit = NSMenu(title: "Edit")
        edit.addItem(withTitle: "Undo", action: Selector(("undo:")), keyEquivalent: "z")
        edit.addItem(withTitle: "Redo", action: Selector(("redo:")), keyEquivalent: "z")
            .keyEquivalentModifierMask = [.command, .shift]
        edit.addItem(.separator())
        edit.addItem(withTitle: "Cut", action: #selector(NSText.cut(_:)), keyEquivalent: "x")
        edit.addItem(withTitle: "Copy", action: #selector(NSText.copy(_:)), keyEquivalent: "c")
        edit.addItem(withTitle: "Paste", action: #selector(NSText.paste(_:)), keyEquivalent: "v")
        edit.addItem(withTitle: "Select All", action: #selector(NSText.selectAll(_:)), keyEquivalent: "a")
        editItem.submenu = edit
        main.addItem(editItem)

        let windowItem = NSMenuItem()
        let windowMenu = NSMenu(title: "Window")
        windowMenu.addItem(withTitle: "Close", action: #selector(NSWindow.performClose(_:)), keyEquivalent: "w")
        windowMenu.addItem(withTitle: "Minimize", action: #selector(NSWindow.performMiniaturize(_:)), keyEquivalent: "m")
        windowItem.submenu = windowMenu
        main.addItem(windowItem)

        NSApp.mainMenu = main
    }
}

@main
struct WriteApp {
    @MainActor static func main() {
        let app = NSApplication.shared
        let delegate = AppDelegate()
        app.delegate = delegate
        app.setActivationPolicy(.accessory)  // menu bar only, no Dock icon
        withExtendedLifetime(delegate) { app.run() }
    }
}
