import sqlite3
from pathlib import Path

def run_ddl(conn, query, description=""):
    cursor = conn.cursor()
    print(f"\n=== {description} ===")
    try:
        cursor.execute(query)
        print("Table created successfully.")
    except sqlite3.Error as e:
        print(f"SQL Error: {e}")

def main():
    conn = sqlite3.connect(":memory:")
    
    print("Welcome to Week 4: Data Modeling Exercises!")
    
    print("\n--- Day 1 & 2: Entities, Attributes, Keys ---")
    query_customers = """
    CREATE TABLE customers (
        customer_id INTEGER PRIMARY KEY,
        email TEXT UNIQUE NOT NULL,
        customer_name TEXT NOT NULL,
        city TEXT,
        created_date DATE
    );
    """
    run_ddl(conn, query_customers, "Creating Customers Entity")

    print("\n--- Day 3: Relationships (One-to-Many) ---")
    query_orders = """
    CREATE TABLE orders (
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        amount DECIMAL(10,2),
        order_date DATE,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    );
    """
    run_ddl(conn, query_orders, "Creating Orders Entity (One-to-Many with Customers)")

    print("\n--- Day 3: Many-to-Many & Bridge Tables ---")
    query_products = """
    CREATE TABLE products (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT,
        price DECIMAL(10,2)
    );
    """
    run_ddl(conn, query_products, "Creating Products Entity")

    query_order_items = """
    CREATE TABLE order_items (
        order_item_id INTEGER PRIMARY KEY,
        order_id INTEGER,
        product_id INTEGER,
        quantity INTEGER,
        price_at_purchase DECIMAL(10,2),
        FOREIGN KEY (order_id) REFERENCES orders(order_id),
        FOREIGN KEY (product_id) REFERENCES products(product_id)
    );
    """
    run_ddl(conn, query_order_items, "Creating Order Items (Bridge Table)")

    print("\n--- Day 6: Star Schema (Fact and Dimension Tables) ---")
    query_dim_customer = """
    CREATE TABLE dim_customer (
        customer_key INTEGER PRIMARY KEY,
        customer_id INTEGER,
        customer_name TEXT,
        city TEXT,
        segment TEXT
    );
    """
    run_ddl(conn, query_dim_customer, "Creating Dimension: Customer")

    query_fact_sales = """
    CREATE TABLE fact_sales (
        sales_id INTEGER PRIMARY KEY,
        date_key INTEGER,
        customer_key INTEGER,
        product_key INTEGER,
        quantity INTEGER,
        sales_amount DECIMAL(10,2),
        FOREIGN KEY (customer_key) REFERENCES dim_customer(customer_key)
    );
    """
    run_ddl(conn, query_fact_sales, "Creating Fact: Sales")

    print("\n--- Day 6: Slowly Changing Dimensions Type 2 ---")
    query_scd_customer = """
    CREATE TABLE dim_customer_scd2 (
        customer_key INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        customer_name TEXT,
        city TEXT,
        effective_start_date DATE,
        effective_end_date DATE,
        is_current BOOLEAN
    );
    """
    run_ddl(conn, query_scd_customer, "Creating SCD Type 2 Customer Dimension")

    conn.close()

if __name__ == "__main__":
    main()
