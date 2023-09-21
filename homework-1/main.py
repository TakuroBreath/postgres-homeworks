"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv

import psycopg2

with psycopg2.connect(host="localhost", database="north", user="postgres", password="2368") as conn:
    with conn.cursor() as cur:
        with open("north_data/customers_data.csv") as file:
            f = csv.DictReader(file)
            for line in f:
                cur.execute("INSERT INTO customers_data VALUES (%s, %s, %s)",
                            (line["customer_id"], line["company_name"], line["contact_name"]))

        with open("north_data/employees_data.csv") as file:
            f = csv.DictReader(file)
            for line in f:
                cur.execute("INSERT INTO employees_data VALUES(%s, %s, %s, %s, %s, %s)",
                            (line["employee_id"], line["first_name"], line["last_name"], line["title"],
                             line["birth_date"], line["notes"]))

        with open("north_data/orders_data.csv") as file:
            f = csv.DictReader(file)
            for line in f:
                cur.execute("INSERT INTO orders_data VALUES(%s, %s, %s, %s, %s)",
                            (line["order_id"], line["customer_id"], line["employee_id"], line["order_date"],
                             line["ship_city"]))

conn.close()
