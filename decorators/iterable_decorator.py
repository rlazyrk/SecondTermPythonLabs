"""
model with iterable decorator
"""

from typing import Iterable


def iterable_decorator(func):
    """
    :param func:
    :return:
    """
    def wrapper(*args, **kwargs):
        if isinstance(func(*args, **kwargs), Iterable):
            print(f"object is iterable, len = {len(func(*args, **kwargs))}")
        else:
            print("object is not iterable, len = 1")
        return func(*args, **kwargs)

    return wrapper
