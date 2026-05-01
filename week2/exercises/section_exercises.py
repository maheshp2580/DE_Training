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
    print("=== Section 1: SELECT ===")
    query_select_all = """
    SELECT * FROM customers;
    """
    run_query(query_select_all)
    
    query_select_city = """
    SELECT city FROM customers;
    """
    run_query(query_select_city)

    print("=== Section 2: WHERE ===")
    query_where_chennai = """
    SELECT * FROM customers WHERE city = 'Chennai';
    """
    run_query(query_where_chennai)
    
    query_where_age = """
    SELECT * FROM customers WHERE age < 30;
    """
    run_query(query_where_age)

    print("=== Section 3: ORDER BY ===")
    query_order_age = """
    SELECT * FROM customers ORDER BY age ASC;
    """
    run_query(query_order_age)
    
    query_order_name = """
    SELECT * FROM customers ORDER BY name;
    """
    run_query(query_order_name)

    print("=== Section 4: JOIN ===")
    query_join_all = """
    SELECT * FROM customers JOIN orders ON customers.id = orders.customer_id;
    """
    run_query(query_join_all)
    
    query_join_name_amount = """
    SELECT customers.name, orders.amount FROM customers JOIN orders ON customers.id = orders.customer_id;
    """
    run_query(query_join_name_amount)

    print("=== Section 5: GROUP BY ===")
    query_group_count = """
    SELECT city, COUNT(*) as customer_count FROM customers GROUP BY city;
    """
    run_query(query_group_count)
    
    query_group_sum = """
    SELECT customers.name, SUM(orders.amount) as total_amount FROM customers JOIN orders ON customers.id = orders.customer_id GROUP BY customers.id, customers.name;
    """
    run_query(query_group_sum)

    print("=== Section 6: HAVING ===")
    query_having_cities = """
    SELECT city FROM customers GROUP BY city HAVING COUNT(*) > 1;
    """
    run_query(query_having_cities)

    print("=== Section 7: NULL Handling ===")
    query_null_age = """
    SELECT * FROM customers WHERE age IS NULL;
    """
    run_query(query_null_age)

    print("=== Section 8: CASE Statement ===")
    query_case_classify = """
    SELECT name, CASE WHEN age > 18 THEN 'Adult' ELSE 'Minor' END AS classification FROM customers;
    """
    run_query(query_case_classify)

if __name__ == "__main__":
    main()
