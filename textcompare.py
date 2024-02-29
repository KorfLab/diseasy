import json
import sys

# Code from: https://spotintelligence.com/2022/12/19/text-similarity-python/


import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import transformers

# Load the BERT model
model = transformers.BertModel.from_pretrained('bert-base-uncased')

def bsim(text1, text2):
	# Tokenize and encode the texts
	encoding1 = model.encode(text1, max_length=512)
	encoding2 = model.encode(text2, max_length=512)

	# Calculate the cosine similarity between the embeddings
	similarity = numpy.dot(encoding1, encoding2) / (numpy.linalg.norm(encoding1) * numpy.linalg.norm(encoding2))
	
	return similarity


def tsim(text1, text2):
	# Convert the texts into TF-IDF vectors
	vectorizer = TfidfVectorizer()
	vectors = vectorizer.fit_transform([text1, text2])

	# Calculate the cosine similarity between the vectors
	similarity = cosine_similarity(vectors)
	
	return similarity



def text_similarity(text1, text2):
	# Tokenize and lemmatize the texts
	tokens1 = word_tokenize(text1)
	tokens2 = word_tokenize(text2)
	lemmatizer = WordNetLemmatizer()
	tokens1 = [lemmatizer.lemmatize(token) for token in tokens1]
	tokens2 = [lemmatizer.lemmatize(token) for token in tokens2]

	# Remove stopwords
	stop_words = stopwords.words('english')
	tokens1 = [token for token in tokens1 if token not in stop_words]
	tokens2 = [token for token in tokens2 if token not in stop_words]

	# Create the TF-IDF vectors
	vectorizer = TfidfVectorizer()
	vector1 = vectorizer.fit_transform(tokens1)
	vector2 = vectorizer.transform(tokens2)

	# Calculate the cosine similarity
	similarity = cosine_similarity(vector1, vector2)

	return similarity

with open('diseasy.json') as fp:
	d = json.load(fp)

for i in range(len(d)):
	dtext1 = ' '.join(d[i]['diseases'])
	for j in range(i, len(d)):
		dtext2 = ' '.join(d[j]['diseases'])
		#print(i, j, text_similarity(dtext1, dtext2))
		print(i, j, bsim(dtext1, dtext2))
	
"""
	
	ptexts = []
	for gene in d['d.rerio']:
		ptexts.append(' '.join(gene['phenotypes']))
	ptext = ' '.join(ptexts)
	d = text_similarity(dtext, ptext)
	print(d)
"""	