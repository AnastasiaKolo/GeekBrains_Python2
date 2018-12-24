# coding=cp1251
# 2. ������� �� ����������� ������ �� ������ json.
# ���� ���� orders � ������� JSON � ����������� � �������. �������� ������,
# ���������������� ��� ���������� �������.
# ��� �����:
# ������� ������� write_order_to_json(), � ������� ���������� 5 ���������� �
# ����� (item), ���������� (quantity), ���� (price), ���������� (buyer), ����
# (date). ������� ������ ���������������  ������ ������ � ���� ������� � ����
# orders.json. ��� ������ ������ ������� �������� ������� � 4 ���������� �������;
# ��������� ������ ��������� ����� ����� ������� write_order_to_json() � ���������
# � ��� �������� �������
# ���������. ###

import json


def write_order_to_json(item, quantity, price, buyer, date):
    dict_to_json = {
        "item": item,
        "quantity": quantity,
        "price": price,
        "buyer": buyer,
        "date": date
    }
    with open('orders.json', 'a') as o_j:
        o_j.write(json.dumps(dict_to_json, indent=4))


write_order_to_json('fork', 5, 124, 'Jane', '25.10.2018')
write_order_to_json('table', 2, 2099, 'Mark', '16.10.2018')
