import sys
sys.path.append('/Users/deniskusic/miniconda3/lib/python3.8/site-packages')
import pdfplumber as pdfP
import os
from datetime import datetime

# if downloading online pdf
##import requests
##def download_file(url):
##    local_filename = url.split('/')[-1]
##
##    with requests.get(url) as r:
##        with open(local_filename, 'wb') as f:
##            f.write(r.content)
##    return local_filename

pathname1 = '/Users/deniskusic/Documents/Personal/Deliveroo/invocies/'
filename1 = '2020-12-04_06.pdf'

def extractTextFromPdf(filename,page_num = 0):
    """Takes filename and returns the text in that file as string
Assumes filename is a string, absolute path to file, which is a pdf.
returns entire text in the pdf; type string"""
    # TODO improve specification
    with pdfP.open(filename) as pdf:
        page = pdf.pages[page_num]
        text = page.extract_text()
    return text

#text_from_invoice = extractTextFromPdf(pathname1 + filename1)
#print(text_from_invoice)

# TODO - extract total from invoice
# TODO - extract date of service provided
def extract_total_and_date(PDFtext):
    total = -2
    date = 4
    PDFtext_list = PDFtext.split('\n')
    return (PDFtext_list[date],PDFtext_list[total])
#print(extract_total_and_date(text_from_invoice))

total = 0
src = pathname1 + 'invocies1/'
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

# Get total for tax relevant tax year
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
    
    
# TODO
# Rename files--- to what format?
# format to yyyy-mm-dd
# Tally up earnings up to 5th april



# use this link for further manipulation https://www.youtube.com/watch?v=syEfR1QIGcY


