import csv
import shutil
import os

root = 'chap17_spreadsheet_pdf'
tmp = 'tmp/17/01'


def init():
    if os.path.exists(tmp):
        shutil.rmtree(tmp)
    os.makedirs(tmp)


def read_csv():
    with open(f'{root}/example.csv', encoding='UTF-8') as csvfile:
        reader = csv.reader(csvfile)
        print(reader.line_num)

        data = list(reader)
        print(data[0])
        print(data[1])


def write_csv():
    with open(f'{tmp}/target.csv', mode='+a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['a', 'b', 'c'])
        writer.writerows([['1', '2', '3'], ['4', '5', '6']])


init()
write_csv()
