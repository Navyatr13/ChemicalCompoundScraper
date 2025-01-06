import sqlite3
import pandas as pd

# Path to the database file
db_path = "compound_data.db"

# Connect to the database
#try:
connection = sqlite3.connect(db_path)
# Retrieve all tables in the database
query = "SELECT name FROM sqlite_master WHERE type='table';"
tables = pd.read_sql(query, connection)
print(tables)
# Read the contents of all tables
data = {}
for table in tables['name']:
    data[table] = pd.read_sql(f"SELECT * FROM {table};", connection)

connection.close()
for table_name, table_data in data.items():
    print(f"Contents of table '{table_name}':")
    print(table_data.head())  # Display first few rows
    print("\n")
#except Exception as e:
#    connection.close()
#    str(e)
