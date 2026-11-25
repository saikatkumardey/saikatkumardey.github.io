#!/usr/bin/env python3
"""Minimal local editor for the Hugo blog.

Run from anywhere:  python3 tools/editor/write.py
Opens http://127.0.0.1:4321 in your browser. Standard library only.
"""
import base64
import datetime as dt
import json
import re
import secrets
import subprocess
import sys
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
BLOG = REPO / "content" / "blog"
IMAGES = REPO / "static" / "images"
ARGS = sys.argv[1:]
PORT = next((int(a) for a in ARGS if a.isdigit()), 4321)
OPEN_BROWSER = "--no-open" not in ARGS
TOKEN = secrets.token_urlsafe(24)
MAX_BODY = 20 * 1024 * 1024
FILE_RE = re.compile(r"^[a-z0-9][a-z0-9-]*\.md$")
IMG_EXT = {"png", "jpg", "jpeg", "gif", "webp", "svg"}
LOCK = threading.Lock()


# ---------- git ----------

def git(*args):
    p = subprocess.run(["git", *args], cwd=REPO, capture_output=True, text=True)
    return p.returncode, (p.stdout + p.stderr).strip()


# ---------- front matter ----------

def split_post(text):
    if text.startswith("+++\n"):
        end = text.find("\n+++", 4)
        if end != -1:
            fm = text[4:end]
            body = text[end + 4:].lstrip("\n")
            return fm, body
    return None, text


def fm_get(fm, key):
    for line in fm.split("\n"):
        if line.startswith("["):
            break
        m = re.match(rf"^{key}\s*=\s*(.+?)\s*$", line)
        if m:
            raw = m.group(1)
            if raw.startswith('"'):
                try:
                    return json.loads(raw)
                except ValueError:
                    return raw.strip('"')
            if raw.startswith("'"):
                return raw.strip("'")
            return raw
    return None


def fm_set(fm, key, literal):
    lines = fm.split("\n")
    top_end = next((i for i, l in enumerate(lines) if l.startswith("[")), len(lines))
    for i in range(top_end):
        if re.match(rf"^{key}\s*=", lines[i]):
            lines[i] = f"{key} = {literal}"
            return "\n".join(lines)
    lines.insert(top_end, f"{key} = {literal}")
    return "\n".join(lines)


def read_post(path):
    fm, body = split_post(path.read_text(encoding="utf-8"))
    fm = fm or ""
    date = str(fm_get(fm, "date") or "")[:10]
    return {
        "file": path.name,
        "title": fm_get(fm, "title") or path.stem,
        "date": date,
        "draft": str(fm_get(fm, "draft")).lower() == "true",
        "hidden": fm_get(fm, "url") is not None or "list = \"never\"" in fm,
        "body": body,
    }


def slugify(title):
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:60].strip("-")
    return s or "untitled"


def write_post(data):
    title = (data.get("title") or "").strip() or "Untitled"
    date = data.get("date") or dt.date.today().isoformat()
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", date):
        raise ValueError("date must be YYYY-MM-DD")
    draft = bool(data.get("draft", True))
    body = data.get("body") or ""
    name = data.get("file")
    with LOCK:
        if name:
            if not FILE_RE.match(name):
                raise ValueError("bad file name")
            path = BLOG / name
            fm, _ = split_post(path.read_text(encoding="utf-8")) if path.exists() else (None, "")
        else:
            base = slugify(title)
            path, n = BLOG / f"{base}.md", 2
            while path.exists():
                path, n = BLOG / f"{base}-{n}.md", n + 1
            fm = None
        fm = fm or ""
        fm = fm_set(fm, "title", json.dumps(title, ensure_ascii=False))
        fm = fm_set(fm, "date", json.dumps(date))
        fm = fm_set(fm, "draft", "true" if draft else "false")
        fm = fm.strip("\n")
        path.write_text(f"+++\n{fm}\n+++\n\n{body.rstrip()}\n", encoding="utf-8")
    return path


