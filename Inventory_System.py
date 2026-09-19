"""
Inventory Stock Analysis System
Python Programming Lab (N-PCCCD304P) - Experiential Learning Utility

Phase 1: Menu skeleton with empty function stubs.
Actual logic will be filled in during Phase 2 and Phase 3.
"""

import json
import os

# File where inventory data will be permanently stored
INVENTORY_FILE = "inventory_data.json"

# Inventory is stored as a list of dictionaries (our "array" of records)
# Example of one record once filled in:
# {"name": "Notebook", "quantity": 50, "price": 40, "threshold": 10}
inventory = []


def load_data():
    """Load inventory data from file at program start."""
    pass  # to be implemented in Phase 2


def save_data():
    """Save the current inventory back to the file."""
    pass  # to be implemented in Phase 2


def add_item():
    """Add a new item to the inventory."""
    pass  # to be implemented in Phase 2


def update_stock():
    """Update quantity when stock is purchased (stock in) or sold (stock out)."""
    pass  # to be implemented in Phase 2


def record_sale():
    """Log a sale transaction and reduce stock accordingly."""
    pass  # to be implemented in Phase 2


def check_restock_alert():
    """Flag items whose quantity has fallen below their threshold."""
    pass  # to be implemented in Phase 2


def generate_summary():
    """Use NumPy/Pandas to compute and display stock statistics."""
    pass  # to be implemented in Phase 3


def display_menu():
    """Print the main menu options."""
    print("\n===== Inventory Stock Analysis System =====")
    print("1. Add Item")
    print("2. Update Stock")
    print("3. Record Sale")
    print("4. Check Restock Alerts")
    print("5. Generate Summary Report")
    print("6. Exit")


def main():
    """Entry point: loads data, shows the menu in a loop, routes user choice."""
    load_data()

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_item()
        elif choice == "2":
            update_stock()
        elif choice == "3":
            record_sale()
        elif choice == "4":
            check_restock_alert()
        elif choice == "5":
            generate_summary()
        elif choice == "6":
            save_data()
            print("Exiting... Data saved.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()