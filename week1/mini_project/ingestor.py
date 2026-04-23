import csv
import logging
from pathlib import Path

EXPECTED_COLUMNS = ['product_id', 'name', 'price', 'category', 'vendor']

def setup_logger(log_file):
    logger = logging.getLogger('MiniProjectIngestor')
    logger.setLevel(logging.ERROR)
    if not logger.handlers:
        fh = logging.FileHandler(log_file, mode='w', encoding='utf-8')
        fh.setFormatter(logging.Formatter('%(asctime)s - ERROR - %(message)s'))
        logger.addHandler(fh)
    return logger

class ProductIngestor:
    def __init__(self, log_path: Path):
        self.logger = setup_logger(log_path)
        self.products = {}
        self.bad_records = 0

    def ingest_vendor_a(self, csv_path: Path):
        self.process_csv(csv_path, 'Vendor A', {
            'product_id': 'id',
            'name': 'title',
            'price': 'cost',
            'category': 'department'
        })
        
    def ingest_vendor_b(self, csv_path: Path):
        self.process_csv(csv_path, 'Vendor B', {
            'product_id': 'sku',
            'name': 'product_name',
            'price': 'price',
            'category': 'category'
        })

    def process_csv(self, csv_path: Path, vendor_name: str, mapping: dict):
        if not csv_path.exists():
            self.logger.error(f"File not found: {csv_path}")
            return
            
        with open(csv_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for file_idx, row in enumerate(reader, start=1):
                try:
                    product_id = row.get(mapping['product_id'], '').strip()
                    name = row.get(mapping['name'], '').strip()
                    price_str = row.get(mapping['price'], '').strip()
                    category = row.get(mapping['category'], '').strip()
                    
                    if not product_id or not name:
                        raise ValueError("Missing critical field 'product_id' or 'name'")
                        
                    if not price_str:
                        price = 0.0
                    else:
                        price = float(price_str)
                        if price < 0:
                            raise ValueError("Price cannot be negative")
                            
                    if not category:
                        category = "Uncategorized"
                        
                    unified_record = {
                        'product_id': product_id,
                        'name': name,
                        'price': price,
                        'category': category,
                        'vendor': vendor_name
                    }
                    
                    unique_key = name.lower()
                    if unique_key not in self.products:
                        self.products[unique_key] = unified_record
                except Exception as e:
                    self.bad_records += 1
                    self.logger.error(f"{vendor_name} File Row {file_idx}: {str(e)} | Data: {row}")

    def get_trusted_records(self):
        return list(self.products.values())