def publish(data):
    data = {**data, "draft": False}
    path = write_post(data)
    rel = path.relative_to(REPO).as_posix()
    paths = [rel]
    img_dir = IMAGES / path.stem
    if img_dir.exists():
        paths.append(img_dir.relative_to(REPO).as_posix())
    log = []
    code, out = git("add", "--", *paths)
    log.append(out)
    if code:
        return False, "\n".join(log), path
    code, _ = git("diff", "--cached", "--quiet", "--", *paths)
    if code == 0:
        msg = "Nothing new to commit."
    else:
        title = read_post(path)["title"]
        code, out = git("commit", "-m", f"Publish: {title}", "--", *paths)
        log.append(out)
        if code:
            return False, "\n".join(log), path
        msg = "Committed."
    code, out = git("push")
    log.append(out)
    if code:
        c2, o2 = git("pull", "--rebase", "--autostash")
        log.append(o2)
        if c2:
            git("rebase", "--abort")
            return False, "\n".join(log), path
        code, out = git("push")
        log.append(out)
        if code:
            return False, "\n".join(log), path
    return True, msg + " Pushed.", path


def save_image(data):
    post = data.get("file") or ""
    if not FILE_RE.match(post):
        raise ValueError("save the post (give it a title) before adding images")
    ext = (data.get("ext") or "png").lower().lstrip(".")
    if ext not in IMG_EXT:
        raise ValueError(f"unsupported image type: {ext}")
    raw = base64.b64decode(data.get("data") or "")
    folder = IMAGES / Path(post).stem
    folder.mkdir(parents=True, exist_ok=True)
    name = dt.datetime.now().strftime("%Y%m%d-%H%M%S") + f"-{secrets.token_hex(2)}.{ext}"
    (folder / name).write_bytes(raw)
    return f"/images/{folder.name}/{name}"


def list_posts():
    posts = []
    for p in BLOG.glob("*.md"):
        if p.name.startswith("_"):
            continue
        d = read_post(p)
        d.pop("body")
        posts.append(d)
    posts.sort(key=lambda d: d["date"], reverse=True)
    return posts


# ---------- http ----------

class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _host_ok(self):
        host = (self.headers.get("Host") or "").split(":")[0]
        return host in ("127.0.0.1", "localhost")

    def _send(self, code, payload, ctype="application/json"):
        body = payload if isinstance(payload, bytes) else json.dumps(payload).encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if not self._host_ok():
            return self._send(403, {"error": "forbidden"})
        url = self.path.split("?")[0]
        if url == "/":
            html = (HERE / "editor.html").read_text(encoding="utf-8")
            return self._send(200, html.replace("__TOKEN__", TOKEN).encode(), "text/html; charset=utf-8")
        if url.startswith("/images/"):
            p = (REPO / "static" / url.lstrip("/")).resolve()
            if IMAGES.resolve() in p.parents and p.is_file():
                ext = p.suffix.lstrip(".").lower()
                ctype = "image/svg+xml" if ext == "svg" else f"image/{'jpeg' if ext == 'jpg' else ext}"
                return self._send(200, p.read_bytes(), ctype)
        return self._send(404, {"error": "not found"})

    def do_POST(self):
        if not self._host_ok() or self.headers.get("X-Token") != TOKEN:
            return self._send(403, {"error": "forbidden"})
        n = int(self.headers.get("Content-Length") or 0)
        if n > MAX_BODY:
            return self._send(413, {"error": "too large"})
        try:
            data = json.loads(self.rfile.read(n) or b"{}")
            route = self.path
            if route == "/api/posts":
                return self._send(200, {"posts": list_posts(), "branch": git("branch", "--show-current")[1]})
            if route == "/api/open":
                name = data.get("file", "")
                if not FILE_RE.match(name) or not (BLOG / name).exists():
                    return self._send(404, {"error": "no such post"})
                return self._send(200, read_post(BLOG / name))
            if route == "/api/save":
                return self._send(200, {"file": write_post(data).name})
            if route == "/api/publish":
                ok, log, path = publish(data)
                return self._send(200 if ok else 500, {"ok": ok, "log": log, "file": path.name})
            if route == "/api/image":
                return self._send(200, {"url": save_image(data)})
            return self._send(404, {"error": "not found"})
        except Exception as e:  # surface errors to the UI
            return self._send(400, {"error": str(e)})


def main():
    if not BLOG.is_dir():
        sys.exit(f"Blog folder not found: {BLOG}")
    code, out = git("pull", "--ff-only", "--quiet")
    if code:
        print(f"warning: git pull failed, working offline\n{out}\n")
    srv = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    url = f"http://127.0.0.1:{PORT}/"
    print(f"Editor running at {url}  (Ctrl+C to stop)")
    if OPEN_BROWSER:
        webbrowser.open(url)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nbye")


if __name__ == "__main__":
    main()
