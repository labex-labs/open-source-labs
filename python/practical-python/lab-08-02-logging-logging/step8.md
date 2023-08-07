# Exercise 8.3: Adding Logging to a Program

To add logging to an application, you need to have some mechanism to initialize the logging module in the main module. One way to do this is to include some setup code that looks like this:

    # This file sets up basic configuration of the logging module.
    # Change settings here to adjust logging output as needed.
    import logging
    logging.basicConfig(
        filename = 'app.log',            # Name of the log file (omit to use stderr)
        filemode = 'w',                  # File mode (use 'a' to append)
        level    = logging.WARNING,      # Logging level (DEBUG, INFO, WARNING, ERROR, or CRITICAL)
    )

Again, you'd need to put this someplace in the startup steps of your program. For example, where would you put this in your `report.py` program?
