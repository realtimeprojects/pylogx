import logging
from pylogx import log, IndentFilter

formatter = logging.Formatter(fmt="%(asctime)s %(indent)s%(message)s")
sh = logging.StreamHandler()
sh.setFormatter(formatter)
log.addHandler(sh)

iflt = IndentFilter(indent=" => ")
log.addFilter(iflt)

log.info("base level")

iflt.inc()
log.info("sub level")

iflt.inc()
log.info("sub sub level")

iflt.dec()
log.info("sub level")
