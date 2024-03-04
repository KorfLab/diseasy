import json

# tsim1, tsim2
# https://spotintelligence.com/2022/12/19/text-similarity-python
"""
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer



def tsim1(text1, text2):
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
"""

###############################################################################

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def tsim2(text1, text2):
	vectorizer = TfidfVectorizer()
	vectors = vectorizer.fit_transform([text1, text2])
	similarity = cosine_similarity(vectors)
	return similarity[0][1]


# tsim3, tsim4
# https://shorturl.at/ehwK8
from sentence_transformers import SentenceTransformer
from scipy.spatial import distance

def tsim3(text1, text2):
	model = SentenceTransformer('distilbert-base-nli-mean-tokens')
	e1 = model.encode(text1)
	e2 = model.encode(text2)
	return 1- distance.cosine(e1, e2)

###############################################################################

import tensorflow_hub as hub

def tsim4(text1, text2):
	embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
	te = embed([text1, text2])
	return 1 - distance.cosine(te[0], te[1])

###############################################################################

## Main ##

cmp = {
	'sklearntext': tsim2,
	'transformer': tsim3,
	'tensorflow':  tsim4,
}

with open('diseasy.json') as fp:
	d = json.load(fp)

for i in range(len(d)):
	gene1 = d[i]['gene']
	dtext1 = ' '.join(d[i]['diseases'])
	for j in range(i, len(d)):
		gene2 = d[j]['gene']
		dtext2 = ' '.join(d[j]['diseases'])
		for method, func in cmp.items():
			print(gene1, gene2, method, func(dtext1, dtext2))
	break

