import glob
import os
import sys

if len(sys.argv) != 3: sys.exit(f'{sys.argv[0]} <dir> <method> (not {sys.argv}')

matrix = {}
sources = {}
targets = {}
for path in glob.glob(f'{sys.argv[1]}/*{sys.argv[2]}'):
	if 'ch211-' in path:
		splitme = path.replace('ch211-', 'ch211_')
	else:
		splitme = path
	gene, species, svt, lvw = os.path.basename(splitme).split('-')
	tag = f'{svt}-{lvw}'
	with open(path) as fp:
		for line in fp:
			source, target, dist = line.split()
			source = os.path.basename(source)
			target = os.path.basename(target)
			if source not in matrix: matrix[source] = {}
			matrix[source][target] = dist
			if source not in sources: sources[source] = True
			if target not in targets: targets[target] = True

names = ['']
names.extend(list(matrix.keys()))
print('\t'.join(names))
for n1 in sources:
	print(n1, end='\t')
	for n2 in sources:
		print(matrix[n1][n2], end='\t')
	print()

