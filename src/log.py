import logging
import os


def setup_logger(name, log_file, level=logging.DEBUG):
    """Настройка и создание логгера с заданными параметрами."""
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


os.makedirs('logs', exist_ok=True)
logger = setup_logger("logs", "logs/flog.log")
