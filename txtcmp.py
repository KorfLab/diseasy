import argparse
import glob
import math
import sys

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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

def compare_text(text1, text2):
	vectorizer = TfidfVectorizer()
	vectors = vectorizer.fit_transform([text1, text2])
	similarity = cosine_similarity(vectors)
	distance = 1 - similarity[0][1]
	if math.isclose(distance, 0, abs_tol=1e-6): return 0
	return distance

## Command Line Interface ##
parser = argparse.ArgumentParser('text comparison program')
parser.add_argument('file')
parser.add_argument('dir')
parser.add_argument('data', help='[words|lines]')
arg = parser.parse_args()

a = read_file(arg.file, arg.data)
for file in glob.glob(f'{arg.dir}/*'):
	b = read_file(arg.file, arg.data)
	d = compare_text(a, b)
	print(arg.file, file, d)
