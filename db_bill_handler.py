import sqlite3
import csv
import os
from datetime import datetime

def init_db():
    conn = sqlite3.connect("restaurant_orders.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT,
            date TEXT,
            item TEXT,
            quantity INTEGER,
            price REAL,
            total REAL,
            payment_method TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_order_to_db(customer_name, cart , payment_method):
    conn = sqlite3.connect("restaurant_orders.db")
    cur = conn.cursor()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for item, qty, price, total in cart:
        cur.execute("""
            INSERT INTO orders (customer_name, date, item, quantity, price, total , payment_method)
            VALUES (?, ?, ?, ?, ?, ? , ?)
        """, (customer_name, date, item, qty, price, total , payment_method))

    conn.commit()
    conn.close()
    print("Order saved to database.")

#----- View Orders ---------
def view_orders():
    conn = sqlite3.connect("restaurant_orders.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM orders")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.close()
    return rows

    
if __name__ == "__main__":
    view_orders()

