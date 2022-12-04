# pylox documentation

## Color customizatoin

An easy way to customize the colors of the log messages is to update the level definitions.

    import pylogx
    pylogx.levels[pylogx.Level.TRACE]['color'] = "cyan"

Check the [termcolor](https://pypi.org/project/termcolor/) documentation for the supported colors.

## Level Configuration

### Register custom levels

You can register custom levels using the `registerLevel()` functions.

    import pylogx
    pylogx.registerLevel(35, {"name": "HEAVYW", "color": "yellow",  "on_color": null, "attrs": ["bold"]})

Or read your own [level json definition](../pylogx/levels.json) file using the `readLevels()` function:

    import pylogx
    pylogx.readLevels("mylevels.json")

### Default pylox levels

By default, all levels defined in the [level json file](../pylogx/levels.json) are
activated / configured.

However, by setting the environment variable PYLOGX\_LEVELS, you can control,
which levels should be added:

        PYLOGX_LEVELS=TRACE,SUCCESS

will only activate the TRACE and SUCCESS level and ignore all other level definitions.
