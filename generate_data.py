import sqlite3
import random
from datetime import datetime, timedelta

# 1. Connect to your Database
conn = sqlite3.connect('restaurant_orders.db')
cursor = conn.cursor()

# 2. Define your "Fake" Data options
customers = ['Arya', 'Rohan', 'Priya', 'Amit', 'Sneha', 'Vikram', 'Anjali' , 'Isha' , 'Rohit' , 'Virat' , 'Pranjal' , 'Nevil' , 'Karan' , 'Kishan' , 'Rishi' , 'Harsh' , 'Manan']
items = {
    "Cheese Pizza": 80,
    "Veg Burger": 70,
    "Tea": 30,
    "Coffee": 40,
    "Dry Manchurian": 90,
    "Masala Dosa": 60,
    "Plain Dosa": 50,
    "White Pasta": 100,
    "Red Pasta": 120,
    "French Fries": 60,
    "Fanta": 20,
    "Cola": 25,
    "Soda": 30,
    "Thums Up": 35,
    "Idli Sambhar": 60,
}
payment_modes = ['Cash', 'UPI', 'Card']

# 3. Generate 100 Random Orders
print("Generating data...")

for i in range(200):
    # Pick random details
    name = random.choice(customers)
    item_name = random.choice(list(items.keys()))
    price = items[item_name]
    qty = random.randint(1, 5)  # Quantity between 1 and 5
    total = price * qty
    mode = random.choice(payment_modes)
    
    # Generate a random date (within last 30 days)
    days_ago = random.randint(0, 30)
    fake_date = datetime.now() - timedelta(days=days_ago)
    formatted_date = fake_date.strftime('%Y-%m-%d %H:%M:%S')

    # 4. Insert into Database
    # IMPORTANT: Change 'orders' below to your actual table name if it is different
    query = """INSERT INTO orders (customer_name, date, item, quantity, price, total, payment_method) 
               VALUES (?, ?, ?, ?, ?, ?, ?)"""
    
    cursor.execute(query, (name, formatted_date, item_name, qty, price, total, mode))

# 5. Save and Close
conn.commit()
print("Success! Added 100 new orders to your database.")
conn.close()