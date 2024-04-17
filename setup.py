import json

with open('diseasy.json') as fp:
	d = json.load(fp)

genes = []
for i in range(len(d)):
	gene = d[i]['gene']
	genes.append(gene)

print('all:\\')
for gene in genes:
	print(f'\tbuild/{gene}.cmp\\')
print()


for i, gene in enumerate(genes):
	target = i+1
	print(f'build/{gene}.cmp:')
	print(f'\tpython3 txtcmp.py {target} > build/{gene}.cmp')
