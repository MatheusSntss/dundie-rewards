import logging
import os
from logging import handlers

LOG_LEVEL = os.getenv("LOG_LEVEL", "WARNING").upper()
logger = logging.getLogger("dundie")
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")


def get_logger(file_log="dundie.log"):
    """Returns configured logs"""
    file_handler = handlers.RotatingFileHandler(
        file_log, maxBytes=10**6, backupCount=10
    )
    file_handler.setLevel(LOG_LEVEL)
    # Formatando a saída
    file_handler.setFormatter(formatter)

    # Associando o handler ao logger
    logger.addHandler(file_handler)
    return logger
