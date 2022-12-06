import re

from testtools import run


def test_indent():
    result = run("indent.py")
    assert result.returncode == 0
    assert re.search(r"[\d:. \-,]+base level", result.stderr)
    assert re.search(r"[\d:. \-,]+ => sub level", result.stderr)
    assert re.search(r"[\d:. \-,]+ =>  => sub sub level", result.stderr)
    assert re.search(r"[\d:. \-,]+ => back to sub level", result.stderr)
