# Store inventory dictionary
store_inventory = {
    "Laptop": {"quantity": 5, "price": 1200},
    "Mouse": {"quantity": 25, "price": 20},
    "Keyboard": {"quantity": 15, "price": 45}
}

print("--- Inventory Items and Quantities ---")
for item, details in store_inventory.items():
    print(f"Item: {item}, Quantity: {details['quantity']}")

print("\n--- Total Value of Inventory (Quantity * Price) ---")
for item, details in store_inventory.items():
    total_value = details["quantity"] * details["price"]
    print(f"Item: {item}, Total Value: ${total_value}")