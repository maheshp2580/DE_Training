import csv
import logging
from pathlib import Path

def setup_logging(log_file):
    logger = logging.getLogger('BadRecordLogger')
    logger.setLevel(logging.ERROR)
    
    if not logger.handlers:
        fh = logging.FileHandler(log_file, mode='w', encoding='utf-8')
        fh.setLevel(logging.ERROR)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        
    return logger

def is_valid_record(row):
    price_str = row.get("Price", "").strip()
    if not price_str:
        return False, "Missing Price"
    try:
        price = float(price_str)
        if price < 0:
            return False, "Negative Price"
    except ValueError:
        return False, "Invalid Price Format"
        
    if not row.get("Product ID", "").strip():
        return False, "Missing Product ID"
        
    return True, ""

def main():
    script_dir = Path(__file__).resolve().parent
    data_dir = script_dir.parent / "data"
    input_csv = data_dir / "products_raw.csv"
    output_dir = data_dir / "output"
    
    output_dir.mkdir(exist_ok=True)
    log_file = output_dir / "bad_records.log"
    
    logger = setup_logging(log_file)
    
    valid_records = []
    total_records = 0
    bad_records_count = 0
    
    print("\n--- Processing Records with Logging ---")
    with open(input_csv, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        reader.fieldnames = [n.strip() for n in reader.fieldnames]
        for idx, row in enumerate(reader, start=1):
            total_records += 1
            is_valid, error_msg = is_valid_record(row)
            
            if is_valid:
                valid_records.append(row)
            else:
                bad_records_count += 1
                logger.error(f"Row {idx} failed validation: {error_msg} | Data: {row}")

    print(f"Total Records: {total_records}")
    print(f"Valid Records: {len(valid_records)}")
    print(f"Bad Records: {bad_records_count}")
    print(f"Check {log_file} for details on discarded records.")

if __name__ == "__main__":
    main()
