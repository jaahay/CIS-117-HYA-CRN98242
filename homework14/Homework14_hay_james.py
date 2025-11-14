from html.parser import HTMLParser
import re

def make_wow_email_regex():
    '''
    see: https://stackoverflow.com/questions/201323/how-can-i-validate-an-email-address-using-a-regular-expression
    I modified it to prevent things like "?cc=" and "cc=". They will still be captured.
    '''
    # return r"(?:[a-z0-9!#$%&'*+\x2f=?^_`\x7b-\x7d~\x2d]+(?:\.[a-z0-9!#$%&'*+\x2f=?^_`\x7b-\x7d~\x2d]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9\x2d]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9\x2d]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9\x2d]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    return r"(?:[a-z0-9\x2f\x7b-\x7d~\x2d]+(?:\.[a-z0-9!#$%&'*+\x2f=?^_`\x7b-\x7d~\x2d]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9\x2d]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9\x2d]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9\x2d]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"

wow_email_regex = make_wow_email_regex()

class MyHTMLParser(HTMLParser):
    
    """
    A subclass of HTMLParser that collects all text data,
    filters out tokens containing punctuation, and can report
    word frequencies and dump raw text to a file.
    """
    def __init__(self):
        super().__init__()
        self.emails = []

    def handle_starttag(self, tag, attrs):
        if "a" != tag.lower():
            return
        href = [item for item in attrs if item[0] == "href"]
        href = href[0]
        if not href[1].startswith("mailto:"):
            return
        self.emails.append(href[1])

    def handle_data(self, data):
        # email_groups = re.finditer(self.email_regex, data)
        email_groups = re.finditer(wow_email_regex, data)
        # if email_groups is None:
        #     return
        for email in email_groups:
            self.emails.append(email.group(0))

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