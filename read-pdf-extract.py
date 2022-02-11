import sys
sys.path.append('/Users/deniskusic/miniconda3/lib/python3.8/site-packages')
import pdfplumber as pdfP
import os
from datetime import datetime
# use this link for further manipulation https://www.youtube.com/watch?v=syEfR1QIGcY

wd = os.getcwd()
src = '/Users/deniskusic/Documents/Personal/Deliveroo/Invoices/Raw-invoices-for-processing/'
#total = 0
all_files = os.listdir(src)
list_of_failed_files = []

if len(all_files) ==0:
    print(f'Src dir {src}')
    print('Empty directory.')
    sys.exit(1)


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

# for file in os.listdir(src):
#     print(f'Filename:{file}')
#     # Extract text
#     PDF = extractTextFromPdf(src + file)
#     # Extract time window and earnings
#     name, earnings = extract_total_and_date(PDF)
#     # Format earnings
#     print(earnings)
#     try:
#         total += float(earnings[6:].strip('£'))
#         os.rename(src + file,pathname1 + name + '.pdf')
#     except ValueError:
#         print(f'Failed on filename:\n{file}')# One file has two pages
#         continue
# print(total)

def format_earnings(earnings, start_indx = 6):
    f_earnings = float(earnings[start_indx:].strip('£'))
    return f_earnings

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


def main(all_files):
    total = 0.0
    for invoice in all_files:
        if invoice[-3:] =='pdf':
            # extract text from invoice
            PDF = extractTextFromPdf(src + invoice)
        else:
            continue
        # Extract invoicing period and total money earned
        period, earnings = extract_total_and_date(PDF)
        # Rename file
        # Tally up earnings from each file
        total += format_earnings(earnings)
    print(f'Total money earned = {total}')

main(all_files)
