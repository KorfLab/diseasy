import json

hsp = {}
with open('hsphenotypes.tsv') as fp:
	header = fp
	for line in fp:
		try:
			name, phe = line.rstrip().split('\t')
		except:
			continue
		if name not in hsp: hsp[name] = []
		hsp[name].append(phe)

zfp = {}
with open('zfphenotype.tsv') as fp:
	header = fp
	for line in fp:
		phe, name = line.rstrip().split('\t')
		if not phe: continue
		if name not in zfp: zfp[name] = []
		zfp[name].append(phe)

gene = {}
with open('zf2hs.tsv') as fp:
	for line in fp:
		if line.startswith('#'): continue
		zf, hs = line.rstrip().split('\t')
		if hs not in hsp: continue
		if zf not in zfp: continue
		if hs not in gene: gene[hs] = []
		gene[hs].append(zf)



data = []
i = 0
for name in gene:
	i += 1
	record = {
		'id': f'tag-{i}',
		'gene': name,
		'diseases': hsp[name],
		'd.rerio': []
	}
	for zfname in gene[name]:
		record['d.rerio'].append({'gene': zfname, 'phenotypes': zfp[zfname]})
	data.append(record)
	

print(json.dumps(data, indent=4))