#!/usr/lib/python
"""reducer.py"""

import sys

unit_price = {}

#Partitoner
for line in sys.stdin:
    line = line.strip()
    key, price = line.split('\t')

    if key in unit_price:
        unit_price[key].append(float(price))
    else:
        unit_price[key] = []
        unit_price[key].append(float(price))

#Reducer
for key in unit_price.keys():
    avg_price = sum(unit_price[key]) / len(unit_price[key])
    print('%s\t%s'% (key, avg_price))