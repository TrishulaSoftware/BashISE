from __future__ import annotations
import hashlib
import os
from importlib import metadata

def pkg_version() -> str:
    try:
        return metadata.version("bise2")
    except Exception:
        return "0.0.0"

def file_sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def legacy_sha256() -> str:
    here = os.path.dirname(__file__)
    legacy = os.path.join(here, "_legacy.py")
    return file_sha256(legacy)

def short_sha(s: str, n: int = 12) -> str:
    return s[:n]

def build_id() -> str:
    # Canon build id: <pkgver>+<legacyshortsha>
    sha = legacy_sha256()
    return f"{pkg_version()}+{short_sha(sha)}"
