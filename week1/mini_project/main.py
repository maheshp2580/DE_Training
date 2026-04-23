import json
from pathlib import Path
from ingestor import ProductIngestor

def main():
    script_dir = Path(__file__).resolve().parent
    data_dir = script_dir.parent / "data"
    output_dir = data_dir / "output"
    
    vendor_a_csv = data_dir / "vendor_a.csv"
    vendor_b_csv = data_dir / "vendor_b.csv"
    
    output_dir.mkdir(exist_ok=True)
    
    log_file = output_dir / "ingestion_errors.log"
    trusted_output = output_dir / "trusted_products.json"
    
    print("--- Starting Multi-Vendor Product Ingestion ---")
    
    ingestor = ProductIngestor(log_file)
    
    print("Ingesting Vendor A...")
    ingestor.ingest_vendor_a(vendor_a_csv)
    
    print("Ingesting Vendor B...")
    ingestor.ingest_vendor_b(vendor_b_csv)
    
    trusted_data = ingestor.get_trusted_records()
    
    print(f"\nIngestion Complete.")
    print(f"Total trusted (deduplicated) records: {len(trusted_data)}")
    print(f"Total bad records skipped: {ingestor.bad_records}")
    print(f"Error log available at: {log_file.name}")
    
    with open(trusted_output, mode='w', encoding='utf-8') as out_f:
        json.dump(trusted_data, out_f, indent=4)
        
    print(f"Clean Trusted data written to: {trusted_output.name}")

if __name__ == "__main__":
    main()
