import sqlite3

def run_ddl(conn, query, description=""):
    cursor = conn.cursor()
    print(f"\n=== {description} ===")
    try:
        cursor.execute(query)
        print("Table created successfully.")
    except sqlite3.Error as e:
        print(f"SQL Error: {e}")

def main():
    print("Welcome to the Week 4 Mini Project: E-commerce Warehouse Model")
    print("Scenario: Design a star schema replacing a spreadsheet-based system.")
    print("You must define Entities, Keys, Relationships, Fact Grain, and SCD types.")
    
    conn = sqlite3.connect(":memory:")

    dim_product_query = """
    """
    
    dim_customer_query = """
    """
    
    dim_date_query = """
    """

    dim_promotion_query = """
    """

    fact_sales_query = """
    """

    conn.close()

if __name__ == "__main__":
    main()
