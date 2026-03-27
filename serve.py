"""Dev server: watches template.html and data.json, rebuilds on change, serves on localhost:8000."""
import http.server
import os
import subprocess
import threading
import time

WATCH = ["template.html", "data.json"]
PORT = 8000


def mtimes():
    return {f: os.path.getmtime(f) for f in WATCH if os.path.exists(f)}


def watch_and_rebuild():
    last = mtimes()
    while True:
        time.sleep(0.5)
        current = mtimes()
        if current != last:
            changed = [f for f in WATCH if current.get(f) != last.get(f)]
            print(f"  changed: {', '.join(changed)} — rebuilding...")
            subprocess.run(["python", "build.py"])
            last = current


threading.Thread(target=watch_and_rebuild, daemon=True).start()

print(f"Serving at http://localhost:{PORT}  (watching {', '.join(WATCH)})")
http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler, port=PORT)
