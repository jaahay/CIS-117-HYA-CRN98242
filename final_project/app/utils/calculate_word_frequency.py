from urllib.request import urlopen
from collections import Counter
import re
from .filler_words import filler_words

def calculate_word_frequency(url: str) -> dict:
    """
    Given a URL, fetch the content and calculate the frequency of each word.
    Returns a dictionary with words as keys and their frequencies as values.
    """

    try:
        # Open the URL and read the HTML content
        response = urlopen(url)
        html_content = response.read().decode('utf-8')

        # Remove HTML tags using a simple regex
        text = re.sub(r'<[^>]+>', '', html_content)

        # Split the text into words using regex to handle punctuation
        words = re.findall(r'\b\w+\b', text.lower())

        # Calculate word frequency using Counter
        word_frequency = Counter(word for word in words if word not in filler_words)

        return dict(word_frequency)

    except Exception as e:
        return {"error": str(e)}