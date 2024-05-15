import glob
import os
import statistics
import sys

aves = {}
for path in glob.glob(f'{sys.argv[1]}/*'):
	if 'ch211-' in path:
		splitme = path.replace('ch211-', 'ch211_')
	else:
		splitme = path
	gene, species, svt, lvw = os.path.basename(splitme).split('-')
	tag = f'{svt}-{lvw}'
	dists = []
	with open(path) as fp:
		for line in fp:
			source, target, dist = line.split()
			if source == target: continue
			dists.append(float(dist))
	if gene not in aves: aves[gene] = {}
	aves[gene][tag] = round(statistics.mean(dists), 4)

for gene in aves:
	print(gene, end='\t')
	for tag in aves[gene]:
		print(aves[gene][tag], end='\t')
	print()

	#print(aves[gene][tag], end='\t')
	#print()

