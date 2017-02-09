#!/usr/bin/python3
# Name: Arjun Singh Brar
# ID: 1001189

from pathlib import Path
import hashlib
from timeit import Timer
import itertools


def main():
	# initializing variables
	input_file = 'hash5.txt'
	output_file = 'hash5_out.txt'
	dict_file = 'words5.txt'



	output = open(output_file, "w")
	hash_in = open(input_file)
	hashed_stuff = hash_in.read().split("\n")
	words = open(dict_file).read().splitlines()
	words_5 = []

	for word in words:
		if len(word) == 5: 
			words_5.append(word)

	words_full = list_builder()
	decrypted_text = []
	# for hash in hashed_stuff:
	# 	for word in words_5_full:
	# 		h = hashlib.md5(word.encode('utf-8')).hexdigest()
	# 		if hash == h and word not in decrypted_text:
	# 			decrypted_text.extend(word)

	for word in words_5:
		h = hashlib.md5(word.encode()).hexdigest()
		if h in hashed_stuff and word not in decrypted_text:
			print(word)
			decrypted_text.append(word)
			del hashed_stuff[hashed_stuff.index(h)]

	for word in words_full:
		h = hashlib.md5(word.encode()).hexdigest()
		if h in hashed_stuff and word not in decrypted_text:
			print(word)
			decrypted_text.append(word)
			del hashed_stuff[hashed_stuff.index(h)]
			if len(hashed_stuff) == 0:
				break

	print(decrypted_text)
	output.write("\n".join(decrypted_text))

def list_builder():
	return_list = []
	word="1234567890qwertyuiopasdfghjklzxcvbnmn"	
	return_list.extend(["".join(perm) for perm in itertools.product(word, repeat=5)])
	return return_list

if __name__ == "__main__":
	# main(sys.argv[1:])
	t = Timer(lambda: main())
	print("Time taken: {}".format(t.timeit(number=1)))
	