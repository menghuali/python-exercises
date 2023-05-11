import requests
import os
import shutil
import bs4

root = 'tmp/15/04'


def setup():
    try:
        if os.path.exists(root):
            shutil.rmtree(root)
        os.makedirs(root)
    except Exception as e:
        print(e)


def book_2stars():
    soup = bs4.BeautifulSoup(requests.get('http://books.toscrape.com/').text, 'lxml')
    books = soup.select('.star-rating.Two')
    for book in books:
        title = book.parent.select('h3')[0].select('a')[0].get('title')
        print(title)

setup()
book_2stars()