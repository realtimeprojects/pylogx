import logging
import pylogx
from pylogx import enable_colors, Level, log

# log = pylogx.log.getChild("pylogx.acre")
log.setLevel(Level.DEBUG)

console = enable_colors(Level.INFO)
fh = logging.FileHandler("test.log")
fh.setLevel(Level.DEBUG)

mh = log.getChild("mh")
mh.setLevel(Level.DEBUG)
monitor = logging.FileHandler("monitor.log")
monitor.setLevel(Level.INFO)
mh.addHandler(monitor)
mh.addHandler(fh)

mh.debug("debug monitor message")
mh.info("info monitor message")

log.debug("debug message")
log.info("info message")
log.trace("trace message")
log.error("error message")
print("-----")
logging.debug("debug logging")
logging.info("info logging")
logging.error("error logging")
print("-----")
print("-----")
