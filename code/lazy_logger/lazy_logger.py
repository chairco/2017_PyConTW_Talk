import logging
import logging.handlers
import functools


FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOGGER_LEVEL = logging.DEBUG
HANDLER_LEVEL = logging.DEBUG

root_logger = logging.getLogger()

_real_print = print


def monkeypatch_method(cls):
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func
    return decorator


def _fake_print_generator(logger):
    def _fake_print(*args, file=None, **kwargs):
        if file is None:
            logger.debug(*args, **kwargs)
        else:
            _real_print(*args, file=file, **kwargs)
    return _fake_print


@monkeypatch_method(logging.Logger)
def patch(self, f):
    @functools.wraps(f)
    def patched(*args, **kwargs):
        import builtins
        builtins.print = _fake_print_generator(logger=self)
        try:
            result = f(*args, **kwargs)
        finally:
            builtins.print = _real_print
        return result
    return patched


def get_logger(name=None):
    return logging.getLogger(name)


def log_to_console(logger=root_logger,
                   logger_level=LOGGER_LEVEL,
                   handler_level=HANDLER_LEVEL,
                   logging_format=FORMAT):
    '''
    :param logger: if not set, will apply settings to root logger
    :param logger_level:
    :param handler_level:
    :param logging_format:
    :return:
    '''

    logger.setLevel(logger_level)

    handler = logging.StreamHandler()
    handler.setLevel(handler_level)

    formatter = logging.Formatter(logging_format)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


FILE_NAME = 'log.out'
MAX_BYTE = 10 * 1024 * 1204
BACK_COUNT = 10


def log_to_rotated_file(logger=root_logger,
                        logger_level=LOGGER_LEVEL,
                        handler_level=HANDLER_LEVEL,
                        logging_format=FORMAT,
                        max_byte=MAX_BYTE,
                        file_name=FILE_NAME,
                        back_count=BACK_COUNT):

    # Set up a specific logger with our desired output level
    logger.setLevel(logger_level)

    # Add the log message handler to the logger
    handler = logging.handlers.RotatingFileHandler(file_name, maxBytes=max_byte, backupCount=back_count)
    handler.setLevel(handler_level)

    formatter = logging.Formatter(logging_format)
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger


def log_to_syslogd(logger=root_logger,
                   address=None,
                   logger_level=LOGGER_LEVEL,
                   handler_level=HANDLER_LEVEL,
                   logging_format=FORMAT
                   ):

    assert address

    logger.setLevel(logger_level)

    handler = logging.handlers.SysLogHandler(address = address)
    handler.setLevel(handler_level)

    formatter = logging.Formatter(logging_format)
    handler.setFormatter(formatter)
    return logger


def main():

    logger = get_logger('test')

    log_to_console(logger)

    logger.debug('yo')  # should be show up in terminal

    @logger.patch
    def show():
        print("message in show")

    show()


if __name__ == "__main__":
    main()
