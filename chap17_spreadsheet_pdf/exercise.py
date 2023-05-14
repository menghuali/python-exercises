import csv
import PyPDF2
import re


def find_download_link():
    with open('chap17_spreadsheet_pdf/Exercise_Files/find_the_link.csv') as f:
        non_num = []
        csv_reader = csv.reader(f)
        for row in csv_reader:
            for cell in row:
                if not cell.isnumeric():
                    non_num.append(cell)
        return ''.join(non_num)


def find_phone_number():
    pdf_reader = PyPDF2.PdfReader(
        'chap17_spreadsheet_pdf/Exercise_Files/Find_the_Phone_Number.pdf')
    pattern = re.compile(r'\d{3}\.\d{3}\.\d{4}')
    for page in pdf_reader.pages:
        text = page.extract_text()
        phones = re.findall(pattern, text)
        if len(phones) > 0:
            print(' '.join(phones))


print(find_download_link())
find_phone_number()
