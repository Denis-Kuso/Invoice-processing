import sys
import pdfplumber as pdfP
import os


def extractTextFromPdf(filename:str)->str:
    """
    Takes filename and returns the text in that file.
    Filename is of type str, representing the absolute path to file, which is a pdf.
    Returns the entire text from the pdf file; type string
    page_num of type int, represents the page number of the file to be parsed.
    """
    try:
        text = ''
        with pdfP.open(filename) as pdf:
            for page in pdf.pages:
                text += page.extract_text()
    except FileNotFoundError:
        print(f'File: {filename} not found')
        sys.exit(1)
    return text


def extractPattern(PDFtext:list, pattern:str = "Total fees")->str:
    """
    Extracts specified pattern from PDFtext
    """
    patterns = {
        "Total fees": "Total fee payable",
        "Total":"Total",
        "Tips": "Tips",
        "Bonus": "Total Adjustments",
        "Period": "Invoice period"
    }
    PDFtext_list = PDFtext.split('\n')
    total = ""
    try:
        search_pattern = patterns[pattern].lower()
    except KeyError:
        print(f"Sorry! Only available to extract {patterns.keys()}")
        return None

    for entry in PDFtext_list:
        if search_pattern in entry.lower():
            total += entry
    return total

    # # Format total
def format_earned_money(earned_money:str)->float:
    """
    
    """
    formated_earned_money = 0.0
    start_indx = 0
    for num, char in enumerate(earned_money):
        if char == '£':
            start_indx = num + 1
    formated_earned_money = float(earned_money[start_indx:])
    return formated_earned_money
    

def is_new_invoice_type(pdf_text:str)->bool:
    """
    Returns True if new invoice type
    """
    pattern_for_old_invoice = "Payment for Services Rendered"
    if pattern_for_old_invoice in pdf_text:
        return False
    return True


def extractTotalFee(PDFtext, new_invoice_type = True):
    """
    Extracts total money earned from PDFtext.
    """
    if new_invoice_type:
        pattern = "Total fees"
    else:
        pattern = "Total"
    total_fee = extractPattern(PDFtext, pattern)
    total_fee = format_earned_money(total_fee)
    return total_fee


def extractInvoicingPeriod(PDFtext):
    pass


def bulkExtract(folder):
    """
    
    """
    pass


def renameInvoice():
    pass
