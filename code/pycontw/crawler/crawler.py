import time
import os
import sys
import django
import requests
import logging
import uuid
import lazy_logger
from collections import OrderedDict

from django.conf import settings

from selenium import webdriver
from bs4 import BeautifulSoup as bs


logger = logging.getLogger(__name__)


if not settings.configured:
    """setting the Django env()"""
    logger.debug('settings.configured: {0}'.format(settings.configured))
    sys.path.append('/Users/chairco/OneDrive/SourceCode/django/pycon/2017-talk/code/pycontw')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pycontw.settings.local')
    django.setup()
    logger.debug('settings.configured: {0}'.format(settings.configured))



class Crawler(object):
    """
    Creates a new instance of the Service
    
    :Args:
     - driver_path : Path to PhantomJS binary
     - log_path : Path to PhantomJS's log
     - executable_path : Path to PhantomJS binary
     - port : Port the service is running on 
     - service_args : A List of other command line options to pass to PhantomJS
    """

    def __init__(self, *args, **kwargs):
        super(Crawler, self).__init__()
        self.args = args
        self.kwargs = kwargs
        self.BASE_DIR = settings.BASE_DIR

    def driver(self):
        service_args = [
        '--webdriver-loglevel=ERROR'  # only record ERROR message
        '--proxy=127.0.0.1:3128',
        ]
        driver = webdriver.PhantomJS(
            executable_path=self.driver_path, # 設定 dirver 路徑
            service_log_path=self.logs_path, # 設定 log 路徑位置
            #service_args=service_args,
        )
        return driver

    @property
    def logs_path(self):
        logs_path = os.path.join(self.BASE_DIR, 'logs', 'ghostdriver.log')
        if not os.path.isdir(os.path.dirname(logs_path)): os.mkdir(os.path.dirname(logs_path))
        return self.kwargs.get('logs_path', logs_path)

    @property
    def driver_path(self):
        def_driver_path = os.path.join(self.BASE_DIR, 'crawler', 'phantomjs-2.1.1', 'bin', 'phantomjs')
        driver_path = self.kwargs.get('driver_path', def_driver_path)
        
        if not os.path.exists(driver_path):
            raise Exception(driver_path + ' Not Exist')
        return driver_path

    def __del__(self):
        pass


def log_time():
    """return str time
    """
    return str(time.strftime("%Y%m%d%H%M", time.localtime(time.time())))


def test_lazylog(f):
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


@test_lazylog
@logger.patch
def test(url, *args, **kwargs):
    PHANTOMJS='/Users/chairco/OneDrive/SourceCode/django/radar/radar/nimbus/phantomjs-2.1.1/bin/phantomjs'
    crawler = Crawler(driver_path=PHANTOMJS)
    driver = crawler.driver()
    driver.get(url)
    pageSource = driver.page_source
    soup = bs(pageSource, "html.parser")
    #print(soup.title, type(soup.title))
    print('{}, {}'.format(type(soup.title), soup.title))
    #logger.info('{}'.format(soup.title))
    driver.close()
    ret = OrderedDict((('ret', 255), ('status', 'success'), ('version', '')))
    logs = get_log(file=kwargs['log_path'], title='test')
    ret.update(logs)
    return logs



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')
    print(test(url='http://pala.tw/js-example/'))