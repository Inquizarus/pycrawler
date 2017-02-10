"""
Tests the base crawler
"""

import unittest
from crawler.Crawler import Crawler

class CrawlerTest(unittest.TestCase):

    def testItCanCrawl(self):
        crawler = Crawler()
        crawler.add_to_crawl('http://google.se')
        crawler.crawl()

    def testItReturnsTheCrawledUrls(self):
        crawler = Crawler();
        urlsToCrawl = ['http://google.se', 'http://aftonbladet.se']
        for url in urlsToCrawl:
            crawler.add_to_crawl(url)
        result = crawler.crawl()
        self.assertEquals(urlsToCrawl, result, 'Not all urls that was supposed to be crawled was crawled.')
    