import os
import shutil

import PyPDF2

root = 'chap17_spreadsheet_pdf'
tmp = 'tmp/17/02'


def init():
    if os.path.exists(tmp):
        shutil.rmtree(tmp)
    os.makedirs(tmp)


def read_pdf():
    reader = PyPDF2.PdfReader(f'{root}/Working_Business_Proposal.pdf')
    print(f'Number of Pages: {len(reader.pages)}')
    print(f'== Page 1 ==\n {reader.pages[0].extract_text()}')
    return reader.pages[0]


def write_pdf(page: PyPDF2.PageObject):
    with PyPDF2.PdfWriter() as writer:
        writer.add_page(page)
        writer.write(f'{tmp}/target.pdf')


init()
page = read_pdf()
write_pdf(page)
