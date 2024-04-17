
import statistics
import sys

data= {
	"sklearntext": [],
	"transformer": [],
	"tensorflow": [],
}

with open(sys.argv[1]) as fp:
	for i in range(6):
		line=fp.readline()
	for line in fp:
		f = line.split()
		if len(f) != 4: continue
		gene1, gene2, method, score = f
		data[method].append(float(score))


for method,values in data.items():
	print(method, statistics.mean(values), statistics.stdev(values))
