import functools
from loguru import logger
import sys

defined_log_levels = ['TRACE', 'DEBUG', 'INFO', 'SUCCESS', 'WARNING', 'ERROR', 'CRITICAL']


def init_logger(level='NOLOG', backtrace=False, diagnose=False, file_log=False, file_log_level="WARNING"):
    logger.remove()
    if level != 'NOLOG':
        logger.add(sys.stderr, level=level, backtrace=backtrace,
                   diagnose=diagnose, colorize=True)
        if file_log:
            logger.add("error_log.log", serialize=True, level=file_log_level, backtrace=backtrace,
                       diagnose=diagnose, rotation="1 day", retention="7 days", compression="zip")


def log_anime_info(anime,msg=""):
    logger.debug(f"{msg} {anime.a_id}, {anime.title}, {anime.slug}, {anime.type}, {anime.episodes_length}")


def logger_wraps(*, entry=True, exit=True, level="TRACE"):
    def wrapper(func):
        name = func.__name__

        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            logger_ = logger.opt(depth=1)
            if entry:
                logger_.log(level, "Entering '{}' (args={}, kwargs={})", name, args, kwargs)
            result = func(*args, **kwargs)
            if exit:
                logger_.log(level, "Exiting '{}' (result={})", name, result)
            return result

        return wrapped

    return wrapper
