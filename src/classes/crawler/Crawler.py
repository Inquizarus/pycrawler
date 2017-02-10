"""
Base class for crawling
"""

import requests

class Crawler:

    # Container for words that an url must contain to be crawled
    requirements = []

    # Container for urls which have been crawled and visited
    container = []

    # Container for urls which should be crawled
    toCrawl = []

    # Blacklisted urls
    blackList = []
    

    def __init__(self, parser):
        self.parser = parser
        self.verbose = False
        self.counter = 0

    def crawl(self):
        self.counter = self.counter + 1

        urls_to_crawl = []

        for url in self.toCrawl:
            if self.should_be_crawled(url) == True or len(self.toCrawl) == 1 and len(self.container) < 1:

                self.printOut("Crawling " + url)

                resp = requests.get(url)   # Crawl the url
                self.toCrawl.remove(url)   # To avoid eternal loops we remove the url from to crawl before next iteration
                self.add_to_container(url) # Urls that have been crawled goes into the container

                if resp.status_code == 200: # Only store urls from pages that was successfully fetched
                    self.parser.feed(resp.text) # Parse the received html
                    parser_urls = self.parser.get_container() # pluck out the links
                    self.parser.reset_container() # Reset links in parser

                    for parser_url in parser_urls: # We add new urls to a local container which will be added to the to crawl later
                        urls_to_crawl.append(parser_url)

            else:
                self.blackList.append(url)
                self.toCrawl.remove(url)

        for url_to_crawl in urls_to_crawl:
            self.add_to_crawl(url_to_crawl)

        if len(self.toCrawl) > 0:
            self.crawl()
        else:
            return

    def add_to_crawl(self, url):
        if url not in self.toCrawl and url not in self.container and url not in self.blackList:
            self.toCrawl.append(url)

    def add_to_container(self, url):
        if url not in self.container:
            self.container.append(url)

    def add_requirement(self, requirement):
        self.requirements.append(requirement)

    def should_be_crawled(self, url):

        shouldBeCrawled = False

        if url in self.toCrawl and url not in self.container:
            requirement_counter = 0
            for requirement in self.requirements:
                if requirement in url:
                    requirement_counter += 1
            if requirement_counter == len(self.requirements):
                shouldBeCrawled = True

        return shouldBeCrawled

    def printOut(self, text):
        if self.verbose is True:
            print text


    def get_container(self):
        return self.container

    def set_verbose(self, flag):
        self.verbose = bool(flag)
    
