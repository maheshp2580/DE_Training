import csv
import json
import os
from pathlib import Path

def main():
    # Setup paths relative to the script location
    script_dir = Path(__file__).resolve().parent
    data_dir = script_dir.parent / "data"
    csv_file_path = data_dir / "students.csv"
    output_dir = data_dir / "output"
    
    # Ensure output directory exists (make sure the folder exists)
    os.makedirs(output_dir, exist_ok=True)
    
    all_rows = []
    names = []
    
    print("--- Reading CSV Rows ---")
    # Read the CSV using csv.DictReader
    with open(csv_file_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            all_rows.append(row)
            names.append(row["name"])
            # Prints each row (so you can see the dict)
            print(row)
            
    print("\n--- List of Names ---")
    # Prints a list of just the names
    print(names)
    
    print("\n--- Writing JSON Files ---")
    # One JSON file should be a list of all rows (each row as a dict)
    all_rows_path = output_dir / "all_students.json"
    with open(all_rows_path, mode="w", encoding="utf-8") as out_f:
        json.dump(all_rows, out_f, indent=4)
    print(f"Successfully wrote {len(all_rows)} rows to {all_rows_path.name}")
        
    # Optionally write another JSON file with one sample dict
    if all_rows:
        sample_path = output_dir / "sample_student.json"
        with open(sample_path, mode="w", encoding="utf-8") as sample_f:
            json.dump(all_rows[0], sample_f, indent=4)
        print(f"Successfully wrote 1 sample dict to {sample_path.name}")

if __name__ == "__main__":
    main()
