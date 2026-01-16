# BashISE (bise2)

BashISE is a **local-first**, **package-first**, safety-minded editor + project runner designed to feel like a lightweight “ISE” experience for Bash workflows on Linux.

It’s built around Trishula’s operational doctrine:
- **Make work reproducible**
- **Make changes provable**
- **Keep users in control**
- **Avoid brittle dependencies**
- **Ship something you can deploy anywhere**

---

## Highlights

### Editor + Workspace
- **Text editor** with a clean, fast buffer-first workflow
- **New / Open / Save / Save As**
- **Dirty-state tracking** (knows when the buffer has unsaved changes)
- **Project root** concept (work rooted inside a chosen folder)
- **Project tree** view for browsing files and folders
- **Refresh tree** button (re-scan project view quickly)
- **Quick Open** dialog (keyboard-friendly file picker scoped to the current root)
- **Find** dialog for fast in-buffer search
- **Project Search** dialog (root-scoped search across files; designed to stay snappy)
- **Problems panel** for check/run feedback and jump-to style workflows (boot-safe)


### Run + Check
- **Run buffer** (execute what’s in the editor)
- **Run selection (“Run Sel”)** (highlight text and run only that)
- **Argument input** support (Run with args)
- **Check** action (non-destructive checks / validation pass)
- **Receipts for run actions** (run.*.json) for auditability and “prove it” workflows

### Evidence + Audit Artifacts (Armory)
- **Evidence Pack export**
  - portable `tar.gz` bundles of receipts / logs / config / hashes
  - built for sharing, archiving, and forensic replay
- **Receipt-first mindset**
  - operations emit structured artifacts to disk
  - UTC-stamped receipts for correlation across machines
- **Armory bootstrap selftest**
  - validates packaging integrity and key invariants
  - verifies compile-safety and environment readiness
  - confirms **tkinter is available but not imported** during selftest (`tkinter_imported: False`)
- **Backups doctrine for critical ops**
  - backups stored under a consistent root in your home directory
  - integrity proof (size + SHA256) recorded in receipts

### Safety Guardrails
- **Deny-list roots** (prevents operating on risky system locations by default)
- **Root-scoped operations** (project actions stay inside the chosen root)
- **Non-sudo install + runtime isolation**
  - installs into a **per-user runtime venv**
  - avoids breaking system Python
- **Compile gate** philosophy
  - packaging changes are compile-checked before shipping

### UI + UX Details
- **Small-screen / older laptop friendly**
  - top toolbar is horizontally scrollable when it overflows
  - prevents “buttons cut off with no access”
- **Keyboard-first workflows**
  - quick open (Ctrl+P style)
  - project search (Ctrl+Shift+F style)
  - run (F5 style)
  - run selection (Ctrl+Enter style)
  - check (F6 style)
  *(Bindings depend on the current canon build.)*
- **Terminal launcher button** (“Terminal”) to open a shell at the current location


<img width="1334" height="732" alt="Screenshot from 2026-01-15 23-26-45" src="https://github.com/user-attachments/assets/6e03bb95-430f-48dd-aee5<img width="1334" height="732" alt="Screenshot from 2026-01-15 23-26-32" src="https://github.com/user-attachments/assets/1a5cca05-0c27-459c-a2b0-aff423a2576e" />
-e26748faacee" />
---

## Install (No sudo)

### Option A — Release tarball (recommended)
1) Download/extract the release tarball  
2) Run:
3) 

```bash
bash ./<release-folder>/install.sh ./<release-folder>/artifacts/bise2-*.whl
<img width="1334" height="732" alt="Screenshot from 2026-01-15 23-26-32" src="https://github.com/user-attachments/assets/34db336f-00b8-4498-a382-fe5c7c9394cb" />
