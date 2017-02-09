#!/usr/bin/python3
# -*- coding: utf-8 -*-
# DA 2017

"""
Lab2: Breaking Ciphers

Pwntool client for python3

Install: sudo pip3 install git+https://github.com/arthaud/python3-pwntools.git

Documentation: https://python3-pwntools.readthedocs.io/en/latest/
"""

from pwn import remote
import random
from collections import Counter
import binascii

def counter(l):
    return[(l.count(x), x) for x in set(l)]


def encrypt(key, plaintext):
    """Encrypt the string and return the ciphertext"""
    return ''.join(key[l] for l in plaintext)

def decrypt(key, ciphertext):
    """Decrypt the string and return the plaintext"""
    flipped = {v: k for k, v in key.items()}
    return ''.join(key[l] for l in ciphertext)

def generate_key():
    """Generate an key for our cipher"""
    shuffled = sorted(CHARS, key=lambda k: random.random())
    return dict(zip(CHARS, shuffled))

def show_result(key, encrypted):
    """Generate a resulting cipher with elements shown"""

    decrypted = decrypt(key, encrypted)

    print ('Key: %s' % key)
    print ('Decrytped: %s' % decrypted)


if __name__ == "__main__":

    # NOTE: UPPERCASE names for constants is a (nice) Python convention
    URL = 'scy-phy.net'
    PORT = 1337

    # NOTE: conn is the connection handler
    conn = remote(URL, PORT)
    # NOTE: try to use sendline()
    # conn.sendline("GET /\r\n\r\n")
    
    print("received message: {}".format(conn.recv()))
    conn.clean()


    conn.sendline("1")
    print("message: {}".format(conn.recv()))

    cipher_text = conn.recvn(7408)
    key = {}
    cipher_text_ascii = ""
    for c in cipher_text:
        cipher_text_ascii += chr(c)

    
    cipher_text_ascii_fd = sorted(counter(cipher_text_ascii), reverse=True)
    cipher_text_ascii_fd_2 = Counter(cipher_text_ascii).most_common()
    with open("sherlock.txt") as f: 
        test_data = f.read()
        test_data = test_data.lower()


    ETAOIN2 = counter(test_data)
    # print(ETAOIN2)
    # print(len(ETAOIN2))

    ETAOIN_items = []
    for i in range(len(ETAOIN2)):
        ETAOIN_items.append(ETAOIN2[i][1])


    # by hit and trial :)
    ETAOIN = [' ', 'e', 't', 'a', 'o', 'h', 'r', 'n', 'd', 'i', 's', 'l', 'w', '\n', 'g', ',', 'u', 'c', 'm', 'y', 'f', 'p', '.', 'b', 'k', 'v', '"', '-', "'", 'j', 'q', '?', '\t', 'x', '!', 'z', '1', ';', '0', ':', '*', '8', '3', '/', ')', '(', '2', '4', '7', '5', '6', '9', '@', '_', ']', '[', '>', '<', '$', '%', '#']


    print (cipher_text_ascii_fd)

    
    ETAOIN_KEY = []

    key = {}
    for i in range(len(cipher_text_ascii_fd)):
        key[cipher_text_ascii_fd[i][1]] = ETAOIN[i]
        ETAOIN_KEY.append(cipher_text_ascii_fd[i][1])

    print(ETAOIN_KEY)
    print(cipher_text_ascii_fd)
    print (cipher_text_ascii_fd_2)

    a = encrypt(key, cipher_text_ascii)
    with open("arjun-out", 'w') as f: 
        f.write(a)
        f.close()

    # print(a)
    conn.clean()
    conn.send(a)
    print(conn.recv())
    conn.clean()

    # keys_list = [key for (key, value) in sorted(Counter(str(cipher_text)).values(), reverse=False)]


    # print(len(sorted(Counter(cipher_text).values(), reverse=True)))
    # new = []
    # for i in sorted(Counter(cipher_text).values(), reverse=True):
    #     new.append(i/sum(Counter(cipher_text).values()))

    # print(new)
    # NOTE: try to use recvuntil() with different delimiters ...
    # DELIMITER = ' '
    # message = r.recvuntil(DELIMITER)
    # NOTE: now try to use recv()
    # message = conn.recv()
    
    conn.close()

    conn = remote(URL, PORT)
    print("received message: {}".format(conn.recv()))
    conn.clean()

    conn.sendline("2")
    print("message: {}".format(conn.recv()))
    otp = conn.recvn(32)

    list_new = []

    for i in otp: 
        list_new.append(i)

    list_new[14] = list_new[14] ^ 0b01 ^ 0b00
    list_new[15] = list_new[15] ^ 0b01 ^ 0b00
    list_new[16] = list_new[16] ^ 0b1000 ^ 0b00
    list_new[17] = list_new[17] ^ 0b1001 ^0b00


    list_new[24] = list_new[24] ^ 0b0100 ^ 0b00
    print("message: {}".format(conn.recv()))
    conn.clean()
    conn.send(bytes(list_new))
    print("message: {}".format(conn.recv()))


    conn.close()