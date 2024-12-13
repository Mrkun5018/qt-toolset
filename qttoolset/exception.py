import logging
from logging import Logger
from typing import Optional, Union
import functools


class Catch:
    logger: Optional[Logger] = None

    @classmethod
    def set_logger(cls, logger: Union[Logger, str], logfile: Optional[str] = None):
        """
        Sets the logger for the Catch class.

        Args:
            :param logger: The logger to be used.
            :param logfile:
        """
        if isinstance(logger, str):
            cls.logger = logging.getLogger(logger)
        else:
            cls.logger = logger

        if logfile is not None:
            cls.logger.addHandler(logging.FileHandler(logfile))

    @classmethod
    def catch_exception(cls, func):
        """
        A decorator that catches any exceptions that occur in the wrapped function and logs them.

        Args:
            func: The function to be wrapped.

        Returns:
            A wrapped function that catches any exceptions and logs them.
        """
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                cls.logger.exception(e)
        return wrapper

