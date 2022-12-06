

def test_unknown_log_level():
    from pylogx import log, PylogxError

    try:
        log.warnf("invalid log level")
    except PylogxError as e:
        assert str(e) == "Unknown log level: WARNF"
        return
    assert False, "error not catched."
