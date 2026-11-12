"""Run the bracketed-path parity cases with Windows PowerShell 5.1."""
import os
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path.cwd()))
import pytest  # noqa: E402
from tests import conftest, parity_helpers  # noqa: E402

exe = shutil.which("powershell.exe")
assert os.name == "nt" and exe, "Windows PowerShell 5.1 is required"
version = subprocess.check_output(
    [exe, "-NoProfile", "-Command", "$PSVersionTable.PSVersion.ToString()"], text=True
).strip()
print(f"powershell.exe {version} at {exe}")
print(f"bash detected by tests/conftest.py: {conftest._has_working_bash()}")
assert version.startswith("5.1."), version
parity_helpers.POWERSHELL_EXE = exe
parity_helpers.HAS_POWERSHELL = True
raise SystemExit(
    pytest.main(
        [
            "-p", "no:cacheprovider", "-rs", "-v",
            "tests/test_resolve_template_python_parity.py",
            "tests/test_setup_tasks_python_parity.py",
            "-k", "bracketed_project or bracketed_manifest",
        ]
    )
)
