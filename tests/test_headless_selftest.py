import os
import subprocess
import sys

def _run(cmd, env):
    return subprocess.run(cmd, env=env, capture_output=True, text=True)

def test_headless_selftest():
    env = dict(os.environ)
    env["BISE2_ARMORY_SELFTEST"] = "1"

    # Prefer module invocation (stable in CI)
    p = _run([sys.executable, "-m", "bise2"], env)
    if p.returncode != 0:
        # Fallback: console-script entrypoint if module isn't wired the way we expect
        p = _run(["bise2"], env)

    out = (p.stdout or "") + "\n" + (p.stderr or "")
    assert p.returncode == 0, out
    assert "BISE2_ARMORY_SELFTEST=OK" in out, out
