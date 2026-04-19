import sqlite3
from models import Transaction

table_statements =""" 
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY,
    type TEXT NOT NULL,
    category TEXT NOT NULL,
    item TEXT NOT NULL,
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


def create_transaction(type, category, item, amount, date):
    with sqlite3.connect("transactions.db") as conn:
        curs = conn.cursor()
        curs.execute("INSERT INTO transactions (type, category, item, amount, date) VALUES (?, ?, ?, ?, ?)", (type, category, item, amount, date))
        conn.commit()


def get_all_trans():
    with sqlite3.connect("transactions.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM transactions")
        rows = cursor.fetchall()

        return [Transaction(id=r[0], type=r[1], category=r[2], item=r[3], amount=r[4], date=r[5]) for r in rows]
    
def delete_transaction(trans_id):
    with sqlite3.connect("transactions.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM transactions WHERE id = ?", (trans_id,))
        conn.commit()

def get_total_spent():
    with sqlite3.connect("transactions.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(amount) FROM transactions")
        
        result = cursor.fetchone()

        return result[0] if result[0] else 0.0
    
def clear_all():
    with sqlite3.connect("transactions.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM transactions")
        conn.commit()
        
 

if __name__ == "__main__":
    print("Testing insertion...")
    create_transaction("expense", "water", 34, "2022-04-14")
    print("Insertion complete!")

    print("\ntesting view all")
    print(get_all_trans())
    print("test complete")
    
    print("\ntesting delete funct")
    delete_transaction("6")
    print(get_all_trans())
    print("test complete")

    print("\ntesting total spent")
    print(get_total_spent())
    print("test complete")
