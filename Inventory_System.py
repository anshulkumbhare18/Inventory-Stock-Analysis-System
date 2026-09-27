"""
Inventory Stock Analysis System
Python Programming Lab (N-PCCCD304P) - Experiential Learning Utility

Phase 2: Core functions implemented with real logic (add, update, sell,
alert, view). NumPy/Pandas based summary report will be completed in Phase 3.
"""

import json
import os

# File where inventory data is permanently stored
INVENTORY_FILE = "inventory_data.json"

# Inventory is stored as a list of dictionaries (our "array" of records)
inventory = []


def load_data():
    """Load inventory data from file at program start."""
    global inventory
    if os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, "r") as f:
            inventory = json.load(f)
        print(f"Loaded {len(inventory)} item(s) from {INVENTORY_FILE}")
    else:
        inventory = []
        print("No existing data found. Starting with an empty inventory.")


def save_data():
    """Save the current inventory back to the file."""
    with open(INVENTORY_FILE, "w") as f:
        json.dump(inventory, f, indent=4)


def find_item(name):
    """Helper: return the item dict matching name (case-insensitive), or None."""
    for item in inventory:
        if item["name"].lower() == name.lower():
            return item
    return None


def add_item():
    """Add a new item to the inventory."""
    name = input("Enter item name: ").strip()

    if find_item(name):
        print(f"'{name}' already exists. Use 'Update Stock' to change its quantity.")
        return

    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per unit: "))
        threshold = int(input("Enter restock threshold: "))
    except ValueError:
        print("Invalid input. Quantity/threshold must be whole numbers, price must be a number.")
        return

    if quantity < 0 or price < 0 or threshold < 0:
        print("Values cannot be negative.")
        return

    inventory.append({
        "name": name,
        "quantity": quantity,
        "price": price,
        "threshold": threshold,
    })
    save_data()
    print(f"'{name}' added successfully.")


def update_stock():
    """Update quantity when stock is purchased (stock in) or sold (stock out)."""
    name = input("Enter item name to update: ").strip()
    item = find_item(name)

    if not item:
        print(f"'{name}' not found in inventory.")
        return

    print("1. Stock In (Purchase)\n2. Stock Out (Sale)")
    choice = input("Choose an option (1/2): ")

    try:
        qty = int(input("Enter quantity: "))
    except ValueError:
        print("Quantity must be a whole number.")
        return

    if choice == "1":
        item["quantity"] += qty
        print(f"Stock updated. New quantity of '{name}': {item['quantity']}")
    elif choice == "2":
        if qty > item["quantity"]:
            print(f"Cannot remove {qty} units. Only {item['quantity']} in stock.")
            return
        item["quantity"] -= qty
        print(f"Stock updated. New quantity of '{name}': {item['quantity']}")
    else:
        print("Invalid option.")
        return

    save_data()
    check_restock_alert(silent_if_ok=True, only_item=name)


def record_sale():
    """Log a sale transaction and reduce stock accordingly."""
    name = input("Enter item name sold: ").strip()
    item = find_item(name)

    if not item:
        print(f"'{name}' not found in inventory.")
        return

    try:
        qty = int(input("Enter quantity sold: "))
    except ValueError:
        print("Quantity must be a whole number.")
        return

    if qty > item["quantity"]:
        print(f"Cannot sell {qty} units. Only {item['quantity']} in stock.")
        return

    item["quantity"] -= qty
    total = qty * item["price"]
    print(f"Sale recorded: {qty} x '{name}' = Rs. {total:.2f}")

    save_data()
    check_restock_alert(silent_if_ok=True, only_item=name)


def check_restock_alert(silent_if_ok=False, only_item=None):
    """Flag items whose quantity has fallen below their threshold."""
    low_stock = [i for i in inventory if i["quantity"] < i["threshold"]]

    if only_item:
        low_stock = [i for i in low_stock if i["name"].lower() == only_item.lower()]

    if not low_stock:
        if not silent_if_ok:
            print("All items are sufficiently stocked.")
        return

    print("\n--- RESTOCK ALERT ---")
    for i in low_stock:
        print(f"'{i['name']}' is low: {i['quantity']} left (threshold: {i['threshold']})")


def view_inventory():
    """Display all current inventory items (added during development for easier testing)."""
    if not inventory:
        print("Inventory is empty.")
        return

    print(f"\n{'Item':<20}{'Quantity':<12}{'Price':<10}{'Threshold':<10}")
    print("-" * 52)
    for i in inventory:
        print(f"{i['name']:<20}{i['quantity']:<12}{i['price']:<10}{i['threshold']:<10}")


def generate_summary():
    """Use NumPy/Pandas to compute and display stock statistics."""
    print("Summary report will be added in Phase 3 using NumPy and Pandas.")


def display_menu():
    """Print the main menu options."""
    print("\n===== Inventory Stock Analysis System =====")
    print("1. Add Item")
    print("2. Update Stock")
    print("3. Record Sale")
    print("4. Check Restock Alerts")
    print("5. View Inventory")
    print("6. Generate Summary Report")
    print("7. Exit")


def main():
    """Entry point: loads data, shows the menu in a loop, routes user choice."""
    load_data()

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_item()
        elif choice == "2":
            update_stock()
        elif choice == "3":
            record_sale()
        elif choice == "4":
            check_restock_alert()
        elif choice == "5":
            view_inventory()
        elif choice == "6":
            generate_summary()
        elif choice == "7":
            save_data()
            print("Exiting... Data saved.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()