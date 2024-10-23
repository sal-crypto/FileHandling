import csv

import datetime

product_data={
    "P001" : ["wireless headphone" , 100],
    "P002" : ["computers" , 10000],
    "P003" : ["speakers" , 1000],
    "P004" : ["tab" , 1000],
    "P005" : ["charger" , 500],
    "P006" : ["Android phone" , 1000],
    "P007" : ["iphone" , 9000],
    "P008" : ["watch" , 100],
    "P009" : ["clock" , 100],
    "P010" : ["game_box" , 1000],

}

csv_data= []

with open('product_sales.txt' , 'r') as file:
    product_IDS = file.readlines()
Sale_id= 1
current_date= datetime.date.today()
current_time=datetime.datetime.now()

for product_id in product_IDS:
    Sale_id=Sale_id+1
    product_id=product_id.strip('\n')
    product_name=product_data[product_id][0]
    product_price=product_data[product_id][1]

    row= [current_date,product_name,product_price, Sale_id, product_id, product_name, product_price]
    csv_data.append(row)

with open('product_sales.csv', 'w',newline= '') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Current_date', ' Sale_id', 'Product_id', 'Product_name', 'Product_price'])
    writer.writerows(csv_data)




