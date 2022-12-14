# v1.0.2

-   `enable_colors()`: set level on logger, not on stream.

# v1.0.1

-   documentation fixes

# v1.0.0

-   refactoring of Indent and PrettyDelta,
    use RecordFactory instead of filters to be compatible
    with modules instanciating their own logger classes.
-   add `logger` argument to `enable\_colors()` to allow
    registering the colorized stream handler to a specific
    logger.

# v0.4.4

-   fix setting the logger functions for additional log levels
    malforming logger class.

# v0.4.3

-   export levels for color customization

# v0.4.2

-   fix import errors

# v0.4.1

-   update documentation

# v0.4.0

-   support user-defined levels.
    Check `registerLevel()` and `readLevels()` functions for custom level definition
-   add additional level "PENDING".

# v0.3.0

-   add `pylogx.enable_colors` for enabling colors with one command.

# v0.2.0

-   add log level "SUCCESS"

# v0.1.3

-   first official release
