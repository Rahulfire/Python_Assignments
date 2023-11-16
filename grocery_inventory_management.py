# Initialize an empty inventory dictionary
inventory = {}

# Function to add items to the inventory
def add_item(item_name, quantity):
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity
    print(f"{quantity} {item_name}(s) added to inventory.")

# Function to update item quantity
def update_item(item_name, new_quantity):
    if item_name in inventory:
        inventory[item_name] = new_quantity
        print(f"Quantity of {item_name} updated to {new_quantity}.")
    else:
        print(f"{item_name} not found in inventory.")

# Function to display the inventory
def display_inventory():
    print("Current Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

# Main loop for user interaction
while True:
    print("\nWhat would you like to do?")
    print("1. Add item to inventory")
    print("2. Update item quantity")
    print("3. Display inventory")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        item = input("Enter item name: ")
        qty = int(input("Enter quantity to add: "))
        add_item(item, qty)
    elif choice == '2':
        item = input("Enter item name: ")
        qty = int(input("Enter new quantity: "))
        update_item(item, qty)
    elif choice == '3':
        display_inventory()
    elif choice == '4':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
