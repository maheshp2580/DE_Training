# Print two greeting lines
print("Welcome to Chunk 1 of the DE Training assignment!")
print("This script demonstrates basic Python syntax and execution order.")

# Store first name and home town in variables; print both
first_name = "Jane"
home_town = "Seattle"
print(f"Name: {first_name}, Hometown: {home_town}")

# Four variables for a fake line item
item_label = "Ergonomic Keyboard"
units = 2
unit_cost = 75.50
on_sale = True

print(f"Item: {item_label}, Units: {units}, Cost/Unit: ${unit_cost}, On Sale: {on_sale}")

# If unit_cost > 50, print "over budget"; else print "fine"
if unit_cost > 50:
    print("over budget")
else:
    print("fine")

# A list of three place names; print each with a for loop
places = ["Portland", "Austin", "Denver"]
print("Places to visit:")
for place in places:
    print(f"- {place}")
