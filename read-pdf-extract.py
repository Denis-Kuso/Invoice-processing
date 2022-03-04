import sys
sys.path.append('/Users/deniskusic/miniconda3/lib/python3.8/site-packages')
import pdfplumber as pdfP
import os
# use this link for further manipulation https://www.youtube.com/watch?v=syEfR1QIGcY

# File information
wd = os.getcwd()
src = '/Users/deniskusic/Documents/Personal/Deliveroo/testing-dir/'
dst = '/Users/deniskusic/Documents/Personal/Deliveroo/Invoices/Processed-invoices/'
all_files = os.listdir(src)
list_of_failed_files = []


def extractTextFromPdf(filename):
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
# textic = extractTextFromPdf(src + all_files[1])
# print(textic)
# textic1 = extractTextFromPdf(src + all_files[0])
# print(textic1)

def extractInvoicingPeriod(PDFtext):
    pass


def extractPattern(PDFtext, pattern = "Total fees"):
    patterns = {
        "Total fees": "Total fee payable",
        "Total":"Total",
        "Tips": "Tips",
        "Bonus": "Total Adjustments",
        "Period": "Invoice period"

    }# To solve different invoices add another key, i.e old total? or have values as tuples?
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

src1 = "/Users/deniskusic/Documents/Personal/Deliveroo/testing-dir/"
fajl = "invoice_e6dcbc69_6701_48a9_a943_42d92b20e9fb_79_1645525852.pdf"
fajl2 = "old-invoice.pdf"
fajls = os.listdir("/Users/deniskusic/Documents/Personal/Deliveroo/testing-dir/")
try:
    fajls.remove('.DS_store')
except ValueError:
    pass
print(fajls)
for fajl in fajls:
    print('extracting teksts')
    print(f"Filename: {fajl}")
    tekst_fajl = extractTextFromPdf(src1+fajl)
    is_new = is_new_invoice_type(tekst_fajl)
    print(f"Extracting money")
    novac = extractTotalFee(tekst_fajl,is_new)
    print(f"Money earned: £{novac}")
    print("-"*10)

# Test some other pdfs

print()

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

#main(all_files)
