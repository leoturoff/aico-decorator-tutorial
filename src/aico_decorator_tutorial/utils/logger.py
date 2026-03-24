import logging
import os

DEBUG = bool(int(os.getenv("DEBUG", 0)))

logging.basicConfig(
    level=logging.DEBUG if DEBUG else logging.INFO,
    format="[%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger(__name__)
logger.info(f"Debug mode: {'ON' if DEBUG else 'OFF'}")
