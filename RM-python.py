TAX_RATE = 0.08 # Sales tax rate
MAX_ITEMS = 100 # Maximum number of menu items

# Class for a menu item
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Class for an order item
class OrderItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Function to edit the menu
def edit_menu(menu):
    while True:
        print("\nMenu editor:")
        print("1. Add item")
        print("2. Delete item")
        print("3. Display menu")
        print("4. Return to main menu")
        choice = input("Enter choice: ")

        if choice == "1":
            add_item(menu)
        elif choice == "2":
            delete_item(menu)
        elif choice == "3":
            display_menu(menu)
        elif choice == "4":
            return
        else:
            print("Invalid choice.")

# Function to add a menu item
def add_item(menu):
    if len(menu) == MAX_ITEMS:
        print("Menu is full.")
    else:
        name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        menu.append(Item(name, price))

# Function to delete a menu item
def delete_item(menu):
    name = input("Enter item name: ")
    for i, item in enumerate(menu):
        if item.name == name:
            del menu[i]
            return
    print("Item not found.")

# Function to display the menu
def display_menu(menu):
    print("\nMenu:")
    for item in menu:
        print(f"{item.name}\t${item.price:.2f}")

# Function to place an order
def place_order(menu):
    order = []
    while True:
        name = input("Enter item name (or 'done' to quit): ")
        if name == "done":
            break
        found = False
        for item in menu:
            if item.name == name:
                order.append(OrderItem(item.name, item.price))
                found = True
                break
        if not found:
            print("Item not found.")
    edit_order(order)
    print_bill(order)

# Function to edit the order
def edit_order(order):
    while True:
        print("\nOrder editor:")
        print("1. Add item")
        print("2. Delete item")
        print("3. Display order")
        print("4. Return to main menu")
        choice = input("Enter choice: ")

        if choice == "1":
            add_order_item(order)
        elif choice == "2":
            delete_order_item
