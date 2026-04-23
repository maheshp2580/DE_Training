import csv
import json
import os
from pathlib import Path

def main():
    script_dir = Path(__file__).resolve().parent
    data_dir = script_dir.parent / "data"
    csv_file_path = data_dir / "students.csv"
    output_dir = data_dir / "output"
    
    os.makedirs(output_dir, exist_ok=True)
    
    all_rows = []
    names = []
    
    print("--- Reading CSV Rows ---")
    with open(csv_file_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            all_rows.append(row)
            names.append(row["name"])
            print(row)
            
    print("\n--- List of Names ---")
    print(names)
    
    print("\n--- Writing JSON Files ---")
    all_rows_path = output_dir / "all_students.json"
    with open(all_rows_path, mode="w", encoding="utf-8") as out_f:
        json.dump(all_rows, out_f, indent=4)
    print(f"Successfully wrote {len(all_rows)} rows to {all_rows_path.name}")
        
    if all_rows:
        sample_path = output_dir / "sample_student.json"
        with open(sample_path, mode="w", encoding="utf-8") as sample_f:
            json.dump(all_rows[0], sample_f, indent=4)
        print(f"Successfully wrote 1 sample dict to {sample_path.name}")

if __name__ == "__main__":
    main()
