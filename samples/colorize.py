import sys
import time
import logging
import pylogx
from pylogx import log

pylogx.enable_colors(logging.getLogger(),
                     fmt="%(asctime)s %(message)s",
                     stream=sys.stdout,
                     level=pylogx.Level.NOTE,
                     ups=[pylogx.Level.NOTE])

log.trace("Have fun with colorized log messages")
log.note("This message disappears with the next log message")
time.sleep(5)
log.note("Another message disappearing soon..")
time.sleep(5)
log.success("Last message is gone")
