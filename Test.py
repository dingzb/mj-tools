import json

import re

lm = []
lm.append({'hostname': '111.1.1.1'})
lm.append({'hostname': '111.1.1.3'})
lm.append({'hostname': '111.1.1.2'})

file = open('json', 'w')

json.dump(lm, file)

file.close()
file = open('json', 'r')
jj = json.load(file)
jj = list(jj)
print(jj)

for j in jj:
    print dict(j)

