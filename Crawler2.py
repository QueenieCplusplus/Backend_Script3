from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):
    def _init_(self, msg):
        super().__init__()

    def handle_starttag(self, tag, attrs):
        print(tag)

    def error(self, msg):
        pass

finder = LinkFinder()
finder.feed('<html><head><title></title></head><body><h1>Parsing !</h1></body></html>')

