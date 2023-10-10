import random
import csv

# Define the customer IDs and item numbers
customer_ids = list(range(1, 201))
item_numbers = list(range(1001, 1201))

# Create a dictionary to store the assigned items for each customer
assigned_items = {}

# Assign items to each customer
for customer_id in customer_ids:
    num_items = min(random.randint(1, 5), len(item_numbers))
    assigned_items[customer_id] = random.sample(item_numbers, num_items)
    item_numbers = [item for item in item_numbers if item not in assigned_items[customer_id]]

# Write the assigned items to a CSV file
with open('assigned_items.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['CustomerID', 'AssignedItems'])
    for customer_id, items in assigned_items.items():
        writer.writerow([customer_id] + items)
