"""terraform_to_ansible/logger.py"""

import logging
import os
from logging.handlers import TimedRotatingFileHandler


def setup_logger():
    """Setup main logger."""

    # Define parent directory to determine root log directory
    # Excluded in .gitignore
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define logs directory
    log_dir = os.path.join(parent_dir, "logs")
    # Define log file
    log_file = os.path.join(log_dir, "terraform_to_ansible.log")

    # Create logs directory if it does not exist
    if not os.path.isdir(log_dir):
        os.makedirs(log_dir)

    # Setup formatting
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    # Setup log
    logger = logging.getLogger()
    # Setup log level
    logger.setLevel(logging.DEBUG)

    # Setup console handler
    console_handler = logging.StreamHandler()
    # Setup console handler level
    console_handler.setLevel(logging.WARNING)
    # Add formatting to console handler
    console_handler.setFormatter(formatter)
    # Add console handler to log
    logger.addHandler(console_handler)

    # Setup file handler
    file_handler = TimedRotatingFileHandler(
        log_file, when="midnight", backupCount=7
    )
    # Setup file handler level
    file_handler.setLevel(logging.DEBUG)
    # Add formatting to file handler
    file_handler.setFormatter(formatter)
    # Add file handler to log
    logger.addHandler(file_handler)

    return logger
