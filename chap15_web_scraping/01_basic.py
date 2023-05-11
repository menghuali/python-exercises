import requests
import bs4


# Get a Web site
result = requests.get("http://www.example.com")

# Grab tags
soup = bs4.BeautifulSoup(result.text, 'lxml')
print(soup.select('title'))
print(soup.select('title')[0].get_text())

site_paragraph = soup.select('p')
print(site_paragraph[0].get_text())


