# Task 4: Combined Operations

# Product names
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones", "Webcam"]

# Prices dictionary
price_dict = {
    "Laptop": 55000,
    "Mouse": 600,
    "Keyboard": 1200,
    "Monitor": 9000,
    "Headphones": 2000,
    "Webcam": 1500
}

# Categories list
categories = ["Electronics", "Accessories", "Accessories", "Electronics", "Accessories", "Electronics"]

# 1. Create catalog list of tuples
catalog = []

for i in range(len(products)):
    catalog.append((products[i], price_dict[products[i]], categories[i]))

print("Catalog:")
print(catalog)

# 2. Create category_to_products dictionary
category_to_products = {}

for product, price, category in catalog:
    if category not in category_to_products:
        category_to_products[category] = []
    category_to_products[category].append(product)

print("\nCategory to products mapping:")
print(category_to_products)

# 3. Find category with maximum number of products
max_category = max(category_to_products, key=lambda x: len(category_to_products[x]))

print("\nCategory with maximum products:", max_category)
print("Products in this category:")
print(category_to_products[max_category])
