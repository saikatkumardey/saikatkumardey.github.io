#!/bin/bash
# Double-click in Finder to open the blog editor.
cd "$(dirname "$0")/../.." && exec python3 tools/editor/write.py
