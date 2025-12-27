import pandas as pd
import sqlite3
# Connect with Database
conn = sqlite3.connect('restaurant_orders.db')


# Load Data into Pandas
sql_query = "Select * from orders"
df = pd.read_sql_query(sql_query,conn)

# Data Analytics Report
print("----- RESTAURANT ANALYTICS REPORT -----")
print("-" *39)

# Total Revenue we created
total_revenue = df['total'].sum()
print(f"Total Revenue : {total_revenue}")

# Most Popular Item
popular_item = df['item'].mode()[0]
print(f"Popular Item : {popular_item}")

# How are people paying? (Cash or UPI(online) or Card)
payment_status = df['payment_method'].value_counts()
print(f"Payment Methods Used")
print(payment_status)

# Most Expensive Orders
expensive_orders = df.loc[df['total'].idxmax()]
print(f"Most Expensive Order : {expensive_orders}")

top3 = df.nlargest(3,'total')
print("TOP 3 Expensive Orders")
print(top3[['customer_name' , 'item' , 'total']])
print("-"*39)