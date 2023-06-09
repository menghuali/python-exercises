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


def book_2stars(page_content):
    soup = bs4.BeautifulSoup(page_content, 'lxml')
    books = soup.select('.star-rating.Two')
    for book in books:
        title = book.parent.select('h3')[0].select('a')[0].get('title')
        print(title)


def loop_bookstore():
    page = 1
    res = requests.get(
        f'https://books.toscrape.com/catalogue/page-{page}.html')
    while (res.status_code == 200):
        print(f'\n=== Page {page} ===')
        book_2stars(res.text)
        page += 1
        res = requests.get(
            f'https://books.toscrape.com/catalogue/page-{page}.html')


setup()
# book_2stars()
loop_bookstore()
