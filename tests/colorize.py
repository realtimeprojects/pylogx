import re

from testtools import run


def test_indent():
    result = run("colorize.py")
    assert result.returncode == 0
    assert re.search(r"\x1b\[35m.*Have fun with colorized log messages\x1b\[0m", result.stdout)
    assert re.search(r"\x1b\[30m.*This message disappears with the next log message\x1b\[0m\x1b\[1A", result.stdout)
    assert re.search(r"\x1b\[1m\x1b\[30m.*Another message.*\x1b\[0m\x1b\[1A", result.stdout)
    assert re.search(r"\x1b\[2K\x1b\[32m.*Last message is gone*\x1b\[0m", result.stdout)
    assert False
