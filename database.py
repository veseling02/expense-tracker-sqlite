import sqlite3

table_statements =""" 
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY,
    type TEXT NOT NULL,
    amount REAL NOT NULL,
    date DATE)
                  """

try:
    with sqlite3.connect("transactions.db") as conn:
        print(f"Opened SQlite database with version {sqlite3.sqlite_version} successfully")
        cursor = conn.cursor()
        cursor.execute(table_statements)
        conn.commit()

except sqlite3.OperationalError as e:
    print("Failed to open database", e)


