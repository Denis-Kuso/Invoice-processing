import pdfplumber as pdfP
import os
from collections import namedtuple


def extractTextFromPdf(filename:str)->str:
    """
    Takes filename and returns the text in that file.
    Filename is of type str, representing the absolute path to file, which is a pdf.
    Returns the entire text from the pdf file; type string
    """
    text = ''
    try:
        with pdfP.open(filename) as pdf:
            for page in pdf.pages:
                text += page.extract_text()
    except FileNotFoundError:
        raise ValueError(f"File:{filename} does not exist")
    return text

def getProperSearchPattern(new_invoice:bool, phrase:str)->str:
    invoice_keywords = namedtuple("invoice_keywords",("old","new"))
    fees = invoice_keywords("Total","Total fee payable")
    invoice_period = invoice_keywords("Payment for services rendered","Invoice period")
    phrases = {
        "fees":fees,
        "invoice_period":invoice_period
    }
    if new_invoice:
        return phrases[phrase].new
    else:
        return phrases[phrase].old
print(getProperSearchPattern(False, "invoice_period"))

def extractPattern(PDFtext:str, pattern:str)->str:
    """
    Extracts specified pattern from PDFtext
    """
    # patterns = {
    #     "Total fees": "Total fee payable",
    #     "Total":"Total",
    #     "Tips": "Tips",
    #     "Bonus": "Total Adjustments",
    #     "Period": "Invoice period"
    # }
    is_new = is_new_invoice_type(PDFtext)
    key_phrase = getProperSearchPattern(is_new, pattern)
    PDFtext_list = PDFtext.split('\n')
    total = ""
    # try:
    #     search_pattern = patterns[pattern].lower()
    # except KeyError:
    #     print(f"Sorry! Only available to extract {patterns.keys()}")
    #     return None

    for entry in PDFtext_list:
        #print(f'Checking if {key_phrase.lower()} matches {entry.lower()}')
        if key_phrase.lower() in entry.lower():
            total += entry
    return total


def format_earned_money(earned_money:str)->float:
    """
    
    """
    currency = '£'
    formated_earned_money = 0.0
    start_indx = 0
    for num, char in enumerate(earned_money):
        if char == currency:
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


def extractTotalFee(invoice_file)->float:
    """
    Extracts total money earned from PDFtext.
    """

    PDFtext = extractTextFromPdf(invoice_file)
    #new_invoice_type = is_new_invoice_type(PDFtext)
    #if new_invoice_type:
        #pattern = "Total fees"
    #else:
        #pattern = "Total"
    pattern = "fees"
    extracted_fee = extractPattern(PDFtext, pattern)
    total_fee = format_earned_money(extracted_fee)
    return total_fee


def extractInvoicingPeriod(PDFtext):
    pass


def bulkExtract(folder):
    """
    
    """
    pass


def renameInvoice():
    pass
print(extractPattern("Some random text,\n Total £164.44","fees"))