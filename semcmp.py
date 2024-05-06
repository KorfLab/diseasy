import argparse
import glob
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
parser.add_argument('file')
parser.add_argument('dir')
parser.add_argument('data', help='[words|lines]')
arg = parser.parse_args()

a = read_file(arg.file, arg.data)
for file in glob.glob(f'{arg.dir}/*'):
	b = read_file(file, arg.data)
	d = compare_meaning(a, b)
	print(arg.file, file, d)

