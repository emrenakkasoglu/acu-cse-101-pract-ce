"""ACU CSE 101 - Automated Unit Tests for Week 02 Practice (stdout verification).

In Week 02, students write sequential scripts with variables and expressions (no functions).
Tests execute practice.py as a subprocess and verify output printed to stdout.
"""

import os
import subprocess
import sys

PRACTICE_FILE = os.path.join(os.path.dirname(__file__), "practice.py")


def run_student_script() -> subprocess.CompletedProcess:
    """Execute student's practice.py and capture stdout and stderr."""
    assert os.path.isfile(PRACTICE_FILE), f"File not found: {PRACTICE_FILE}"
    try:
        res = subprocess.run(
            [sys.executable, PRACTICE_FILE],
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
        return res
    except subprocess.TimeoutExpired:
        raise AssertionError("practice.py timed out after 5 seconds.")


def test_script_executes_cleanly():
    """Verify that practice.py runs without syntax errors or runtime exceptions."""
    res = run_student_script()
    assert res.returncode == 0, (
        f"practice.py crashed with exit code {res.returncode}.\n\nError output:\n{res.stderr}"
    )


def test_bookstore_cost_output():
    """Verify that total bookstore cost ($945.45) is printed to stdout."""
    res = run_student_script()
    stdout = res.stdout

    # 60 copies total wholesale cost is 945.45
    assert "945.45" in stdout, (
        "Expected wholesale cost 945.45 not found in stdout.\n"
        f"Your output was:\n{res.stdout}"
    )


def test_arrival_time_output():
    """Verify that arrival time (7:30 or 07:30) is printed to stdout."""
    res = run_student_script()
    stdout = res.stdout

    found = ("7:30" in stdout) or ("07:30" in stdout)
    assert found, (
        "Expected arrival time 7:30 or 07:30 not found in stdout.\n"
        f"Your output was:\n{res.stdout}"
    )


def test_banner_output():
    """Verify that banner containing 'PYTHON' and '=' is printed to stdout."""
    res = run_student_script()
    stdout = res.stdout

    assert "PYTHON" in stdout, (
        f"Expected 'PYTHON' not found in stdout banner.\nYour output was:\n{res.stdout}"
    )
    assert "=" in stdout, (
        "Expected border character '=' not found in stdout banner.\n"
        f"Your output was:\n{res.stdout}"
    )
