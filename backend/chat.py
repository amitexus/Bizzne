import json

# Load products
with open("../knowledge/products.json", "r") as file:
    data = json.load(file)

products = data["products"]

# Customer message
question = input("Customer: ")

# Find answer
if "bottle" in question.lower():
    for product in products:
        if "Bottle" in product["name"]:
            print(f"Bizzne: Our {product['name']} costs Rs. {product['price']}.")

elif "mug" in question.lower():
    for product in products:
        if "Mug" in product["name"]:
            print(f"Bizzne: Our {product['name']} costs Rs. {product['price']}.")

else:
    print("Bizzne: Sorry, I'm still learning.")