import pandas as pd
import numpy as np
from faker import Faker
from datetime import timedelta

fake = Faker()

# Define spending limits for categories
spending_limits = {
    'Housing': (700, 1000),
    'Subscriptions': (20, 50),
    'Food': (150, 300),
    'Gas/Transportation': (50, 150),
    'Clothing/Personal': (30, 100),
    'Miscellaneous': (20, 100)
}

# Function to generate sequential timestamps over a certain period
def generate_chronological_timestamps(start_date, num_transactions):
    return [start_date + timedelta(hours=i) for i in range(num_transactions)]

# Function to generate spending data
def generate_spending_data(num_transactions, start_date):
    categories = list(spending_limits.keys())

    # Generate data
    data = {
        'TransactionID': range(1, num_transactions + 1),
        'Category': [np.random.choice(categories) for _ in range(num_transactions)],
        'TransactionAmount': [
            round(np.random.uniform(*spending_limits[np.random.choice(categories)]), 2) 
            for _ in range(num_transactions)
        ],
        'Location': ['Orlando' for _ in range(num_transactions)],  # Fixed location (Orlando)
        'Timestamp': generate_chronological_timestamps(start_date, num_transactions)  # Chronological timestamps
    }

    # Create a DataFrame
    return pd.DataFrame(data)

# Example usage: Generate data for 100 transactions
num_transactions = 100
start_date = fake.date_time_this_year()  # Starting date for the first transaction

df = generate_spending_data(num_transactions, start_date)

# Display the first few rows
print(df.head())


