import os
import shutil
import send2trash

try:
    if os.path.exists('./tmp/14/02'):
        shutil.rmtree('./tmp/14/02')
    os.makedirs('./tmp/14/02/a')
    os.makedirs('./tmp/14/02/b')
    with open('tmp/12/02/a/practice.txt', 'w+') as f:
        f.write('This is a test string')
    with open('tmp/12/02/a/practice2.txt', 'w+') as f:
        f.write('This is a test string')
except Exception as e:
    pass

def print_dirtree():
    with os.popen('tree tmp/12/02') as stream:
        print(stream.read())

print('#0 Walk through a folder')
print(f'Current working directory (cwd)\t: {os.getcwd()}')
print(f'Directory tree (os.walk)\t: { list(os.walk("tmp/12/02"))}')

print('\n#1 Moving tmp/12/02/a/practice.txt to tmp/12/02/b')
shutil.move('tmp/12/02/a/practice.txt', 'tmp/12/02/b')
print_dirtree()

print('\n#2 Remove tmp/12/02/b/practice.txt')
os.unlink('tmp/12/02/b/practice.txt')
print_dirtree()

print('\n#3 Send tmp/12/02/a/practice2.txt to Trash')
send2trash.send2trash('tmp/12/02/a/practice2.txt')
print_dirtree()