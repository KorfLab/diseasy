import argparse
import math
import sys

from sentence_transformers import SentenceTransformer
from scipy.spatial import distance


def read_file(filename, method):
	data = {}
	if method == 'words':
		with open(filename) as fp:
			for line in fp:
				words = line.rstrip().split()
				for word in words:
					data[word] = True
	elif method == 'lines':
		with open(filename) as fp:
			for line in fp:
				phrase = line.rstrip()
				data[phrase] = True
	else: sys.exit('wtf')
	
	
	return ' '.join(data.keys())

def compare_meaning(text1, text2):
	model = SentenceTransformer('distilbert-base-nli-mean-tokens')
	e1 = model.encode(text1)
	e2 = model.encode(text2)
	return distance.cosine(e1, e2)

## Command Line Interface ##
parser = argparse.ArgumentParser('text comparison program')
parser.add_argument('file1')
parser.add_argument('file2')
parser.add_argument('data', help='[words|lines]')
arg = parser.parse_args()

a = read_file(arg.file1, arg.data)
b = read_file(arg.file2, arg.data)
d = compare_meaning(a, b)
print(d)

