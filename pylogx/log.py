import os
import sys
import logging
from datetime import datetime, timedelta, timezone
from termcolor import colored

logging.NOTE = 15
logging.SUCCESS = 22
logging.HINT = 23
logging.TRACE = 25
logging.addLevelName(logging.SUCCESS, "SUCCESS")
logging.addLevelName(logging.NOTE, "NOTE")
logging.addLevelName(logging.HINT, "HINT")
logging.addLevelName(logging.TRACE, "TRACE")


class ColorFormatter(logging.Formatter):
    COLORS = {
            logging.DEBUG: "grey",
            logging.NOTE: "grey",
            logging.INFO: "white",
            logging.SUCCESS: "green",
            logging.HINT: "cyan",
            logging.TRACE: "magenta",
            logging.WARNING: "yellow",
            logging.ERROR: "red",
            logging.CRITICAL: "red",
    }

    ATTRIBUTES = {
            logging.NOTE: ["bold"],
            logging.CRITICAL: ["bold"]
    }
    ON_COLORS = {}

    def __init__(self, fmt="%(message)s", ups=[], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args = args
        self.kwargs = kwargs
        self._fmt = fmt
        self.ups = ups
        self.lastLevel = 0

        self.colors = ColorFormatter.COLORS
        self.attributes = ColorFormatter.ATTRIBUTES
        self.on_colors = ColorFormatter.ON_COLORS

    def format(self, record):
        log_fmt = self.get_colored_format(record.levelno)
        formatter = logging.Formatter(log_fmt, *self.args, **self.kwargs)
        return formatter.format(record)

    def get_colored_format(self, level):
        kwargs = {}
        if level in self.colors:
            kwargs["color"] = self.colors[level]
        if level in self.on_colors:
            kwargs["on_color"] = self.on_colors[level]
        if level in self.attributes:
            kwargs["attrs"] = self.attributes[level]
        fmt = colored(self._fmt, **kwargs)
        if self.lastLevel in self.ups:
            fmt = "\033[2K" + fmt
        if level in self.ups:
            fmt = fmt + "\033[1A"
            self.lastLevel = level
        return fmt


class IndentFilter(logging.Filter):
    def __init__(self, initial=0, indent="   "):
        self._indent = indent
        self._ilevel = initial

    def inc(self):
        self._ilevel += 1

    def dec(self):
        if self._ilevel > 0:
            self._ilevel -= 1

    def filter(self, record):
        record.indent = self._ilevel * self._indent
        return True


class PrettyDelta(logging.Filter):
    def __init__(self, start=None, indent="   ", name="prettyDelta", fmt=None, relative=False):
        self._started = start
        self.name = name
        self.relative = relative
        self.lastUpdate = datetime.now().timestamp()
        self.fmt = fmt

    def filter(self, record):
        if self._started:
            delta = datetime.fromtimestamp(record.created) - self._started
        else:
            delta = timedelta(milliseconds=record.relativeCreated)
        if self.relative:
            delta = datetime.fromtimestamp(record.created) - datetime.fromtimestamp(self.lastUpdate)
            self.lastUpdate = record.created
        if self.fmt:
            dt = datetime.fromtimestamp(0, timezone.utc) + delta
            delta = dt.strftime(self.fmt)
        record.__setattr__(self.name, delta)
        return True


def fatal(self, *args, **kwargs):
    log.critical(*args, **kwargs)
    sys.exit(255)


def trace(self, *args, **kwargs):
    log.log(logging.TRACE, *args, **kwargs)


def success(self, *args, **kwargs):
    log.log(logging.SUCCESS, *args, **kwargs)


def hint(self, *args, **kwargs):
    log.log(logging.HINT, *args, **kwargs)


def note(self, *args, **kwargs):
    log.log(logging.NOTE, *args, **kwargs)


logging.Logger.fatal = fatal
logging.Logger.trace = trace
logging.Logger.hint = hint
logging.Logger.note = note
logging.Logger.success = success

os.environ['FORCE_COLOR'] = "yes"

log = logging.getLogger().getChild('pylogx')


class Level:
    NOTSET = logging.NOTSET
    DEBUG = logging.DEBUG
    HINT = logging.HINT
    INFO = logging.INFO
    SUCCESS = logging.SUCCESS
    NOTE = logging.NOTE
    TRACE = logging.TRACE
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL


logging.getLogger().setLevel(logging.DEBUG)
log.setLevel(logging.DEBUG)
