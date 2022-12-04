from logging import StreamHandler
from .log import log, Level, IndentFilter, ColorFormatter, PrettyDelta  # noqa: F401
from .log import registerLevel, readLevels, levels  # noqa: F401


def enable_colors(level=None, stream=None, **kwargs):
    """ enable colorization for console.

        Setup a StreamHandler, add the ColorFormatter to the StreamHandler and return it.

        @param  level   The log levelfor the StreamHandler.
        @param  stream  The output stream to initialize the StreamHandler as passed to
                        the StreamHandler constructor.
        @param  kwargs  Further arguments passed to the ColorFormatter

        @returns the initialized StreamHandler.
    """
    cf = ColorFormatter(**kwargs)
    sh = StreamHandler(stream)
    if level:
        sh.setLevel(level)
    sh.setFormatter(cf)
    log.addHandler(sh)
    return sh
