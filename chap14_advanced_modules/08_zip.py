import zipfile
import shutil
import os

dir = './tmp/14/08'
file1 = f'{dir}/file1.txt'
file2 = f'{dir}/file2.txt'
compressed = f'{dir}/compressed.zip'
extracted = f'{dir}/extracted'
shutil_zip = f'{dir}/shutil'

def setup():
    try:
        if os.path.exists(dir):
            shutil.rmtree(dir)
        os.makedirs(dir)
        with open(file1, 'w+') as f:
            f.write('File One')
        with open(file2, 'w+') as f:
            f.write('File Two')
    except Exception:
        pass


def zip():
    with zipfile.ZipFile(compressed, 'w') as zip:
        zip.write(file1, compress_type=zipfile.ZIP_DEFLATED)
        zip.write(file2, compress_type=zipfile.ZIP_DEFLATED)

def print_dirtree():
    with os.popen(f'tree {dir}') as stream:
        print(stream.read())

def unzip():
    with zipfile.ZipFile(compressed, 'r') as zip:
        zip.extractall(extracted)

def zip_with_shutil():
    shutil.make_archive(shutil_zip, 'zip', extracted)

def unzip_with_shutil():
    shutil.unpack_archive(f'{shutil_zip}.zip', f'{dir}/shutil_unzip', 'zip')

setup()
zip()
print_dirtree()

unzip()
print_dirtree()

zip_with_shutil()
print_dirtree()

unzip_with_shutil()
print_dirtree()