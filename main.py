import json

order = {"name": "John Doe", "drinks": "coffee", "flavor": "vanilla", "topping": "whipped cream"}

order1 = {
    "name": "John Doe",
    "drinks": "coffee",
    "flavor": "vanilla",
    "topping": "whipped cream"
}

orders = []

orders.append(order)
orders.append(order1)

f = open("orders.json", "w")

json.dump(orders, f, indent=4)

f.close()

saved_orders = []

f = open("orders.json", "r")
saved_orders = json.load(f)

for i, j in enumerate(saved_orders):
    print(f"Order {i + 1}:")
    print(f"Name: {j['name']}")
    print(f"Drink: {j['drinks']}")
    print(f"Flavor: {j['flavor']}")
    print(f"Topping: {j['topping']}")
    print()
