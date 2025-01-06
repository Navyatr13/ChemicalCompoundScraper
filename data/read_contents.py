import sqlite3
import pandas as pd

db_path = "data/compound_data.db"

# Connect to the database
conn = sqlite3.connect(db_path)

# Retrieve table names
tables_query = "SELECT name FROM sqlite_master WHERE type='table';"
tables = pd.read_sql(tables_query, conn)
print("Tables in the database:")
print(tables)

# Retrieve content from UnifiedCompounds
try:
    df = pd.read_sql("SELECT * FROM UnifiedCompounds;", conn)
    print("Contents of UnifiedCompounds:")
    print(df)
except Exception as e:
    print(f"Error querying UnifiedCompounds: {e}")

conn.close()
