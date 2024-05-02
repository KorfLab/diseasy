import argparse
import json
import os
import sys


## Command Line Interface ##
parser = argparse.ArgumentParser('Makefile writer')
parser.add_argument('--limit', type=int, default=0)
arg = parser.parse_args()

human = 'build/human'
zfish = 'build/zfish'
h2h = 'build/h2h'
z2z = 'build/z2z'
h2z = 'build/h2z'

# make directories
for d in (human, zfish, h2h, z2z, h2z):
	if not os.path.exists(d): os.makedirs(d)

# get all data
htext = {}
ztext = {}
with open('diseasy.json') as fp:
	d = json.load(fp)

for i, entry in enumerate(d):
	hg = entry['gene']
	htext[hg] = entry['diseases']
	for zd in entry['d.rerio']:
		zfg = zd['gene']
		ztext[zfg] = zd['phenotypes']
	if arg.limit and i+1 == arg.limit:
		print('reached limit:', arg.limit, file=sys.stderr)
		break

print('human genes:', len(htext.keys()), file=sys.stderr)
print('zfish genes:', len(ztext.keys()), file=sys.stderr)

# create human files
for gene, text in htext.items():
	with open(f'{human}/{gene}', 'w') as fp:
		fp.write('\n'.join(text))

# create zfish files
for gene, text in ztext.items():
	with open(f'{zfish}/{gene}', 'w') as fp:
		fp.write('\n'.join(text))

# organize jobs
base = {
	'h2h' : (htext, htext),
	'z2z' : (ztext, ztext),
	'h2z' : (htext, ztext),
}

targets = {}
for basename, (t1, t2) in base.items():
	for n1 in t1:
		for n2 in t2:
			for cmp in ('txt', 'sem'):
				for opt in ('words', 'lines'):
					target = f'{n1}-{n2}-{cmp}-{opt}'
					if n1 in htext: f1 = f'build/human/{n1}'
					else:           f1 = f'build/zfish/{n1}'
					if n2 in htext: f2 = f'build/human/{n2}'
					else:           f2 = f'build/zfish/{n2}'
					if cmp == 'txt': p = 'python3 txtcmp.py'
					else:            p = 'python3 semcmp.py'
					out = f'build/{basename}/{target}'
					cli = f'{p} {f1} {f2} {opt} > {out}'
					targets[out] = cli

# create makefile
print('all:\\')
for target in targets:
	print(f'\t{target}\\')
print()

for target, cli in targets.items():
	print(f'{target}:\n\t{cli}\n')

print(len(targets), 'jobs', file=sys.stderr)