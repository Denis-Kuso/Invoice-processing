import pdfplumber as pdfP
import os
from collections import namedtuple


def extractTextFromPdf(filename:str)->str:
    """Takes a pdf file and extracts text from that file.

    Parameters
    ----------
    filename
        Represents the string representation of the absolute pathname to the PDF file.
    
    Raises
    ------
    ValueError
        If the filename doesn't not exist or is provided as relative pathname.

    Returns
    -------
    str
        String containing text from PDF file
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
    """
    Chooses search pattern dependent on invoice being of new or old type.

    Parameters
    ----------
    new_invoice:
        True if the invoice is the current edition, false otherwise.
        New invoice from 25/01/2022, old invoice guaranteed from 23/09/2020 until new invoice date.

    phrase:
        Accepts phrases 'fees', 'invoice_period' which are named differently in old/new invoices.

    Returns
    -------
        String, representing a keyword to search in text extracted from a PDF file.
    """
    invoice_keywords = namedtuple("invoice_keywords",("old","new"))
    fees = invoice_keywords("Total","Total fee payable")
    invoice_period = invoice_keywords("Payment for services rendered","Invoice period")
    keywords = {
        "fees":fees,
        "invoice_period":invoice_period
    }
    if new_invoice:
        return keywords[phrase].new
    else:
        return keywords[phrase].old


def extractPattern(PDFtext:str, pattern:str)->str:
    """
    Extracts specified pattern from PDFtext.

    Parameters
    ----------
    PDFtext:
        text extracted from Deliveroo invoice (filename.PDF)

    pattern:
        pattern ('Total fees', 'tips') to be extracted from a list of strings, 
        determined by getProperSearchPattern

    Returns
    -------
        String containing the words to extract ('Total fees')
    """
    
    is_new = is_new_invoice_type(PDFtext)
    key_phrase = getProperSearchPattern(is_new, pattern)
    PDFtext_list = PDFtext.split('\n')
    total = ""

    for entry in PDFtext_list:
        if key_phrase.lower() in entry.lower():
            total += entry
    return total


def format_earned_money(earned_money:str)->float:
    """
    Strips everything from earned_money besides the number representing money.

    Parameters
    ----------
    earned_money:
        Money earned/deducted.

    Returns
    -------
    Float representing money earned.
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
    Determines wheter invoice is of new type and returns True if so, False otherwise.

    Parameters
    ----------
    pdf_text:
        Represent text extracted from a Deliveroo invoice file (.pdf). Layout, column names used are
        different between two invoices. Old invoice contains keyphrase 'Payment for services rendered', 
        new invoice states 'Invoice period'. 
    Returns
    -------
        True if invoice is new, false otherwise.
    """
    pattern_for_old_invoice = "Payment for Services Rendered"
    if pattern_for_old_invoice in pdf_text:
        return False
    return True


def extractTotalFee(invoice_file:str)->float:
    """
    Extracts total fee earned from a Deliveroo invoice (pdf file). 

    Parameters
    ----------
    invoice_file:
        absolute path to a Deliveroo invoice

    Returns
    -------
    Float as fee earned. 
    """

    PDFtext = extractTextFromPdf(invoice_file)
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
