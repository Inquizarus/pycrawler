from classes.file.JsonFile import JsonFile
from classes.crawler.Crawler import Crawler
from classes.parser.LinkParser import LinkParser
import os

path = os.path.dirname(os.path.abspath(__file__)) + "/config/sites.json"

sites = JsonFile(path)
crawled = [];
parser = LinkParser()

for site in sites.load():
    parser.reset_container()
    crawler = Crawler(parser)
    crawler.set_verbose(True)

    for requirement in site["requirements"]:
        crawler.add_requirement(requirement)

    crawler.add_to_crawl(site["url"])
    crawler.crawl()
    print crawler.get_container()
