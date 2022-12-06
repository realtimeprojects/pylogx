import re

from testtools import run


def test_indent():
    result = run("timestamps.py")
    assert result.returncode == 0
    assert re.search(r"0:00:00\.0.*\[\+00:00\.0.*\] 1 enjoy", result.stderr)
    assert re.search(r"0:00:01\.0.*\[\+00:01\.0.*\] 2 enjoy", result.stderr)
    assert re.search(r"0:00:03\.0.*\[\+00:02\.0.*\] 3 enjoy", result.stderr)
