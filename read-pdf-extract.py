import sys
sys.path.append('/Users/deniskusic/miniconda3/lib/python3.8/site-packages')
import pdfplumber as pdfP
import os
from datetime import datetime
# use this link for further manipulation https://www.youtube.com/watch?v=syEfR1QIGcY

# File information
wd = os.getcwd()
src = '/Users/deniskusic/Documents/Personal/Deliveroo/Invoices/Raw-invoices-for-processing/'
dst = '/Users/deniskusic/Documents/Personal/Deliveroo/Invoices/Processed-invoices/'
all_files = os.listdir(src)
list_of_failed_files = []

def extractTextFromPdf(filename,page_num = 0):
    """
    Takes filename and returns the text in that file.
    Filename is of type str, representing the absolute path to file, which is a pdf.
    Returns the entire text from the pdf file; type string
    page_num of type int, represents the page number of the file to be parsed.
    """
    try:
        with pdfP.open(filename) as pdf:
            page = pdf.pages[page_num]
            text = page.extract_text()
    except FileNotFoundError:
        print(f'File: {filename} not found')
        sys.exit(1)
    return text

def extract_total_and_date(PDFtext, indx_total=-2,indx_date=4):
    """
    Extracts the total money earned and invoicing period from PDFtext.
    Return type(tuple)
    PDFtext: type(str)
    Tuple contains two values both of type str, total money and invoicing period.
    """
    PDFtext_list = PDFtext.split('\n')
    return (PDFtext_list[indx_total],PDFtext_list[indx_date])

def format_earnings(earnings, start_indx = 6):
    """
    Returns formated earnings stripping
    redundant symbols and words.
    Return type: float
    Keyword arguments:
    start_indx has type int is the index at which the number begins.
    Positional arguments:
    earnings has type string, always of form 'Total:£123.55'
    """
    f_earnings = float(earnings[start_indx:].strip('£'))
    return f_earnings

def main(all_files):
    total = 0.0
    print(f'Searching for invoices in: {src}')
    for invoice in all_files:
        if invoice[-3:] == 'pdf':
            # extract text from invoice
            PDF = extractTextFromPdf(src + invoice)
        else:
            continue
        # Extract invoicing period and total money earned
        earnings, period = extract_total_and_date(PDF)
        # Tally up earnings from each file
        total += format_earnings(earnings)
    print(f'Total money earned = £{total}')

main(all_files)
