#!/usr/lib/python
"""reducer.py"""

import sys

unit_sold = {}

#Partitoner
for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')

    if key in unit_sold:
        unit_sold[key].append(float(value))
    else:
        unit_sold[key] = []
        unit_sold[key].append(float(value))

#Reducer
for key in unit_sold.keys():
    total = sum(unit_sold[key])
    print('%s\t%s'% (key, total))