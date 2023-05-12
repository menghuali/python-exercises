import requests
import bs4
import os
import shutil


def get_page_content(link):
    res = requests.get(link)
    return res.text


def get_authors(soup: bs4.BeautifulSoup):
    return set(author.text for author in soup.select('.author'))


def get_quotes(soup: bs4.BeautifulSoup):
    return [quote.select('.text')[0].text for quote in soup.select('.quote')]


def get_top10_tags(soup: bs4.BeautifulSoup):
    top10 = soup.find_all('h2', string='Top Ten tags').pop().parent
    return [tag.text for tag in top10.select('a')]


def first_page():
    print('\n\n=== First Page ===')
    link = 'http://quotes.toscrape.com/page/1/'
    page_content = get_page_content(link)
    soup = bs4.BeautifulSoup(page_content, 'lxml')
    authors = get_authors(soup)
    print(f'\nAuthors: {authors}')
    quotes = get_quotes(soup)
    print(f'\nQuotes: {quotes}')
    top10_tags = get_top10_tags(soup)
    print(f'\nTop 10 Tags: {top10_tags}')


def loop_pages():
    print('\n\n=== Authors of All Pages ===')
    page = 1
    res = requests.get(f'http://quotes.toscrape.com/page/{page}/')
    authors = set()
    page_authors = get_authors(bs4.BeautifulSoup(res.text, 'lxml'))
    while len(page_authors) > 0:
        authors.update(page_authors)
        page += 1
        res = requests.get(f'http://quotes.toscrape.com/page/{page}/')
        page_authors = get_authors(bs4.BeautifulSoup(res.text, 'lxml'))

    print(authors)


first_page()
loop_pages()
