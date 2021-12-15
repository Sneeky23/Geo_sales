#!/usr/lib/python
"""reducer.py"""

import sys

# Custom Partitoner Class and reducer
class MinMaxPartitionClass:

    def __init__(self):
        self.unit_sold = {}
    

    def update_min_max(self,key,val):
        value = float(val)
        if key not in self.unit_sold.keys():
            self.unit_sold[key] ={'max': value, 'min': value}
        else:
            self.unit_sold[key]['min'] = value if self.unit_sold[key]['min'] < value else self.unit_sold[key]['min'] 
            self.unit_sold[key]['max'] = value if self.unit_sold[key]['max'] > value else self.unit_sold[key]['max'] 
        
        return self.unit_sold


# Object for paritioner class
mmObject = MinMaxPartitionClass()
updated_units_sold = {}


# for each line in input update min max value in object
for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')
    updated_units_sold = mmObject.update_min_max(key,value)
    

# printing min, max values for every key in the data setd
for key in updated_units_sold.keys():
    max_unit = updated_units_sold[key]['min']
    min_unit = updated_units_sold[key]['max']
    print('%s\t%s'% (key, (min_unit,max_unit)))