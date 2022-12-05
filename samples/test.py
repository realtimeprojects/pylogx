import logging
import pylogx

plx = logging.getLogger().getChild("plx")
fh = logging.FileHandler("test.log")
sh = logging.StreamHandler()
plx.setLevel(logging.DEBUG)
plx.addHandler(sh)
plx.addHandler(fh)

mh = logging.getLogger().getChild("mh")
mh.propagate = False
mh.setLevel(logging.TRACE)
monitor = logging.FileHandler("monitor.log")
monitor.setLevel(logging.DEBUG)
mh.addHandler(monitor)

mh.info("info mh")
mh.trace("trace mh")
plx.info("pylogx info")
plx.info("pylogx trace")
