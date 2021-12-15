#!/usr/lib/python
"""reducer.py"""

import sys

#creating hashmap to store top ten values
top_ten = {}

#Combiner
for line in sys.stdin:
    line = line.strip()
    keys, value = line.split('\t')

    if keys in top_ten :
        value = eval(value)
        top_ten[keys].append(value)
    else:
        top_ten[keys] = []
        value = eval(value)
        top_ten[keys].append(value)

#Reducer
for keys in top_ten.keys():
    total = sorted(top_ten[keys],key=lambda x: x[0],reverse=True)
    print('%s\t%s'% (keys, total[0:10]))