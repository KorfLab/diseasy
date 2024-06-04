import glob
import os
import sys

## input

data = {}
for path in glob.glob(f'build/h2z/*'):
	s1 = path.split('/')
	hgene, zf, cmp = s1[2].split('-', maxsplit=2)
	if cmp not in data: data[cmp] = {}
	if hgene not in data[cmp]: data[cmp][hgene] = {}
	with open(path) as fp:
		for line in fp:
			hi, zi, perf = line.split()
			zgene = zi.split('/')[2]
			if zgene not in data[cmp][hgene]: data[cmp][hgene][zgene] = {}
			data[cmp][hgene][zgene] = perf

## output

hgenes = list(data['sem-lines'].keys())
zgenes = list(data['sem-lines']['SLX4'].keys())

for cmp in data:
	with open(f'bigtable.{cmp}.tsv', 'w') as fp:
		fp.write(f'zfgene\t')
		fp.write('\t'.join(hgenes))
		fp.write('\n')
		for zgene in zgenes:
			fp.write(f'{zgene}\t')
			for hgene in hgenes:
				fp.write(f'{data[cmp][hgene][zgene]}\t')
			fp.write('\n')