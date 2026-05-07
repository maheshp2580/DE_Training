import sqlite3
from pathlib import Path

def setup_database():
    db_path = Path(__file__).parent / 'training.db'
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('DROP TABLE IF EXISTS orders;')
    cursor.execute('DROP TABLE IF EXISTS customers;')
    cursor.execute('DROP TABLE IF EXISTS transactions;')

    cursor.execute('''
        CREATE TABLE customers (
            customer_id INTEGER,
            name TEXT NOT NULL,
            city TEXT,
            age INTEGER,
            updated_at TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE orders (
            order_id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            order_date TEXT,
            amount INTEGER,
            status TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE transactions (
            transaction_id INTEGER,
            customer_id INTEGER,
            status TEXT,
            amount INTEGER,
            updated_at TEXT,
            source_system TEXT
        )
    ''')

    customers_data = [
        (1, 'Ravi', 'Hyderabad', 25, '2024-01-10'),
        (2, 'Asha', 'Chennai', 30, '2024-01-12'),
        (3, 'Imran', 'Hyderabad', 22, '2024-01-11'),
        (1, 'Ravi', 'Hyderabad', 26, '2024-02-01')
    ]
    cursor.executemany('INSERT INTO customers (customer_id, name, city, age, updated_at) VALUES (?, ?, ?, ?, ?)', customers_data)

    orders_data = [
        (101, 1, '2024-01-01', 500, 'completed'),
        (102, 2, '2024-02-01', 700, 'completed'),
        (103, 1, '2024-03-01', 300, 'returned'),
        (104, 3, '2024-03-05', 250, 'completed')
    ]
    cursor.executemany('INSERT INTO orders (order_id, customer_id, order_date, amount, status) VALUES (?, ?, ?, ?, ?)', orders_data)

    transactions_data = [
        (1001, 1, 'PENDING', 500, '2024-04-01 10:00:00', 'web'),
        (1001, 1, 'COMPLETED', 500, '2024-04-02 14:30:00', 'bank_api'),
        (1002, 2, 'PENDING', 1200, '2024-04-03 09:15:00', 'app'),
        (1003, 1, 'FAILED', 300, '2024-04-04 11:00:00', 'web'),
        (1002, 2, 'COMPLETED', 1200, '2024-04-04 16:45:00', 'bank_api')
    ]
    cursor.executemany('INSERT INTO transactions (transaction_id, customer_id, status, amount, updated_at, source_system) VALUES (?, ?, ?, ?, ?, ?)', transactions_data)



    conn.commit()
    conn.close()
    print(f"Database successfully created at {db_path}")

if __name__ == '__main__':
    setup_database()
