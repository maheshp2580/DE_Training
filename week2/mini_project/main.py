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
    print("=== Mini Project ===")
    print("Build a report containing:")
    print("- Total orders per customer")
    print("- Total revenue per customer")
    print("(Use JOIN + GROUP BY + aggregation functions)\n")
    
    query_report = """
    SELECT customers.name, COUNT(orders.order_id) AS total_orders, SUM(orders.amount) AS total_revenue
    FROM customers
    LEFT JOIN orders ON customers.id = orders.customer_id
    GROUP BY customers.id, customers.name;
    """
    
    run_query(query_report)

if __name__ == "__main__":
    main()
