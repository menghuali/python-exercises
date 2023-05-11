import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(res.text, 'lxml')
tocs = soup.select('.vector-toc-text')

print(tocs[2])
contents = [list(toc.children)[-1] for toc in tocs]
print(contents)

contents_numbered = [toc.get_text(separator=': ', strip=True) for toc in tocs]
print(contents_numbered)
