"""
Long description of what this script does.

Contains the following functions:
    * function1 - bla bla bla (TO ADD)
    * main - main function of the script, extracts fees earned from every file in the folder provided
      and adds them up, printing total money earned from the invoice files in folder specified. It flag -p provided, it will 
      print out fees and filename from each invoice as well.
"""
import argparse
import os
import sys
import invoiceParser as invPar


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        'source_dir',
        type=str,
        help="Folder containing Deliveroo invoice files. Can be relative to script location or absolute path."
    )
    parser.add_argument(
        '-p',
        '--print',
        action='store_true',
        help='Print progress to screen, default = False'
    )
    args = parser.parse_args()
    total = 0.0
    try:
        files = os.listdir(args.source_dir)
    except FileNotFoundError:
        print(f"No such file or directory: '{args.source_dir}'")
        sys.exit(1)

    for file in files:
        invoice = args.source_dir + '/' + file
        fee = invPar.extractTotalFee(invoice)
        total += fee
        if args.print:
            print(f"Extracting from: {invoice}")
            print(f" extracted £{fee}, total = £{total}")
    print(f"Total extracted: £{total}")


if __name__ == '__main__':
    main()