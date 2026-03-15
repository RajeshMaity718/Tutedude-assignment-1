#Task3:product Pricing(Dictionaries)
#1. Create a dictionary price_dict where keys are product names and values are prices(integers or floats)
price_dict={
    "laptop":5000,
    "Mouse":700,
    "Keyboard":1500,
    "Monitor":9000,
    "printer":7000,
    "Headphones":2000
    }
print(price_dict)

#2. Add a new product with price to price_dict
price_dict["camera"]=25000
print(price_dict)
#2.update the price of an existing product 
price_dict["Mouse"]=1000
print(price_dict)
#2. Remove a product by name 
product_to_remove = "mouse"

if product_to_remove in price_dict:
    del price_dict[product_to_remove]
    print("\nPrinter removed successfully.")
else:
    print("\nProduct not found.")

print("\nUpdated dictionary:")
print(price_dict)

#3. print the average price of all products(use only dictinary operations and basic arithmetic).

total = sum(price_dict.values())
average_price = total / len(price_dict)

print(average_price)
