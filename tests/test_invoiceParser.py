from unittest import TestCase, main
import extractor.invoiceParser as invPar

class TestInvoiceParser(TestCase):

    def setUp(self):
        print("Setting up")
        self.wdir = "/Users/deniskusic/Documents/Personal/Deliveroo/testing-dir/"
        
    
    def testExtractTextFromPdf(self):
        good_file = self.wdir + "file1.pdf"
        bogus_file = "InexistentFile.pdf"
        good_file = invPar.extractTextFromPdf(good_file)
        self.assertIsInstance(good_file,str)
        self.assertRaises(ValueError,invPar.extractTextFromPdf,bogus_file)


    def testExtractPattern(self):
        pass

    def testFormatEarnedMoney(self):
        good_cases = [
            "Total: £134.00",
            "Tips: £20",
            "Adjustments: £1.00",
            "Deductions: £-4.19",
            "£24.56"
        ]
        exp_cases = [
            134.00, 
            20.00, 
            1.00,
            -4.19, 
            24.56
        ]
        for case,expected in zip(good_cases,exp_cases):
            outcome = invPar.format_earned_money(case)
            self.assertIsInstance(outcome,float)
            self.assertAlmostEqual(expected, outcome, places = 4)
    

    def testIsNewInvoiceType(self):
        pattern_for_old = "Payment for Services Rendered"
        any_string = "Any string"
        self.assertTrue(invPar.is_new_invoice_type(any_string))
        self.assertFalse(invPar.is_new_invoice_type(pattern_for_old))
        

    def testExtractTotalFee(self):
        # input files
        wdir = "/Users/deniskusic/Documents/Personal/Deliveroo/testing-dir/"
        expected_fees = (250.64, 164.44, 58.60, 107.58,41.53,)
        files = {}
        file_template_name = "file"
        for num, exp_fee in enumerate(expected_fees,1):
            filename = file_template_name + str(num) + ".pdf"
            files[filename] = exp_fee

        for file in files:
            print(f"Testing file {wdir + file}")
            fee = invPar.extractTotalFee(wdir + file)
            print(f"Completed and extracted {fee}")
            self.assertAlmostEqual(fee, files[file],places = 4)
            

    def testRenameInvoice(self):
        pass 

if __name__ == '__main__':
    main()