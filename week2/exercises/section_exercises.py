import sqlite3
from pathlib import Path

def run_query(query):
    """Helper function to execute and print the query results."""
    db_path = Path(__file__).resolve().parent.parent / 'data' / 'training.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        cursor.execute(query)
        # Fetch headers
        headers = [description[0] for description in cursor.description]
        print(f"--- Query Results ---")
        print(" | ".join(headers))
        print("-" * 30)
        
        # Fetch and print rows
        rows = cursor.fetchall()
        for row in rows:
            print(" | ".join(str(val) for val in row))
        print(f"({len(rows)} rows returned)\n")
    except sqlite3.Error as e:
        print(f"SQL Error: {e}\n")
    finally:
        conn.close()

def main():
    print("=== Section 1: SELECT ===")
    # 1. Get all columns
    query_select_all = """
    -- TODO: Write a query to get all columns from the customers table
    """
    # run_query(query_select_all)
    
    # 2. Get only 'city'
    query_select_city = """
    -- TODO: Write a query to get only the city column from the customers table
    """
    # run_query(query_select_city)

    print("=== Section 2: WHERE ===")
    # 1. Find customers from Chennai
    query_where_chennai = """
    -- TODO: Write a query to find customers from Chennai
    """
    # run_query(query_where_chennai)
    
    # 2. Find age < 30
    query_where_age = """
    -- TODO: Write a query to find customers with age less than 30
    """
    # run_query(query_where_age)

    print("=== Section 3: ORDER BY ===")
    # 1. Sort by age ASC
    query_order_age = """
    -- TODO: Write a query to sort customers by age in ascending order
    """
    # run_query(query_order_age)
    
    # 2. Sort by name
    query_order_name = """
    -- TODO: Write a query to sort customers by name
    """
    # run_query(query_order_name)

    print("=== Section 4: JOIN ===")
    # 1. Join customers and orders
    query_join_all = """
    -- TODO: Write a query to join customers and orders tables
    """
    # run_query(query_join_all)
    
    # 2. Get name + amount
    query_join_name_amount = """
    -- TODO: Write a query to join customers and orders and get name and amount
    """
    # run_query(query_join_name_amount)

    print("=== Section 5: GROUP BY ===")
    # 1. Count per city
    query_group_count = """
    -- TODO: Write a query to count customers per city
    """
    # run_query(query_group_count)
    
    # 2. Sum amounts
    query_group_sum = """
    -- TODO: Write a query to get the sum of order amounts per customer
    """
    # run_query(query_group_sum)

    print("=== Section 6: HAVING ===")
    # 1. Cities with >1 customers
    query_having_cities = """
    -- TODO: Write a query to find cities with more than 1 customer
    """
    # run_query(query_having_cities)

    print("=== Section 7: NULL Handling ===")
    # 1. Find missing values
    query_null_age = """
    -- TODO: Write a query to find customers with missing age values
    """
    # run_query(query_null_age)

    print("=== Section 8: CASE Statement ===")
    # 1. Classify rows
    query_case_classify = """
    -- TODO: Write a query to classify customers as 'Adult' (age > 18) or 'Minor'
    """
    # run_query(query_case_classify)

if __name__ == "__main__":
    main()
