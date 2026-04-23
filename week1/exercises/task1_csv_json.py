import csv
import json
from pathlib import Path

def clean_value(val):
    val = val.strip() if isinstance(val, str) else val
    return val if val else None

def standardize_header(header):
    return header.strip().lower().replace(" ", "_")

def main():
    script_dir = Path(__file__).resolve().parent
    data_dir = script_dir.parent / "data"
    input_csv = data_dir / "products_raw.csv"
    output_dir = data_dir / "output"
    output_json = output_dir / "cleaned_products.json"
    
    output_dir.mkdir(exist_ok=True)
    
    cleaned_rows = []
    
    with open(input_csv, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        try:
            headers = next(reader)
        except StopIteration:
            print("Empty CSV file.")
            return

        standardized_headers = [standardize_header(h) for h in headers]
        
        for row in reader:
            cleaned_row = {}
            is_empty_row = True
            for header, value in zip(standardized_headers, row):
                cleaned_val = clean_value(value)
                cleaned_row[header] = cleaned_val
                if cleaned_val is not None:
                    is_empty_row = False
                    
            if not is_empty_row:
                cleaned_rows.append(cleaned_row)
                
    with open(output_json, mode="w", encoding="utf-8") as f:
        json.dump(cleaned_rows, f, indent=4)
        
    print(f"Processed {len(cleaned_rows)} cleaned records into {output_json.name}")

if __name__ == "__main__":
    main()
