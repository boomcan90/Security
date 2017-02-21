#!/usr/bin/python3
# Name: Arjun Singh Brar
# ID: 1001189

# Arjun Singh Brar
# 1001189

import hashlib
from timeit import Timer
import itertools
import random

def main():
	input_file = 'hash5.txt'
	output_file = 'hash5_out.txt'
	dict_file = 'words5.txt'
	global hashed_stuff
	global decrypted_text
	
	hash_in = open(input_file)
	hashed_stuff = {bytes.fromhex(x) for x in hash_in.read().split("\n") if x}
	hash_in.close()

	words_full = list_builder()
	decrypted_text = []
	 
	for word in words_full:
		word = bytes(word)
		h = hashlib.md5(word).digest()
		if h in hashed_stuff:
			print(word)
			decrypted_text.append(word)
			hashed_stuff.remove(h)
			if len(hashed_stuff) == 0:
				break

	output = open(output_file, "wb")
	output.write(b"\n".join(decrypted_text))
	output.close()

def salt():
	output_file = 'hash5_out.txt'
	with open(output_file, "r") as f:
		passwords = f.read().splitlines()

	new_pass = {}
	for p in passwords:
		salt = random.choice(list(base_word))
		new_pass_append = str(p) + chr(salt)
		h = hashlib.md5(new_pass_append.encode()).hexdigest()
		new_pass[new_pass_append] = h

	f1 = open("pass6.txt", "w")
	f2 = open("salt6.txt", "w")

	for p in new_pass.keys():
		f1.write(p+"\n")
		f2.write(new_pass[p]+"\n")

	f1.close()
	f2.close()


def list_builder():
	global base_word
	# slowert base_word=b'qwertyuiopasdfghjklzxcvbnm1234567890"
	# faster base_word=b"abcdefghijklmnopqrstuvwxyz1234567890"
	base_word=b"etapoinsrhldcumfpgwybvkxjqz1234567890"
	return_set = itertools.product(base_word, repeat=5)
	print(return_set)
	return return_set

if __name__ == "__main__":
	t = Timer(lambda: main())
	print("Time taken: {}".format(t.timeit(number=1)))
	salt()