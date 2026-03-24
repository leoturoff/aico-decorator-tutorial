import logging
import os

DEBUG = bool(int(os.getenv("DEBUG", 0)))

GREY = "\033[90m"
YELLOW = "\033[33m"
RED = "\033[31m"
ORANGE = "\033[38;5;208m"
RESET = "\033[0m"
LOG_COLOR = {
    logging.DEBUG: YELLOW,
    logging.INFO: GREY,
    logging.WARNING: ORANGE,
    logging.ERROR: RED,
    logging.CRITICAL: RED,
}


class ColoredFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        message = super().format(record)
        color = LOG_COLOR.get(record.levelno, RESET)
        return f"{color}{message}{RESET}"


handler = logging.StreamHandler()
handler.setFormatter(ColoredFormatter("[%(levelname)s] %(message)s"))

logging.basicConfig(
    level=logging.DEBUG if DEBUG else logging.INFO,
    handlers=[handler],
)
logger = logging.getLogger(__name__)
logger.info(f"Debug mode: {'ON' if DEBUG else 'OFF'}")
