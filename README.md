# pylogx
> python logging extensions supporting additional levels, colorization, indentation and more

## Features

-   Additional log levels (HINT, NOTE, TRACE) for more granularity
-   Colorize log messages based on the log level
-   Indent log messages
-   Log relative time stamps


## Quickstart

### Colorize your log messages

        import time
        import pylogx
        from pylogx import log

        pylogx.enable_colors(level=pylogx.Level.NOTE, ups=[pylogx.Level.NOTE])

        log.trace("Have fun with colorized log messages")
        log.note("This message disappears with the next log message")
        time.sleep(5)
        log.note("Another message disappearing soon..")
        time.sleep(5)
        log.success("Last message is gone")

### Indent your log messages

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

### Print log messages with relative time stamp

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
