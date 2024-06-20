"""Module that print loggings while the application is running."""
import logging


def setup_logging(app):
    """
    The function write log for the code when the application is running.
    """
    # Define the logger
    logger = logging.getLogger('PetClinic')
    logger.setLevel(logging.DEBUG)

    # Define the file handler to log to a file in the logs directory
    console_handler = logging.StreamHandler()
    #file_handler = logging.FileHandler('app.log')

    # Set level for handlers
    console_handler.setLevel(logging.DEBUG)
    #file_handler.setLevel(logging.DEBUG)


    # Deine the log format
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    #file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(console_handler)
    #logger.addHandler(file_handler)

    app.logger.handlers = logger.handlers
    app.logger.setLevel(logger.level)

    return logger
