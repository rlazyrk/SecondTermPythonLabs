"""
module with logging decorator
"""

import logging


def loging_decorator(func):
    """
    :param func:
    :return:
    """

    def wrapper(*args, **kwargs):
        logging.basicConfig(level=logging.INFO, filename="program_log.log", filemode="w")
        logging.info(f"function call -> {func.__name__} ")
        for i in args:
            logging.info(f"function args -> {i}")
        logging.info(f"function result -> {func(*args, **kwargs)}")
        return func(*args, **kwargs)

    return wrapper
