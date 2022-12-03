import time
import logging
from pylogx import log, PrettyDelta, Level

pd = PrettyDelta()
log.addFilter(pd)
prd = PrettyDelta(name="prettyRelativeDelta", fmt="+%M:%S.%f", relative=True)
log.addFilter(prd)
formatter = logging.Formatter(fmt="%(prettyDelta)s [%(prettyRelativeDelta)s] %(message)s")
sh = logging.StreamHandler()
sh.setFormatter(formatter)
log.addHandler(sh)
log.setLevel(Level.INFO)

log.warning("enjoy relative timestamps")
time.sleep(1)
log.info("enjoy relative timestamps")
time.sleep(2)
log.info("enjoy relative timestamps")
