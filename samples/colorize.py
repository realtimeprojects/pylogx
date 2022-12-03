import logging
import time
from pylogx import log, ColorFormatter, Level

console = logging.StreamHandler()
cf = ColorFormatter(ups=[Level.NOTE])
console.setFormatter(cf)
console.setLevel(Level.NOTE)
log.addHandler(console)

log.trace("Have fun with colorized log messages")
log.note("This message disappears with the next log message")
time.sleep(5)
log.note("Another message disappearing soon..")
time.sleep(5)
log.info("Last message is gone")
