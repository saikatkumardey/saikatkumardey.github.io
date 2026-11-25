#!/bin/bash
# Builds Write.app and installs it in ~/Applications.
# Usage: tools/editor/mac/build.sh
set -euo pipefail

cd "$(dirname "$0")"
REPO="$(cd ../../.. && pwd)"
APP="build/Write.app"
DEST="$HOME/Applications/Write.app"

if ! command -v swiftc >/dev/null; then
  echo "swiftc not found. Run: xcode-select --install" >&2
  exit 1
fi

rm -rf build
mkdir -p "$APP/Contents/MacOS" "$APP/Contents/Resources"
swiftc -O -parse-as-library \
  -target "$(uname -m)-apple-macos12.0" \
  -o "$APP/Contents/MacOS/Write" Write.swift
cp Info.plist "$APP/Contents/Info.plist"
printf '%s' "$REPO" > "$APP/Contents/Resources/repo-path"
codesign --force --sign - "$APP" >/dev/null

# Stop a running copy, then install and launch.
pkill -x Write >/dev/null 2>&1 && sleep 1 || true
mkdir -p "$HOME/Applications"
rm -rf "$DEST"
cp -R "$APP" "$DEST"
open "$DEST"
echo "Installed $DEST. Look for the pencil icon in the menu bar."
