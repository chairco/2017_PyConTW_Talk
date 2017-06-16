import lazy_logger
import time


def test_log_to_console(capsys):
    logger = lazy_logger.get_logger('noname')
    lazy_logger.log_to_console(logger)
    logger.debug('yo')

    out, err = capsys.readouterr()
    assert err[0:10] == time.strftime("%Y-%m-%d")
    assert err[26:] == 'noname - DEBUG - yo\n'


def test_log_to_rotated_file(tmpdir):
    logger = lazy_logger.get_logger('noname')
    file_path = tmpdir.join(lazy_logger.FILE_NAME).strpath
    lazy_logger.log_to_rotated_file(logger, lazy_logger.LOGGER_LEVEL, lazy_logger.HANDLER_LEVEL,
        '%(message)s', 100, file_path)
    logger.debug('y'*100)
    logger.debug('y')

    log_out_1 = open(file_path+'.1', 'r')
    assert log_out_1.read() == 'y'*100+'\n'
    log_out_1.close()
    log_out = open(file_path, 'r')
    assert log_out.read() == 'y'+'\n'
