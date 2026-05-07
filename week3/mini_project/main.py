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
            print("-" * 60)
            
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
    print("Welcome to the Week 3 Mini Project!")
    print("Scenario: A fintech platform stores multiple status updates for every transaction.")
    print("The business wants a reporting dataset that keeps the latest valid transaction state")
    print("and supports quick fraud analyst reporting.\n")

    step1_query = """
    """

    step2_query = """
    """

    step3_query = """
    """

    step4_query = """
    """

if __name__ == "__main__":
    main()
    print("\nUncomment the run_query calls to test your steps.")
