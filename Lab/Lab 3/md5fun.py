#!/usr/bin/python3
# Name: Arjun Singh Brar
# ID: 1001189

from pathlib import Path
import hashlib
from timeit import Timer
import itertools


def main(argv):
	# initializing variables
	input_file = 'hash5.txt'
	output_file = 'hash5_out.txt'
	dict_file = 'words5.txt'



	output = open(output_file, "w")
	hash_in = open(input_file)
	hashed_stuff = hash_in.read().split("\n")
	words = open(dict_file).read().split("\n")
	words_5 = []

	for word in words:
		if len(word) == 5: 
			words_5.append(word)

	words_5_full = list_builder(words_5)
	decrypted_text = []
	for hash in hashed_stuff:
		for word in words_5_full:
			h = hashlib.md5(word.encode('utf-8')).hexdigest()
			if hash == h:
				decrypted_text.extend(word)

	output_file.write("/n".join(decrypted_text))

def list_builder(words_list):
	return_list = []
	for word in words_list:
		return_list.extend(["".join(perm) for perm in itertools.permutations(word)])
	return return_list

if __name__ == "__main__":
	# main(sys.argv[1:])
	t = Timer(main(sys.argv[1:]))
	print("Time taken: {}".format(t.timeit(number=1)))
	