import sqlite3
from pathlib import Path

def run_query(query):
    """Helper function to execute and print the query results."""
    db_path = Path(__file__).resolve().parent.parent / 'data' / 'training.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        cursor.execute(query)
        if cursor.description:
            headers = [description[0] for description in cursor.description]
            print(f"--- Query Results ---")
            print(" | ".join(headers))
            print("-" * 50)
            
            rows = cursor.fetchall()
            for row in rows:
                print(" | ".join(str(val) for val in row))
            print(f"({len(rows)} rows returned)\n")
        else:
            print("Query executed successfully. (No data returned)\n")
            
    except sqlite3.Error as e:
        print(f"SQL Error: {e}\n")
    finally:
        conn.close()

def main():
    print("=== Section 1: Common Table Expressions (CTEs) ===")
    query_cte = """
    WITH filtered_customers AS (
        SELECT customer_id, name, city, age
        FROM customers
        WHERE age > 25
    )
    SELECT *
    FROM filtered_customers;
    """
    run_query(query_cte)

    print("=== Section 2: Window Function - ROW_NUMBER ===")
    query_row_number = """
    SELECT name, city, age,
           ROW_NUMBER() OVER (
               PARTITION BY city
               ORDER BY age DESC
           ) AS city_age_rank
    FROM customers;
    """
    run_query(query_row_number)

    print("=== Section 3: RANK and DENSE_RANK ===")
    query_rank = """
    SELECT order_id, customer_id, amount,
           RANK() OVER (ORDER BY amount DESC) AS amount_rank,
           DENSE_RANK() OVER (ORDER BY amount DESC) AS dense_amount_rank
    FROM orders;
    """
    run_query(query_rank)

    print("=== Section 4: LAG and LEAD for trend analysis ===")
    query_lag = """
    SELECT customer_id, updated_at, amount,
           LAG(amount) OVER (
               PARTITION BY customer_id
               ORDER BY updated_at
           ) AS previous_amount
    FROM transactions;
    """
    run_query(query_lag)

    print("=== Section 5: Subqueries and correlated subqueries ===")
    query_subquery = """
    SELECT name
    FROM customers
    WHERE customer_id IN (
        SELECT customer_id
        FROM orders
    );
    """
    run_query(query_subquery)

    print("=== Section 6: Deduplication and latest-record selection ===")
    query_dedup = """
    WITH ranked_customers AS (
        SELECT customer_id, name, city, age, updated_at,
               ROW_NUMBER() OVER (
                   PARTITION BY customer_id
                   ORDER BY updated_at DESC
               ) AS rn
        FROM customers
    )
    SELECT customer_id, name, city, age, updated_at
    FROM ranked_customers
    WHERE rn = 1;
    """
    run_query(query_dedup)

    print("=== Section 7 & 8: Query optimization basics & Indexes ===")
    query_optimization = """
    SELECT customer_id, amount, order_date
    FROM orders
    WHERE order_date >= '2024-02-01'
      AND status = 'completed';
    """
    run_query(query_optimization)
    
    query_explain = """
    EXPLAIN QUERY PLAN
    SELECT customer_id, amount, order_date
    FROM orders
    WHERE order_date >= '2024-02-01'
      AND status = 'completed';
    """
    run_query(query_explain)

if __name__ == "__main__":
    main()
