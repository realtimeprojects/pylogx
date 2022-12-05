from logging import StreamHandler, getLogger
from .log import log, Level, Indent, ColorFormatter, PrettyDelta  # noqa: F401
from .log import registerLevel, readLevels, levels  # noqa: F401


def enable_colors(level=None, stream=None, logger=None, **kwargs):
    """ enable colorization for console.

        Setup a StreamHandler, add the ColorFormatter to the StreamHandler and return it.

        @param  level   The log levelfor the StreamHandler.
        @param  stream  The output stream to initialize the StreamHandler as passed to
                        the StreamHandler constructor.
        @param  kwargs  Further arguments passed to the ColorFormatter

        @returns the initialized StreamHandler.
    """
    sh = StreamHandler(stream)
    if level:
        sh.setLevel(level)

    cf = ColorFormatter(**kwargs)
    sh.setFormatter(cf)
    logger = logger if logger else getLogger()
    logger.addHandler(sh)
    return sh
