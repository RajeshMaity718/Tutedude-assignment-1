# Task 1: Product Collections (Lists & Tuples)

# 1. Create a list with at least 6 product names
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer", "Headphones"]

# 2. Create a tuple for one product: (product_name, price, category)
sample_product = ("Laptop", 55000, "Electronics")

# 3. Print the 2nd and last product from the list
print("Second product:", products[1])
print("Last product:", products[5])

# 4. Append two new product names and print updated list
products.append("Webcam")
products.append("Speaker")
print(products)

# Extra (optional): Convert tuple to list, change price, and convert back to tuple
sample_product_list = list(sample_product)
sample_product_list[1] = 60000   # changing price
sample_product = tuple(sample_product_list)
print(sample_product)
