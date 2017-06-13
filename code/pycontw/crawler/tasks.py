import time
import os
import sys
import django
import requests
import logging
import uuid
import lazy_logger

from collections import OrderedDict

from bs4 import BeautifulSoup as bs

from .crawler import Crawler

logger = logging.getLogger(__name__)


def log_time():
    """return str time
    """
    return str(time.strftime("%Y%m%d%H%M", time.localtime(time.time())))


def call_lazylog(f):
    def lazylog(*args, **kwargs):
        log_path = os.path.join(os.getcwd(), 'logs', log_time()+'-'+str(uuid.uuid1())+'.log')
        lazy_logger.log_to_console(logger)
        lazy_logger.log_to_rotated_file(logger=logger,file_name=log_path)
        logger.info('logger file: {0}'.format(log_path))
        kwargs['log_path'] = log_path
        return f(*args, **kwargs)
    return lazylog


def get_log(file, title):
    with open(file, 'rb') as fp:
        logs = OrderedDict([(title, fp.read())])
    return logs


@logger.patch
@call_lazylog
def crawler_job(url, *args, **kwargs):
    crawler = Crawler()
    driver = crawler.driver()
    driver.get(url)
    pageSource = driver.page_source
    soup = bs(pageSource, "html.parser")
    print('{}'.format(soup.title))
    driver.close()
    ret = OrderedDict((('ret', 255), ('status', 'success'), ('version', '')))
    logs = get_log(file=kwargs['log_path'], title='crawler_job')
    ret.update(logs)
    return ret


def job(url):
    log_path = os.path.join(os.getcwd(), 'logs', log_time()+'-'+str(uuid.uuid1())+'.log')
    lazy_logger.log_to_console(logger)
    lazy_logger.log_to_rotated_file(logger=logger,file_name=log_path)
    logger.info('logger file: {0}'.format(log_path))

    crawler = Crawler()
    driver = crawler.driver()
    driver.get(url)
    pageSource = driver.page_source
    soup = bs(pageSource, "html.parser")
    print('{}'.format(soup.title))
    driver.close()
    ret = OrderedDict((('ret', 0), ('status', 'Success'), ('version', '0.1')))
    logs = get_log(file=log_path, title='crawler_job')
    ret.update(logs)
    return ret




