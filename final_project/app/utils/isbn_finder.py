import json
from urllib.request import urlopen
import urllib.parse

def find_isbn(title: str) -> str:
    """
    A utility function to find ISBN based on book title.
    This is a placeholder function and should be replaced with actual implementation.
    """
    try:
        fields = "isbn"
        url = f"https://openlibrary.org/search.json?title={urllib.parse.quote(title)}&fields={fields}"
        print(url);
        response = urlopen(url)
        html_content = response.read().decode('utf-8')
        data = json.loads(html_content)
        # print(data)
        if data['docs']:
            return data['docs'][0]['isbn'][0]
        else:
            return ""


    except Exception as e:
        print(f"Error fetching or parsing the URL: {e}")
        return ""