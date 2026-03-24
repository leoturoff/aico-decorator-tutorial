from typing import Callable
from functools import wraps
from .logger import logger, DEBUG
from .exceptions import ControlledExit


def my_decorator(func: Callable) -> Callable:
    """Add debug logging to the function"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print()
        logger.debug(f"{func.__name__}: args={args}, kwargs={kwargs}")
        try:
            # Call the function normally
            result = func(*args, **kwargs)
            logger.debug(f"{func.__name__}: result={result}")
            print()
            return result
        except Exception as e:
            # Log the error and exit
            logger.error(f"{func.__name__}: {e.__class__.__name__}: {str(e)}")
            exit(1)

    if DEBUG is False:
        return func
    else:
        return wrapper


def debug_with_exits(func: Callable) -> Callable:
    """Add debug logging to the function"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print()
        logger.debug(f"{func.__name__}: args={args}, kwargs={kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.debug(f"{func.__name__}: result={result}")
            print()
            return result
        except ControlledExit as e:
            logger.warning(f"{func.__name__}: {e}")
            exit(0)
        except Exception as e:
            logger.error(f"{func.__name__}: Real Error! {e}")
            exit(1)

    if DEBUG is False:
        return func
    else:
        return wrapper
