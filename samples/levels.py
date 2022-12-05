import logging
import pylogx
from pylogx import enable_colors, Level, log

# log = pylogx.log.getChild("pylogx.acre")
log.setLevel(Level.DEBUG)

console = enable_colors(Level.INFO)
fh = logging.FileHandler("test.log")
fh.setLevel(Level.DEBUG)
log.addHandler(fh)

mh = logging.getLogger().getChild("mh")
mh.setLevel(Level.DEBUG)
monitor = logging.FileHandler("monitor.log")
monitor.setLevel(Level.DEBUG)
mh.addHandler(monitor)

mh.info("monitor message")

console.debug("debug console")
console.info("info console")
console.trace("trace console")
console.error("error console")
print("-----")
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
