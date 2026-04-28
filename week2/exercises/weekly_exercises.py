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
    
    # 1. Retrieve all customers
    query_1 = """
    -- TODO: Write a query to retrieve all customers
    """
    # run_query(query_1)
    
    # 2. Filter customers by city
    query_2 = """
    -- TODO: Write a query to filter customers by a specific city (e.g., 'Hyderabad')
    """
    # run_query(query_2)
    
    # 3. Join tables and display name + amount
    query_3 = """
    -- TODO: Write a query to join tables and display customer name and order amount
    """
    # run_query(query_3)
    
    # 4. Calculate total orders per customer
    query_4 = """
    -- TODO: Write a query to calculate the total number of orders per customer
    """
    # run_query(query_4)
    
    # 5. Find customers with missing values
    query_5 = """
    -- TODO: Write a query to find customers with missing values (e.g., age is NULL)
    """
    # run_query(query_5)

if __name__ == "__main__":
    main()
