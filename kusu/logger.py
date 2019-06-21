"""
Description:
    A wrapper for the standard library logging module. Contains configuration\
        for the logging of all modules and the main file.
Example:
    In main module use;
        from utilities.logger import setup_primary_logger
        PRIMARY_LOGGER = setup_primary_logger("Main")
        PRIMARY_LOGGER.debug("message from main")
    In submodules use;
        import logging
        logger = logging.getLogger('root')
        logger.debug('submodule message')
Attributes:
    LOG_FOLDER (str):Allows you to specify a directory to save log file(s) to\
        NOTE: do NOT include filename, specify that in the LOG_FILE_FORMAT variable
    LOG_LEVEL (int): sets logging level; see logging documentation for details\
        https://docs.python.org/3/library/logging.html#levels
    LOG_FORMAT (str): Allows you to format log output to file/stream see logging\
        documentation for other builtin options\
        https://docs.python.org/3/library/logging.html#logrecord-attributes
    LOG_FILE_FORMAT (str): Allows you to set the naming convention of the output file\
        by default it's <date>-primary.log
    NOW (datetime): An aliased call to datetime.datetime.now() because i'm lazy
"""
__author__ = "Kieran Wood"
__version__ = "0.0.1"
__maintainer__ = "Kieran Wood"
__email__ = "kieranw098@gmail.com"

import logging # Standard lib module used as backend for logging configuration
import os # Used to handle paths primarily
import datetime # Used in formatting strings to identify date and time

NOW = datetime.datetime.now()

LOG_FOLDER = os.path.join(os.path.dirname(__file__), "logs")
LOG_LEVEL = 10 # Equivalent to logging.DEBUG see https://docs.python.org/3/library/logging.html#levels for details 

# See https://docs.python.org/3/library/logging.html#logrecord-attributes for other builtin attributes
LOG_FORMAT = "{0} | %(levelname)s | %(module)s | : %(message)s ".format(NOW.time()) 

LOG_FILE_FORMAT = os.path.join(LOG_FOLDER, "{} {} {}-main.log".format(NOW.strftime("%B"), NOW.day, NOW.year))

def setup_primary_logger(name="main", log_to_stream=False):
    """A function to configure a primary logger. Please note\
        this should only be called once per project, not once per\
        module. For module usage details, see the readme.
    Args:
        name (str): The name of the logger; this will be used to\
            access it later on so make sure it's short.
        log_to_stream(bool): If True it will cause logs to be\
            output to the terminal as well as to the file.\
            defaults to False
    Returns:
        Logger: A logger configured based on passed variables
    """
    if "main" not in name: # If name is not main, change output file to have correct name
        LOG_FILE_FORMAT = os.path.join(LOG_FOLDER, "{} {} {}-{}.log".format(NOW.strftime("%B"), NOW.day, NOW.year, name))

    # Instantiate logger based on input name
    logger = logging.getLogger(name)

    #Sets handler levels
    logger.setLevel(LOG_LEVEL)

    # Create Formatter and handlers
    formatter = logging.Formatter(LOG_FORMAT)
    file_handler = logging.FileHandler(LOG_FILE_FORMAT)

    if log_to_stream: # If true this outputs logs to terminal
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        stream_handler.setLevel(LOG_LEVEL)
        logger.addHandler(stream_handler)

    # Set Formatter to handlers
    file_handler.setFormatter(formatter)

    # Add file handler to logger
    logger.addHandler(file_handler)

    return logger