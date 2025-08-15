import os

import requests
from bs4 import BeautifulSoup

os.system('cls')

url = 'http://localhost:8000/'
response = requests.get(url)

raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')

# print(parsed_html.title)

article_heading = parsed_html.select_one('#intro > div > div > article > h2')

if article_heading is not None:
    print(article_heading.text)
    article = article_heading.parent

    if article is not None:
        for p in article.select('p'):
            print(p.text)
            print(p.text)
