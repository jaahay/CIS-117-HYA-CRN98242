from bs4 import BeautifulSoup
from urllib.request import urlopen

def parse_book_for_uuid(url: str):
    """
    Parses the HTML content of a book page to extract the UUID (ISBN).
    Assumes that the ISBN is contained within a specific HTML element.
    """
    try:
        response = urlopen(url)
        html_content = response.read().decode('utf-8')
        soup = BeautifulSoup(html_content, 'html.parser')
        ebook_no = extract_row(soup, "EBook-No.")
        title = extract_row(soup, "Title")
        author = extract_row(soup, "Author")
        original_publication = extract_row(soup, "Original Publication")
        return { "ebook_no": ebook_no, "title": title, "author": author, "original_publication": original_publication }

    except Exception as e:
        print(f"Error fetching or parsing the URL: {e}")
        return None

def extract_row(soup: BeautifulSoup, target_value: str) -> str:
    target_row = soup.select_one(f'#about_book_table tr:has(th:contains("{target_value}"))')

    if target_row:
        print(f"Found row containing '{target_value}':")
        print(target_row.prettify())
    else:
        print(f"Row containing '{target_value}' not found.")
    return target_row.th.find_next_sibling('td').text.strip() if target_row else ""