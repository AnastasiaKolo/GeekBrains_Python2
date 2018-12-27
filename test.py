# -*- coding: utf8 -*-
from socket import *
import json
import time

with open('orders.json') as f_n:
    order_list = json.load(f_n)
print(order_list)
print(type(order_list))
print(order_list.keys())
for item in order_list.items():
    print(type(item))
print('----------------------')
new_data = {
        "item": 'table',
        "quantity": 5,
        "price": 15,
        "buyer": 'Mary',
        "date": '2018-12-26'
    }
order_list["orders"].append(new_data);
str=json.dumps(order_list)
print(str)