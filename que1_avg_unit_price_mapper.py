#!/usr/bin/env python
"""mapper.py"""

#Importing necessary libraries
import sys 
import pandas as pd


# Operations for every line in the stdin
for line in sys.stdin:
    
    #using the column name
    columns = ["index",'region','country','item_type','sales_channel','order_priority','order_date', 'order_id',	'ship_date',	'units_sold','unit_price',	'unit_cost', 	'total_revenue', 	'total_cost',	'total_profit']

    #removing tailing spaces
    line = line.strip()

    colvalues = line

    #splitting input line to column values
    cols = colvalues.split(',')
    rowJson = dict()

    #mapping input line to column names using dict for easier access
    for i in range(0,len(columns)):
        rowJson[columns[i]] = cols[i]

    #acessing required data
    order_date = pd.to_datetime(rowJson['order_date'])
    ship_date = pd.to_datetime(rowJson['ship_date'])
    year = order_date.year

    #creating the tab '\t' seperated key,value pair and prting - in order to stdin of reducer to pick
    key = (rowJson['country'],rowJson['item_type'],year)
    value = rowJson['unit_price']
    print('%s\t%s' % (key,value))




