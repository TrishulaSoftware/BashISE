from __future__ import annotations
import os
import sys
import runpy
from .buildmeta import build_id, legacy_sha256, pkg_version, short_sha

def _is_receipt_json_path(p: str) -> bool:
    try:
        ap = os.path.abspath(os.path.expanduser(p))
    except Exception:
        return False
    # Canon receipt roots
    r1 = os.path.abspath(os.path.expanduser("~/.local/share/bise2/receipts"))
    r2 = os.path.abspath(os.path.expanduser("~/.local/share/bise2/receipts/armory"))
    if ap.endswith(".json") and (ap.startswith(r1 + os.sep) or ap.startswith(r2 + os.sep)):
        return True
    # Heuristic block: run.*.json or receipt-like json opened as the main target
    base = os.path.basename(ap).lower()
    if ap.endswith(".json") and (base.startswith("run.") or base.startswith("op.") or base.startswith("receipt.") or base.startswith("evidence.")):
        return True
    return False

def main() -> int:
    argv = sys.argv[1:]

    # Version stamping (wrapper level; no legacy edits)
    if "--version" in argv or "-V" in argv:
        # Legacy-compat mode if needed
        if os.environ.get("BISE2_VERSION_LEGACY", "0") == "1":
            print("bise2")
        else:
            print(f"bise2 {build_id()}")
        return 0

    if "--build" in argv:
        print(f"bise2_pkg_version: {pkg_version()}")
        sha = legacy_sha256()
        print(f"bise2_legacy_sha256: {sha}")
        print(f"bise2_legacy_sha256_short: {short_sha(sha)}")
        return 0

    # Guard: refuse to open receipts as the primary target unless explicitly overridden
    # (This is the startup-side guard; the in-GUI Run-guard stays on the Canon list next.)
    if argv and os.environ.get("BISE2_RUN_GUARD", "1") != "0":
        if _is_receipt_json_path(argv[0]):
            print("[run] blocked: refusing to open receipt JSON as a runnable/primary target")
            return 2

    # Canon: if Armory selftest is requested, emit build fingerprint prelude
    if os.environ.get("BISE2_ARMORY_SELFTEST") == "1":
        print(f"bise2_build_id: {build_id()}")
        print(f"bise2_pkg_version: {pkg_version()}")
        print(f"bise2_legacy_sha256_short: {short_sha(legacy_sha256())}")

    runpy.run_module("bise2._legacy", run_name="__main__")
    return 0
