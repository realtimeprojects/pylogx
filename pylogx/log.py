import os
import logging
import json
from datetime import datetime, timedelta, timezone
from termcolor import colored


class Level:
    pass


class ColorFormatter(logging.Formatter):
    def __init__(self, fmt="%(message)s", ups=[], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args = args
        self.kwargs = kwargs
        self._fmt = fmt
        self.ups = ups
        self.lastLevel = 0

    def format(self, record):
        log_fmt = self.getColoredFormat(record.levelno)
        formatter = logging.Formatter(log_fmt, *self.args, **self.kwargs)
        return formatter.format(record)

    def getColoredFormat(self, level):
        lvl = getLevelByNumber(level)
        kwargs = {}
        if lvl['color']:
            kwargs["color"] = lvl['color']
        if lvl['on_color']:
            kwargs["on_color"] = lvl['on_color']
        if lvl['attrs']:
            kwargs["attrs"] = lvl['attrs']
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


class PylogxLogger(logging.Logger):
    def __getattr__(self, name):
        name = name.upper()

        def _logfnc(*args, **kwargs):
            level = int(logging.getLevelName(name))
            return self.log(level, *args, **kwargs)
        if hasattr(Level, name):
            return _logfnc
        return super().__getattr__(name)


def registerLevel(number, level):
    name = level['name']
    if not hasattr(logging, name):
        setattr(logging, name, number)
        logging.addLevelName(number, name)
    setattr(Level, name, number)
    # if not hasattr(logging, name.lower()):
    #    setattr(logging.Logger, name.lower(), _logfnc)


def readLevels(file=None):
    if not file:
        file = os.path.join(os.path.dirname(__file__), "levels.json")
    levelFP = open(file)
    lvls = json.load(levelFP)
    actives = os.environ.get("PYLOG_LEVELS")
    if actives:
        actives = actives.split(",")
    levels = {}
    for (number, data) in lvls.items():
        levels[int(number)] = data
        if not actives or data['name'] in actives:
            registerLevel(int(number), data)
    return levels


levels = readLevels()


def getLevelByNumber(number):
    return levels[number]


logging.setLoggerClass(PylogxLogger)

os.environ['FORCE_COLOR'] = "yes"
log = logging.getLogger().getChild('pylogx')
log.setLevel(logging.DEBUG)
logging.setLoggerClass(PylogxLogger)
logging.getLogger().setLevel(logging.DEBUG)
