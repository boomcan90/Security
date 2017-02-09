#!/usr/bin/python3
# -*- coding: utf-8 -*-
# DA 2017

"""
Lab2: Breaking Ciphers
"""
import string
import math
from pwn import remote
from collections import Counter
import os.path
import operator

# takes analysis, makes list of 
# common chars in descending order
def FreqAnalysis(dictFreq):
    tupleFreq = sorted(dictFreq.items(), key=operator.itemgetter(1))
    tupleFreq.reverse()
    listFreq = [k[0] for k in tupleFreq]
    return listFreq

# cipher- encrypted text
# takes cipher, make dict of analysis
def CalculateFreq(cipher):
    dictF = {}
    for c in cipher:
        if c in dictF:
            dictF[c] += 1
        else:
            dictF[c] = 1

    return dictF

# cipher- encrypted text
# fd - freq_dist of sherlock.txt
# cd - cipher_dist of encrypted text
def Decrypt(cipher, fd, cd):
    decrypted = ""
    for c in cipher:
        decrypted += fd[cd.index(c)]

    print(decrypted)
    return(decrypted)

if __name__ == "__main__":

    URL = 'scy-phy.net'
    PORT = 1337

    conn = remote(URL, PORT)
    if not (os.path.exists('cipher.txt')):
        print("cipher.txt being created now")
        # Welcome message
        print("received message: {}".format(conn.recv()))
        conn.clean()

        # Challenge 1
        conn.sendline("1\n")
        conn.recv()

        # Find out that Challenge1 data is 7408 bytes, so use recvn
        # Getting Challenge1 data
        cipher = conn.recvn(7408)
        print(len(cipher))

        # Write to file
        with open('cipher.txt', 'wb') as foutC:
            foutC.write(cipher)
            foutC.close()

    fin_cipher = open('cipher.txt', 'rb')
    cipherBytes = fin_cipher.read()

    fin_sherlock = open('sherlock.txt')
    fSherlock = fin_sherlock.read()
    fSherlock = fSherlock.lower()


    fCipher = ""
    for c in cipherBytes:
        fCipher += chr(c)

    # CIPHERFREQ = FreqAnalysis(CalculateFreq(fCipher))
    # print(CIPHERFREQ)

    CIPHERFREQ = ['/', '5', 'I', '>', 'W', 'O', 'S', 'U', 'X', '{',
                  'o', 'u', '!', '\x0c', 'Y', 'T', 'd', 'E', '3',
                '\n', '\r', 'R', 'y', 'N', '*', 'C', '$', '=', 'f', ' ', 'm', 'h', '}']


    FREQ =  [' ', 'e', 't', 'a', 'o', 'h', 'r', 'n', 'd', 'i', 's', 'l', 'w', '\n', 'g', ',', 'u', 'c', 'm', 'y', 'f', 'p', '.', 'b', 'k', 'v', '"', '-', "'", 'j', 'q', '?', '\t', 'x', '!', 'z', '1', ';', '0', ':', '*', '8', '3', '/', ')', '(', '2', '4', '7', '5', '6', '9', '@', '_', ']', '[', '>', '<', '$', '%', '#']


    print("\n------------------------------------------------\n")

    # CIPHERFREQ = FrequencyAnalysis(cipher_new)
    # print("CIPHER_DIST", len(CIPHERFREQ), CIPHERFREQ)

    ans = Decrypt(fCipher, FREQ, CIPHERFREQ)

    with open("dhanya-out", "w") as f:
        f.write(ans)
        f.close()
    # Welcome message
    conn.recv()
    conn.clean()

    # Challenge 1
    conn.sendline("1")
    conn.recv()

    # Find out that Challenge1 data is 7408 bytes, so use recvn
    # Getting Challenge1 data
    cipher = conn.recvn(7408)
    conn.clean()
    conn.send(ans)   
    print(conn.recv())
    conn.clean()
    conn.close()

