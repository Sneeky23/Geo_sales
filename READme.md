
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


**Note:** To understand the execution of files, please [click here](BDS_Assignment2.pdf)