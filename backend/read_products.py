import json

# Open the products file
with open("../knowledge/products.json", "r") as file:
    data = json.load(file)

# Get the list of products
products = data["products"]

# Print each product
for product in products:
    print(f"{product['name']} - Rs. {product['price']}")