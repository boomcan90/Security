#!/usr/bin/env python3
# SUTD 50.020 Security Lab 1
# Simple file read in/out
# Quyen, 2014

# Import libraries
import sys
import argparse

def doStuff(filein,fileout):
    # open file handles to both files
    fin  = open(filein)       # by default, read mode
    fout = open(fileout,'w')  # write mode
    c    = fin.read()         # read in file into c

    # now put your code: convert every second character to upper case

    # and write to fileout


# our main function
if __name__=="__main__":
    # set up the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='filein',help='input file')
    parser.add_argument('-o', dest='fileout', help='output file')

    # parse our arguments
    args = parser.parse_args()
    filein=args.filein
    fileout=args.fileout

    doStuff(filein,fileout)

    # all done


