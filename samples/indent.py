import logging
from pylogx import log, Indent

formatter = logging.Formatter(fmt="%(asctime)s %(indent)s%(message)s")
sh = logging.StreamHandler()
sh.setFormatter(formatter)

indent = Indent(indent=" => ")

logging.getLogger().addHandler(sh)

log.info("base level")

indent.inc()
log.info("sub level")

indent.inc()
log.info("sub sub level")

dd = logging.getLogger("dd")
dd.warning("hello")

indent.dec()
log.info("back to sub level")
