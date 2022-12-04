from datetime import datetime, timedelta
import logging
from pylogx import log, ColorFormatter, IndentFilter, PrettyDelta, Level, levels
import time

indentFilter = IndentFilter()
prettyDelta = PrettyDelta(datetime.now() - timedelta(days=1, hours=12))
prettyRelativeDelta = PrettyDelta(name="prettyRelativeDelta", fmt="+%M:%S.%f", relative=True)
console = logging.StreamHandler()
console.setFormatter(ColorFormatter(fmt="%(prettyDelta)s [%(prettyRelativeDelta)s] %(indent)s %(message)s",
                                    ups=[Level.NOTE]))
console.setLevel(Level.NOTE)
log.addHandler(console)
log.addFilter(indentFilter)
log.addFilter(prettyDelta)
log.addFilter(prettyRelativeDelta)


log.trace("trace message")
indentFilter.inc()
log.warning("warning message")
indentFilter.inc()
log.info("info message")
indentFilter.dec()
log.info("info message")
log.note("note message1")
time.sleep(1)
log.note("note message2")
time.sleep(1)
log.note("note message3")
time.sleep(1)
log.info("info message")
levels[Level.TRACE]['color'] = "cyan"
log.trace("trace message in cyan")
