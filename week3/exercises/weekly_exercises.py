import sqlite3
from pathlib import Path

def run_query(query, description=""):
    """Helper function to execute and print the query results."""
    db_path = Path(__file__).resolve().parent.parent / 'data' / 'training.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"\n=== {description} ===")
    try:
        cursor.execute(query)
        if cursor.description:
            headers = [desc[0] for desc in cursor.description]
            print(" | ".join(headers))
            print("-" * 50)
            
            rows = cursor.fetchall()
            for row in rows:
                print(" | ".join(str(val) for val in row))
            print(f"({len(rows)} rows returned)")
        else:
            print("Query executed successfully.")
    except sqlite3.Error as e:
        print(f"SQL Error: {e}")
    finally:
        conn.close()

def main():
    task1_query = """
    """

    task2_query = """
    """

    task3_query = """
    """

    task4_query = """
    """

    task5_query = """
    """

    task6_query = """
    """

    task7_query = """
    """

if __name__ == "__main__":
    main()
    print("Uncomment the run_query calls to test your answers.")
