# error_logger.py
# Captures and logs errors and anomalies

import logging
from logging.handlers import RotatingFileHandler

class ErrorLogger:
    def __init__(self, log_file='error.log'):
        # Set up a logger with a rotating file handler
        self.logger = logging.getLogger('ErrorLogger')
        self.logger.setLevel(logging.DEBUG)  # Capture all levels of logs

        # Create a file handler that logs even debug messages
        file_handler = RotatingFileHandler(log_file, maxBytes=1024*1024*5, backupCount=5)
        file_handler.setLevel(logging.DEBUG)

        # Create a console handler with a higher log level
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.ERROR)

        # Create a formatter and set it for the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add the handlers to the logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def log_error(self, error):
        """ Log an error message """
        self.logger.error(error)

    def log_warning(self, warning):
        """ Log a warning message """
        self.logger.warning(warning)

    def log_info(self, info):
        """ Log an informational message """
        self.logger.info(info)

    def log_debug(self, debug):
        """ Log a debug message """
        self.logger.debug(debug)

# Example usage
if __name__ == '__main__':
    error_logger = ErrorLogger()

    # Logging examples
    error_logger.log_error("This is an error message")
    error_logger.log_warning("This is a warning message")
    error_logger.log_info("This is an info message")
    error_logger.log_debug("This is a debug message")
