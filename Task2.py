# Task 2: Categories (Sets)

# Product list
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer", "Headphones"]

# Parallel category list with matching length
categories = ["Electronics", "Accessories", "Accessories", "Electronics", "Office", "Accessories"]

# 1. Create a set of categories
categories_set = set(categories)

print("Unique categories:")
print(categories_set)

# 2. Add a new category and show duplicates are ignored
categories_set.add("Gaming")
categories_set.add("Electronics")   # duplicate, will be ignored

print("\nCategories after adding new and duplicate values:")
print(categories_set)

# 3. Check whether a category exists in the set
print("\nIs 'Office' in categories_set?")
print("Office" in categories_set)

# Extra (optional): total number of unique categories
print("\nTotal number of unique categories:")
print(len(categories_set))
