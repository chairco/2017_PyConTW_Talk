from .crawler import Crawler
import time

import logging

from bs4 import BeautifulSoup as bs

logger = logging.getLogger(__name__)


def log_time():
    """return str time
    """
    return str(time.strftime("%Y%m%d%H%M", time.localtime(time.time())))


def crawler_job(url):
    crawler = Crawler()
    driver = crawler.driver()
    driver.get(url)
    pageSource = driver.page_source
    driver.close()
    return pageSource
    
    #PHANTOMJS='/Users/chairco/OneDrive/SourceCode/django/radar/radar/nimbus/phantomjs-2.1.1/bin/phantomjs'
    #crawler = Crawler(driver_path=PHANTOMJS)
    #driver = crawler.driver()
    #driver.get(url)
    #pageSource = driver.page_source
    #soup = bs(pageSource, "html.parser")
    #print(soup.title, type(soup.title))
    #driver.close()
    #return pageSource