import sqlite3
from pathlib import Path

def setup_database():
    db_path = Path(__file__).parent / 'training.db'
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('DROP TABLE IF EXISTS orders;')
    cursor.execute('DROP TABLE IF EXISTS customers;')

    cursor.execute('''
        CREATE TABLE customers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            city TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE orders (
            order_id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            amount INTEGER,
            FOREIGN KEY(customer_id) REFERENCES customers(id)
        )
    ''')

    customers_data = [
        (1, 'Ravi', 25, 'Hyderabad'),
        (2, 'Asha', 30, 'Chennai'),
        (3, 'Imran', 22, 'Bangalore'),
        (4, 'Sita', None, 'Chennai')
    ]
    cursor.executemany('INSERT INTO customers (id, name, age, city) VALUES (?, ?, ?, ?)', customers_data)

    orders_data = [
        (101, 1, 500),
        (102, 2, 700),
        (103, 1, 300)
    ]
    cursor.executemany('INSERT INTO orders (order_id, customer_id, amount) VALUES (?, ?, ?)', orders_data)

    conn.commit()
    conn.close()
    print(f"Database successfully created at {db_path}")

if __name__ == '__main__':
    setup_database()
