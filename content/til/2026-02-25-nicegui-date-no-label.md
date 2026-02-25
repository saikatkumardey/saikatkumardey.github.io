---
date: 2026-02-25
title: "NiceGUI: ui.date() does not accept a label parameter"
---

In NiceGUI 3.x, `ui.date()` does not accept a `label` keyword argument — unlike `ui.input()` or `ui.number()` which do. Passing one throws a `TypeError` at runtime and surfaces as a 500 on the page.

Fix: add a `ui.label()` manually above the date picker.

```python
# Wrong — crashes
ui.date(label="Date")

# Right
ui.label("Date").classes("text-xs text-gray-500")
ui.date()
```

[NiceGUI docs](https://nicegui.io/documentation/date)
