from html.parser import HTMLParser
from collections import Counter
import string
import re
import sys

class MyHTMLParser(HTMLParser):
    
    """
    A subclass of HTMLParser that collects all text data,
    filters out tokens containing punctuation, and can report
    word frequencies and dump raw text to a file.
    """
    def __init__(self):
        super().__init__()
        email_regex = r"^[a_zA_Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    def handle_starttag(self, tag, attrs):
        if "a" == tag.lower():
            return
        starttag_search = re.search(self.email_regex, attrs.join())

        pass
        
    def handle_data(self, data):
        pass

if __name__ == '__main__':
    # Fetch and parse the page again
    link = 'https://collegeofsanmateo.edu/wellnesscenter'
    from urllib.request import urlopen

    resp = urlopen(link)
    html = resp.read().decode().lower()

    main = main_search.group()
    # print(main)
    parser = MyHTMLParser()
    parser.feed(main)

    # Show frequency for words occurring >= 10 times
    parser.frequency(6)
    print(parser.counter.get("wellness"))
    parser.print_clean_data()
