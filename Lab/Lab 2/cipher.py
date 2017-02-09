import os
from collections import Counter
import binascii

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





f = open("encrypted.txt", 'rb')
encrypted = f.read()
encrypted = binascii.b2a_base64(encrypted)
print(Counter(str(encrypted)))
key = Counter(str(encrypted)).most_common()
print(len(key))

with open("sherlock.txt") as f: 
    test_data = f.read()
    test_data = test_data.lower()
    test_data = bytearray(test_data, "ascii")

ETAOIN2 = Counter(str(test_data)).most_common()
print(ETAOIN2)
print(len(ETAOIN2))

key_dic = {}

# for i in range(len(key)):
#     key_dic[key[i][0]] = ETAOIN2[i].lower()

# print(key_dic)

# print(encrypt(key_dic, encrypted))