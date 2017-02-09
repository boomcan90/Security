#!/usr/bin/python3
# -*- coding: utf-8 -*-
# DA 2017

"""
Lab2: Breaking Ciphers

Pwntool client for python3

Install: sudo pip3 install git+https://github.com/arthaud/python3-pwntools.git

Documentation: https://python3-pwntools.readthedocs.io/en/latest/
"""
import string
import math
from pwn import remote
from collections import Counter

# takes any text and does freq analysis for it
# returns list of most common letters, sorted in desc order
def FrequencyAnalysis(text):
    # get freq distribution 
    MOST_COMMON = Counter(text).most_common()
    freq_dist = []
    for i in MOST_COMMON:
        freq_dist.append(i[0])
    # print("FREQ DIST", len(freq_dist), freq_dist)
    return freq_dist


# takes a list, flips position of a and b
def Flip(LIST, a, b):
    if a not in LIST:
        LIST.append(a)
    elif b not in LIST:
        LIST.append(b)
    indexA = LIST.index(a)
    indexB = LIST.index(b)
    LIST[indexA] = b
    LIST[indexB] = a
    return LIST

# cipher- encrypted text
# fd - freq_dist of sherlock.txt
# cd - cipher_dist of encrypted text
def Decrypt(cipher, fd, cd):
    # now, based on trial and error, and observations, 
    # modify FREQ to get deciphered text
    # TEST CASE = ohye cboh a trfe tiene uad a sean lrttle mrnl uio uad lokes
    fd = [' ', 'e', 't', 'a', 'o', 'h', 'r', 'n', 'd', 'i', 's', 'l', 'w', '\n',
        'g', ',', 'u', 'c', 'm', 'y', 'f', 'p', '.', 'b', 'k', 'v', '"', '-',
        "'", 'j', 'q', '?', '\t', 'x', '!', 'z', '1', ';', '0', ':', '*', '8',
        '3', '/', ')', '(', '2', '4', '7', '5', '6', '9', '@', '_', ']', '[',
        '>', '<', '$', '%', '#']
    decrypted = ""
    for c in cipher:
        decrypted += fd[cd.index(c)]
    return(decrypted)

def encrypt(key, plaintext):
    """Encrypt the string and return the ciphertext"""
    return ''.join(key[l] for l in plaintext)

if __name__ == "__main__":

    # NOTE: UPPERCASE names for constants is a (nice) Python convention
    URL = 'scy-phy.net'
    PORT = 1337

    # NOTE: conn is the connection handler
    conn = remote(URL, PORT)
    # NOTE: try to use sendline()
    # conn.sendline("GET /\r\n\r\n")

    # Welcome message
    print("received message: {}".format(conn.recv()))
    conn.clean()

    # Challenge 1
    conn.sendline("1\n")
    print("received: {}".format(conn.recv()))

    # Find out that Challenge1 data is 7408 bytes, so use recvn
    # Getting Challenge1 data
    cipher = conn.recvn(7408)
    print(len(cipher))
    # print(cipher) 

    cipher_new = ""
    for c in cipher:
        cipher_new += chr(c)

    # by default, read mode
    fin  = open('sherlock.txt')
    # read in file into cipher       
    fileFreq = fin.read()
    fileFreq = fileFreq.lower()

    FREQ = FrequencyAnalysis(fileFreq)
    # print("FREQ_DIST", len(FREQ), FREQ)


    CIPHERFREQ = FrequencyAnalysis(cipher_new)
    # print("CIPHER_DIST", len(CIPHERFREQ), CIPHERFREQ)
    # thanks, Counter. You have failed me. 
    CIPHERFREQ = ['/', '5', 'I', '>', 'W', 'O', 'S', 'U', 'X', '{', 'o', 'u', '!', '\x0c', 'Y', 'T', 'd', 'E', '3', '\n', '\r', 'R', 'y', 'N', '*', 'C', '$', '=', 'f', ' ', 'm', 'h', '}']
    

    f = open("dhanyaout.txt", "w")
    f.write(Decrypt(cipher_new, FREQ, CIPHERFREQ))
    f.close()
    print(Decrypt(cipher_new, FREQ, CIPHERFREQ)[:7411])
    
    conn.clean()
    conn.send(Decrypt(cipher_new, FREQ, CIPHERFREQ)[:7411])
    print(conn.recv())
    conn.clean()
    # conn.close()










