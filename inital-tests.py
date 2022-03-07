import os
import invoiceParser as inpar
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
    print(f"Filename: {fajl}")
    tekst_fajl = inpar.extractTextFromPdf(src1+fajl)
    is_new = inpar.is_new_invoice_type(tekst_fajl)
    novac = inpar.extractTotalFee(tekst_fajl,is_new)
    print(f"Money earned: £{novac}")
    print("-"*10)