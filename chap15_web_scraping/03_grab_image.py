import requests
import bs4
import shutil
import os

root = './tmp/15/03'


def setup():
    try:
        if os.path.exists(root):
            shutil.rmtree(root)
        os.makedirs(root)
    except Exception as e:
        print(e)


def grab_images():
    res = requests.get(
        'https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    for image in soup.select('.image'):
        image_src = f"http:{image.select('img')[0].get('src')}"
        print(image_src)
        image_name = image_src.split('/')[-1]
        image_content = requests.get(image_src).content
        with open(f'{root}/{image_name}', 'wb') as f:
            f.write(image_content)


setup()
grab_images()
