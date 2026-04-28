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
    -- TODO: Write a query that joins customers and orders, groups by the customer,
    -- and calculates both the total number of orders and the total revenue (sum of amounts).
    -- Make sure to include the customer's name in the results.
    """
    
    # run_query(query_report)

if __name__ == "__main__":
    main()
