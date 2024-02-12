import json


with open('diseasy.json') as fp:
	db = json.load(fp)

print(db)