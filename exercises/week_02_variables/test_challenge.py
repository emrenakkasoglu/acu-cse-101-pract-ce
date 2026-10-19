"""ACU CSE 101 - Automated Unit Tests for Week 02 Graded Challenge (stdout verification).

In Week 02, students write sequential scripts with variables and expressions (no functions).
Tests execute challenge.py as a subprocess and verify output printed to stdout.
"""

import os
import re
import subprocess
import sys

CHALLENGE_FILE = os.path.join(os.path.dirname(__file__), "challenge.py")


def run_student_script() -> subprocess.CompletedProcess:
    """Execute student's challenge.py and capture stdout and stderr."""
    assert os.path.isfile(CHALLENGE_FILE), f"File not found: {CHALLENGE_FILE}"
    try:
        res = subprocess.run(
            [sys.executable, CHALLENGE_FILE],
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
        return res
    except subprocess.TimeoutExpired:
        raise AssertionError("challenge.py timed out after 5 seconds.")


def test_script_executes_cleanly():
    """Verify that challenge.py runs without syntax errors or runtime exceptions."""
    res = run_student_script()
    assert res.returncode == 0, (
        f"challenge.py crashed with exit code {res.returncode}.\n\nError output:\n{res.stderr}"
    )


def test_notebook_cost_output():
    """Verify the labeled cost of three notebooks."""
    res = run_student_script()
    assert any(
        re.fullmatch(r"Total cost:\s*60(?:\.0+)?(?:\s+TL)?", line.strip())
        for line in res.stdout.splitlines()
    ), f"Expected 'Total cost: 60' in output.\nYour output was:\n{res.stdout}"


def test_seconds_output():
    """Verify the labeled duration of a five-minute break."""
    res = run_student_script()
    assert any(
        re.fullmatch(r"Seconds:\s*300(?:\.0+)?", line.strip())
        for line in res.stdout.splitlines()
    ), f"Expected 'Seconds: 300' in output.\nYour output was:\n{res.stdout}"


def test_greeting_output():
    """Verify the greeting includes the supplied name."""
    res = run_student_script()
    assert "Hello, Ada!" in res.stdout.splitlines(), (
        f"Expected 'Hello, Ada!' in output.\nYour output was:\n{res.stdout}"
    )
