from HTMLParser import HTMLParser

class LinkParser(HTMLParser):

    container = []

    def get_container(self):
        return self.container

    def reset_container(self):
        self.container = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if 'href' in attr[0]:
                    self.container.append(attr[1])
