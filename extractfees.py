"""
Long description of what this script does.

Contains the following functions:
    * function1 - bla bla bla
    * main - main function of the script, extracts fees earned from every file in the folder provided
      and adds them up printing total money earned from the invoice files in folder specified.
"""
import argparse
import os
import sys
import invoiceParser as invPar


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        'src',
        type=str,
        help="Folder containing Deliveroo invoice files."
    )
    parser.add_argument(
        '-p',
        '--print',
        action='store_true',
        help='Print progress to screen, default = False'
    )
    args = parser.parse_args()
    total = 0.0
    files = os.listdir(args.src)
    for file in files:
        invoice = args.src + file
        fee = invPar.extractTotalFee(invoice)
        total += fee
        if args.prints:
            print(f"Extracting from: {invoice}")
            print(f"* extracted {fee}, total = {total}")
    print(f"Total extracted: {total}")

if __name__ == '__main__':
    main()