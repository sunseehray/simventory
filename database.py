import sqlite3

def connect_db():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    # Create products table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL
    )
    """)

    conn.commit()
    conn.close()

connect_db()