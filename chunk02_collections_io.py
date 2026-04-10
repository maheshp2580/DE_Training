from pathlib import Path

# One dictionary: keys sku, title, department, msrp
product = {
    "sku": "ABC-12345",
    "title": "Wireless Mouse",
    "department": "Electronics",
    "msrp": 29.99
}

# Print only msrp
print(f"MSRP: ${product['msrp']}")

# Function shout_label(text) -> returns text.upper(). Call it once; print result.
def shout_label(text):
    return text.upper()

shout_result = shout_label(product['title'])
print(f"Shout Label: {shout_result}")

# Read stash/teaser_copy.txt with with open(...) as f, f.read()
file_path = Path(__file__).resolve().parent / "stash" / "teaser_copy.txt"

with open(file_path, "r") as f:
    content = f.read()
    print("\n--- File Content ---")
    print(content.strip())
