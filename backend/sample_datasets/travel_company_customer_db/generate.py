import sqlite3
import os
import datetime
from . import case_descriptions

def generate_travel_db(path):
    if os.path.exists(path):
        print("Database exists, no need to generate database")
        return

    print(f"Generating database at {path}...")
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    
    # Load and execute schema from SQL file
    schema_path = 'sample_datasets/travel_company_customer_db/schema.sql'
    with open(schema_path, 'r') as f:
        schema_sql = f.read()
    cursor.executescript(schema_sql)
    print("Database generated successfully")