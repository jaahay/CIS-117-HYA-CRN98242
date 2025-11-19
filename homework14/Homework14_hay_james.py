from html.parser import HTMLParser
from email_extractor import extract_emails

class MyHTMLParser(HTMLParser):
    
    """
    A subclass of HTMLParser that collects all text data,
    filters out tokens containing punctuation, and can report
    word frequencies and dump raw text to a file.
    """
    def __init__(self):
        super().__init__()
        self.emails = set()

    def handle_starttag(self, tag, attrs):
        if "a" != tag.lower():
            return
        hrefs = [item for item in attrs if item[0] == "href"]
        assert len(hrefs) == 1, "duplicate href attributes detected"
        href = hrefs[0][1]
        if href is not None:
            self.emails.update(
                extract_emails(href)
            )

    def handle_data(self, data):
        self.emails.update(
            extract_emails(data)
        )

if __name__ == '__main__':
    # Fetch and parse the page again
    # link = 'https://collegeofsanmateo.edu/wellnesscenter'
    link = 'https://maildiver.com/blog/mailto-links-complete-guide/'
    from urllib.request import urlopen

    resp = urlopen(link)
    html = resp.read().decode().lower()

    parser = MyHTMLParser()
    parser.feed(html)

    print(parser.emails)