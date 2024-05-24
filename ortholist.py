
import json

with open('diseasy.json') as fp:
	d = json.load(fp)

for record in d:
	print(record['gene'], end='\t')
	orth = []
	for o in record['d.rerio']: orth.append(o['gene'])
	print('\t'.join(orth))
