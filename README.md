# Restaurant Management & Analytics System 📊

A Python project that manages restaurant billing and analyzes sales data. It allows users to take orders, save them to a database, and run reports to see sales trends.

## 🚀 Key Features

### 1. The Billing App
* **Take Orders:** Calculates total bills automatically.
* **Save Data:** Stores every order in a SQL database so no data is lost.

### 2. The Data Generator
* **Create Fake Data:** Includes a script (`generate_data.py`) that instantly adds 100+ sample orders to the database. This lets you test the analytics without typing orders manually.

### 3. The Analytics Report
* **Analyze Sales:** A special script (`analytics.py`) that uses **Pandas** to calculate:
    * 💰 Total Sales (Revenue)
    * 🏆 Best Selling Item
    * 💳 Most Used Payment Method (Cash vs Online)

