"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv

import psycopg2
from config import CUSTOMERS, EMPLOYEES, ORDERS


connect_database = psycopg2.connect(host="localhost", database="north",
                                    user="postgres", password="123")
try:
    with connect_database:
        with connect_database.cursor() as curs:
            with open(CUSTOMERS, encoding='utf-8') as customers_file:
                info_cudtomers = csv.DictReader(customers_file)
                for item in info_cudtomers:
                    curs.execute("INSERT INTO customers VALUES (%s, %s, %s)",
                                 (item['customer_id'], item['company_name'], item['contact_name']))
            with open(EMPLOYEES, encoding='utf-8') as employees_file:
                info_employees = csv.DictReader(employees_file)
                for employee in info_employees:
                    curs.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)",
                                 (employee['employee_id'],
                                  employee['first_name'],
                                  employee['last_name'],
                                  employee['title'],
                                  employee['birth_date'],
                                  employee['notes']))
            with open(ORDERS, encoding='utf-8') as orders_file:
                info_orders = csv.DictReader(orders_file)
                for order in info_orders:
                    curs.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
                                 (order['order_id'],
                                  order['customer_id'], order['employee_id'],
                                  order['order_date'], order['ship_city']))

finally:
    connect_database.close()
