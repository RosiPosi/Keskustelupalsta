import sqlite3

# Read your schema file
with open("schema.sql", "r") as f:
    schema = f.read()

# Create the database file (or open it if it exists)
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Execute the SQL commands from schema.sql
cursor.executescript(schema)

conn.commit()
conn.close()

print("database.db created successfully!")