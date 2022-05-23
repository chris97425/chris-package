import requests
from bs4 import BeautifulSoup

def easy_scrape(url):
    r = requests.get(url)

    if r.status_code == 404:
        return f"error with the link: {url}"

    text_to_convert = r.text
    soup = BeautifulSoup(text_to_convert, 'html.parser')
    print(type(soup))
    return soup
