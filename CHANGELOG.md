# Changelog

## 0.1.0 — 2026-01-16
Initial packaged release.

Packaging & deployment
- Wheel packaging and reproducible artifact build
- Per-user runtime venv install (`~/.local/share/bise2/runtime/venv`)
- Stable wrapper launcher `~/.local/bin/bise2` runs `python -m bise2`

Armory / audit
- Armory bootstrap selftest (compile gate + environment checks)
- Evidence packs and receipts pipeline validated
- Selftest confirms `tkinter_imported: False`

UX / stability
- Small-screen toolbar fix: horizontally scrollable toolbar when overflow occurs
- Startup stability hardened (compile-checked; safe handler stubs to prevent boot failures)
