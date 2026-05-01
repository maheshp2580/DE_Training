import sqlite3
from pathlib import Path

def run_query(query):
    """Helper function to execute and print the query results."""
    db_path = Path(__file__).resolve().parent.parent / 'data' / 'training.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        cursor.execute(query)
        headers = [description[0] for description in cursor.description]
        print(f"--- Query Results ---")
        print(" | ".join(headers))
        print("-" * 30)
        
        rows = cursor.fetchall()
        for row in rows:
            print(" | ".join(str(val) for val in row))
        print(f"({len(rows)} rows returned)\n")
    except sqlite3.Error as e:
        print(f"SQL Error: {e}\n")
    finally:
        conn.close()

def main():
    print("=== Weekly Exercises ===")
    
    query_1 = """
    SELECT * FROM customers;
    """
    run_query(query_1)
    
    query_2 = """
    SELECT * FROM customers WHERE city = 'Hyderabad';
    """
    run_query(query_2)
    
    query_3 = """
    SELECT customers.name, orders.amount FROM customers JOIN orders ON customers.id = orders.customer_id;
    """
    run_query(query_3)
    
    query_4 = """
    SELECT customers.name, COUNT(orders.order_id) AS total_orders FROM customers LEFT JOIN orders ON customers.id = orders.customer_id GROUP BY customers.id, customers.name;
    """
    run_query(query_4)
    
    query_5 = """
    SELECT * FROM customers WHERE age IS NULL;
    """
    run_query(query_5)

if __name__ == "__main__":
    main()
