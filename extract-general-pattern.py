
import sys
sys.path.append('/Users/deniskusic/miniconda3/lib/python3.8/site-packages')
import pdfplumber as pdfP
import os
from fnmatch import fnmatch

src ='/Users/deniskusic/Documents/Personal/Deliveroo/Invoices/Raw-invoices-for-processing/'
filename = 'invoice_e6dcbc69_6701_48a9_a943_42d92b20e9fb_74_1643110735.pdf'


def extractTextFromPdf(filename,page_num = 0):
    """
    Takes filename and returns the text in that file.
    Filename is of type str, representing the absolute path to file, which is a pdf.
    Returns the entire text from the pdf file; type string
    page_num of type int, represents the page number of the file to be parsed.
    """
    with pdfP.open(filename) as pdf:
        page = pdf.pages[page_num]
        text = page.extract_text()
    return text

def extract_total_and_date(PDFtext, indx_total=-2,indx_date=4):
    """
    Extracts the total money earned and invoicing period from PDFtext.
    Return type(tuple)
    PDFtext: type(str)
    Tuple contains two values both of type str, total money and invoicing period.
    """
    PDFtext_list = PDFtext.split('\n')
    print(PDFtext_list)
    filtered = fnmatch.filter(PDFtext_list,'Total:*****')
    print(filtered)
PDF = extractTextFromPdf(src+filename)
patern = 'Total*'
patern2 = 'Invoice period*'# Note however the new invoices contain this word
patern3 = 'Tips*'
PDF_list = PDF.split('\n')
for line in PDF_list:
    if fnmatch(line,patern) or fnmatch(line,patern2) or fnmatch(line,patern3):
        print(line)
        
# This WORKS =) and is perhaps better than using specific index
