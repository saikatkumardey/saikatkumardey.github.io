# Write

A tiny local editor for this blog. It needs Python 3 and git only. Nothing to install.

## Start

```bash
python3 tools/editor/write.py
```

Or double-click `tools/editor/Write.command` in Finder. It opens http://127.0.0.1:4321.

## Menu bar app (Mac)

```bash
tools/editor/mac/build.sh
```

This builds `Write.app`, installs it in `~/Applications`, and starts it. A pencil icon appears in the menu bar. Its menu has Open Editor, New Post, Open in Browser, Open at Login, Show Log, and Quit.

- It needs Xcode Command Line Tools for `swiftc`. Install them with `xcode-select --install`.
- The app runs the same editor in its own window and stops the editor when you quit.
- The app remembers this blog folder. Rebuild it if you move the folder.
- The editor's output goes to `~/Library/Logs/Write.log`.

## Keys

| Key | Action |
|---|---|
| ⌘O | Find or open a post |
| ⌘N | New post |
| ⌘/ | Preview on or off |
| ⌘S | Save now (it also autosaves while you type) |
| ⌘⏎ | Publish: commit and `git push` |

Paste or drop an image to save it in `static/images/<post>/` and insert a link.

## How it works

- Posts are saved to `content/blog/<slug>.md` as you type. A new post's file name comes from its first title.
- New posts start as drafts. Publish sets `draft = false`, commits only that post and its images, then pushes.
- Publish uses your normal git login. Run it on `main` so the push deploys the site.
- Other front matter, like `url` or `[_build]`, is kept.
