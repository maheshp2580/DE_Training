def validate_data(rows: list, expected_schema: set, min_rows: int = 1):
    if len(rows) < min_rows:
        raise ValueError(f"Validation Error: Expected at least {min_rows} rows, got {len(rows)}.")
        
    for idx, row in enumerate(rows):
        row_keys = set(row.keys())
        missing_keys = expected_schema - row_keys
        if missing_keys:
            raise ValueError(f"Validation Error in row {idx}: Missing expected columns {missing_keys}")

def main():
    good_data = [
        {"id": "1", "name": "Apple", "price": "1.00"},
        {"id": "2", "name": "Banana", "price": "0.50"}
    ]
    bad_data = [
        {"id": "3", "name": "Cherry"}
    ]
    
    expected_schema = {"id", "name", "price"}
    
    print("--- Validating Good Data ---")
    try:
        validate_data(good_data, expected_schema, min_rows=1)
        print("Good data passed validation successfully.")
    except Exception as e:
        print(e)
        
    print("\n--- Validating Bad Data (Missing Column) ---")
    try:
        validate_data(bad_data, expected_schema, min_rows=1)
    except Exception as e:
        print(f"Caught expected error: {e}")
        
    print("\n--- Validating Empty Data (Row Count Check) ---")
    try:
        validate_data([], expected_schema, min_rows=1)
    except Exception as e:
        print(f"Caught expected error: {e}")

if __name__ == "__main__":
    main()
