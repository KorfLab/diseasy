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
		if ':' in zfg: zfg = zfg.replace(':', '_') # `make` doesn't like colons
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
	'h2h' : (htext, 'human'),
	'z2z' : (ztext, 'zfish'),
	'h2z' : (htext, 'zfish'),
}

targets = {}
for basename, (text, d) in base.items():
	for name in text:
		for cmp in ('txt', 'sem'):
			for opt in ('words', 'lines'):
				target = f'{name}-{d}-{cmp}-{opt}'
				if name in text: f = f'build/human/{name}'
				else:            f = f'build/zfish/{name}'
				if cmp == 'txt': p = 'python3 txtcmp.py'
				else:            p = 'python3 semcmp.py'
				out = f'build/{basename}/{target}'
				cli = f'{p} {f} build/{d} {opt} > {out}'
				targets[out] = cli

# create makefile
print('all:\\')
for target in targets:
	print(f'\t{target}\\')
print()

for target, cli in targets.items():
	print(f'{target}:\n\t{cli}\n')

print(len(targets), 'jobs', file=sys.stderr)
