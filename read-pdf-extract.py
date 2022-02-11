import sys
sys.path.append('/Users/deniskusic/miniconda3/lib/python3.8/site-packages')
import pdfplumber as pdfP
import os
from datetime import datetime


pathname1 = '/Users/deniskusic/Documents/Personal/Deliveroo/invocies/'
filename1 = '2020-12-04_06.pdf'
src = pathname1 + 'invocies1/'
total = 0
all_files = os.listdir(src)
list_of_failed_files = []


def extractTextFromPdf(filename,page_num = 0):
    """Takes filename and returns the text in that file as string
Assumes filename is a string, absolute path to file, which is a pdf.
returns entire text in the pdf; type string"""
    # TODO improve specification
    with pdfP.open(filename) as pdf:
        page = pdf.pages[page_num]
        text = page.extract_text()
    return text

def extract_total_and_date(PDFtext):
    total = -2
    date = 4
    PDFtext_list = PDFtext.split('\n')
    return (PDFtext_list[date],PDFtext_list[total])

for file in os.listdir(src):
    print(f'Filename:{file}')
    # Extract text
    PDF = extractTextFromPdf(src + file)
    # Extract time window and earnings
    name, earnings = extract_total_and_date(PDF)
    # Rename file

    # Format earnings
    print(earnings)
    try:

        total += float(earnings[6:].strip('£'))
        os.rename(src + file,pathname1 + name + '.pdf')
    except ValueError:
        print(f'Failed on filename:\n{file}')# One file has two pages
        continue
print(total)

##src1 = pathname1
##total1 = 0
##for file in os.listdir(src1):
##    if file[-3:] == 'pdf':
##        PDF = extractTextFromPdf(src1 + file)
##    else:
##        continue
##    name, earnings = extract_total_and_date(PDF)
##    print(f'Period:{name[30:]}; {earnings}')
##    total1 +=  float(earnings[6:].strip('£'))
##    print(f'Total = {total1}£')
##print('Total earned', round(total1, ndigits=2))

    # use this link for further manipulation https://www.youtube.com/watch?v=syEfR1QIGcY
def main():
    # extract text from invoice
    # Extract invoicing period and total money earned
    # Rename file
    # Tally up earnings from each file
