import shutil
import os
import re

root = './tmp/14/09'


def setup():
    try:
        if os.path.exists(root):
            shutil.rmtree(root)
        os.makedirs(root)
    except Exception as e:
        print(e)


def unzip_me_instructions():
    shutil.unpack_archive(
        'chap14_advanced_modules/unzip_me_for_instructions.zip', f'{root}/instruction', 'zip')


def find_phone_number():
    pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
    it = os.walk(root)
    item = next(it, None)
    while item:
        folder = item[0]
        files = item[2]
        for file in files:
            phone_nums = None
            with open(f'{folder}/{file}', 'r+') as f:
                phone_nums = re.findall(pattern, f.read())
            if len(phone_nums) > 0:
                print(phone_nums)

        item = next(it, None)


setup()
unzip_me_instructions()
find_phone_number()
