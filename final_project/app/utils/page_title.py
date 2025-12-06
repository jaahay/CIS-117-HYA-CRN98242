from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_page_title(url):
    """
    Retrieves the title of a webpage using urllib and BeautifulSoup.
    """
    try:
        # Open the URL and read the HTML content
        response = urlopen(url)
        html_content = response.read()

        # Decode the HTML content
        decoded_html = html_content.decode('utf-8')

        # Parse the HTML with BeautifulSoup
        soup = BeautifulSoup(decoded_html, 'html.parser')

        # Extract the title tag and its text
        title_tag = soup.title
        if title_tag:
            return title_tag.text.strip()
        else:
            return "Title not found"

    except Exception as e:
        return f"Error: {e}"
