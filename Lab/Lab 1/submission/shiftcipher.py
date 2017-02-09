#!/usr/bin/python3
# Name: Arjun Singh Brar
# ID: 1001189

import sys, getopt, string
from pathlib import Path

MAX_KEY_SIZE = 100

def main(argv):
    # initializing variables
    input_file = ''
    output_file = ''

    # parsing input arguments
    try:
        opts, args = getopt.getopt(argv, "hi:o:k:m:", ["ifile=", "ofile=", "key=", "mode="])
    except getopt.GetoptError:
        print('shiftcipher.py -i <inputfile> -o <outputfile> -k <key>')
        sys.exit(2)

    if len(opts) < 3:
       print('Invalid usage. Use: shiftcipher.py -i <inputfile> -o <outputfile> -k <key>')
       sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('shiftcipher.py -i <inputfile> -o <outputfile> -k <key>')
        elif opt in ('-i', '--ifile'):
            input_file = arg
        elif opt in ('-o', '--ofile'):
            output_file = arg
        elif opt in ('-k', '--key'):
            try:
                key = int(arg)
            except ValueError: 
                print("Invalid Usage. Key should be integer.")
                sys.exit(2)
        elif opt in ('-m', '--mode'):
            mode = arg

    # input validation
    if key > MAX_KEY_SIZE:
        print('Invalid usage. Max key size is 100.')
        sys.exit(2)

    if mode.lower() not in "e d".split():
        print("Invalid usage. Mode should be one of the following: e E d D")
        sys.exit(2)


    input_file_path = Path(input_file)
    if not input_file_path.is_file():
        print("The input file does not exist.")
        sys.exit(2)


    if mode.lower() in "d D".split():
        key = -key

    # reading the file
    f = open(input_file, mode='r', newline="\n")
    out_file = open(output_file, mode='w', newline="\n")
    for line in f:
        cipher_text = ''
        for symbol in line:
            num = string.printable.index(symbol)
            num += key
            num = num%100
            cipher_text+=string.printable[num]
        out_file.write(cipher_text)
    out_file.close()
    f.close()

if __name__ == "__main__":
    main(sys.argv[1:])

