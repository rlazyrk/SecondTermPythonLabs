import logging


def exception_logger(exception, mode):
    def inner_func(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                if mode == "log":
                    logging.basicConfig(level=logging.ERROR, filename="program_exception_log.log", filemode="w")
                    logging.error(e)
                elif mode == "console":
                    logging.basicConfig(level=logging.ERROR)
                    logging.error(e)
                else:
                    raise ValueError("mode must be 'log' or 'console'")

        return wrapper

    return inner_func
