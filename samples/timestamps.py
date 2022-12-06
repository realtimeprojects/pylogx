import time
import logging
from pylogx import log, PrettyDelta, Level

pd = PrettyDelta()
prd = PrettyDelta(name="prettyRelativeDelta", fmt="+%M:%S.%f", relative=True)
formatter = logging.Formatter(fmt="%(prettyDelta)s [%(prettyRelativeDelta)s] %(message)s")
sh = logging.StreamHandler()
sh.setFormatter(formatter)
log.addHandler(sh)
log.setLevel(Level.INFO)

log.warning("1 enjoy relative timestamps")
time.sleep(1)
log.info("2 enjoy relative timestamps")
time.sleep(2)
log.info("3 enjoy relative timestamps")
