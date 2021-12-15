# Using Hadoop for historical sales data analysis 
**Note:** To understand the execution of files, please [click here](BDS_Assignment2.pdf)

### Business context:

 A large multi-national retail chain has sales orders data across regions and different sales channels for a large variety of item types. The business team wants to use this data to analyze various aspects of sales  - e.g. top selling items in a region, regions with maximum profit in a certain item type, if there is a significant difference in revenue in two item types across regions etc. 

### Problem statement:

As the data analytics team, use the sales transaction data set with about 100K records to answer these questions below — 

1. Average unit_price by country for a given item type in a certain year

2. Total units_sold by year for a given country and a given item type

3. Find the max and min units_sold in any order for each year by country for a given item type. Use a custom partitioner class instead of default hash based.

4. What are the top 10 order id for a given year by the total_profit 

You have to show the above analysis working on a Hadoop system using map reduce code, preferably in Java or Python. You can do data preparation steps as required before running a MapReduce job to answer these questions above.

### Question1: 
Average unit_price by country for a given item type in a certain year

* mapper file: [Average Unit Price Mapper](que1_avg_unit_price_mapper.py)  
* reducer file: [Average Unit Price Reducer](que1_avg_unit_price_reducer.py)  
* Ouptut: [Average Unit Price output](./question1_ans.txt)  

* O/p format: 
(Country, Item_type, Year)  Average Unit Price


### Question2: 
Total units_sold by year for a given country and a given item type

* mapper file: [Total Units Sold Mapper](que2_total_unit_sold_mapper.py)  
* reducer file: [Total Units Sold Reducer](que2_total_unit_sold_reducer.py)  
* Ouptut: [Total Units Sold output](./question2_ans.txt)  

* O/p format: 
 (Country, Item_type, Year)  Units Sold

### Question3: 
Find the max and min units_sold in any order for each year by country for a given item type
* mapper file: [Min-Max Units Sold Mapper](que3_min_max_units_sold_mapper.py)  
* reducer file: [Min-Max Units Sold Reducer](que3_min_max_units_sold_reducer.py)  
* Ouptut: [Min-Max Units Sold output](./question3_ans.txt)  
* O/p format: 
(Country, Item_type, Year)  (min_units, max_units)



### Question4: 
What are the top 10 order id for a given year by the total_profit

* mapper file: [Top Orders Mapper](que4_top_order_id_mapper.py)  
* reducer file: [Top Orders Reducer](que4_top_order_id_reducer.py)  
* Ouptut: [Top Orders output](./question4_ans.txt)  
* O/p format: 
Year  [ (Profit, OrderID1), (Profit, OrderID2), (Profit, OrderID3), ……..(Profit, OrderID10)]


