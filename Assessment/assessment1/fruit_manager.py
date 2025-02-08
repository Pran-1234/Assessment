import json
import logging

# Logging configuration
LOG_FILE = "transaction.log"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(message)s')

# Global variable for fruit stock
fruit_stock = {}

def log_transaction(message):
    """Log transaction details."""
    logging.info(message)

def load_data():
    """Load fruit stock data from JSON file."""
    global fruit_stock
    try:
        with open('fruit_stock.json', 'r') as file:
            fruit_stock = json.load(file)
    except FileNotFoundError:
        fruit_stock = {}

def save_data():
    """Save fruit stock data to JSON file."""
    with open('fruit_stock.json', 'w') as file:
        json.dump(fruit_stock, file)

def add_fruit_stock():
    """Add fruit stock to the inventory."""
    print("ADD FRUIT STOCK")
    fruit_name = input("Enter fruit name to the stock: ")
    while True:
        try:
            qty = int(input("Enter the quantity in kg: "))
            price = float(input("Enter the price for kg: "))
            break
        except ValueError:
            print("Invalid input. Please enter the proper number or value.")
    
    fruit_stock[fruit_name] = {'qty': qty, 'price': price}
    save_data()
    log_transaction(f"Added {fruit_name}: {qty} kg @ ${price} per kg")
    print(f"{fruit_name} added to the stock.")

def view_fruit_stock():
    """View all available fruit stock."""
    print("VIEW FRUIT STOCK")
    if fruit_stock:
        for fruit, details in fruit_stock.items():
            print(f"{fruit}: {details['qty']} kg @ ${details['price']} per kg")
    else:
        print("Not Available Fruit Stock.")

def update_fruit_stock():
    """Update the quantity and price of a specific fruit."""
    print("UPDATE FRUIT STOCK")
    fruit_name = input("Enter the fruit name to be updated: ")
    if fruit_name in fruit_stock:
        while True:
            try:
                new_qty = int(input("Enter the new quantity: "))
                new_price = float(input("Enter the new price: "))
                fruit_stock[fruit_name]['qty'] = new_qty
                fruit_stock[fruit_name]['price'] = new_price
                save_data()
                log_transaction(f"Updated {fruit_name}: {new_qty} kg @ ${new_price} per kg")
                print(f"{fruit_name} stock updated successfully.")
                return
            except ValueError:
                print("Invalid input. Please enter a proper number.")
    else:
        print(f"{fruit_name} not found in stock.")

def run_manager_module():
    """Run the manager interface."""
    load_data()  # Load existing data at the start
    while True:
        print("\n--Manager Menu--")
        print("1. Add Fruit Stock")
        print("2. View Fruit Stock")
        print("3. Update Fruit Stock")
        print("4. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            add_fruit_stock()
        elif choice == '2':
            view_fruit_stock()
        elif choice == '3':
            update_fruit_stock()
        elif choice == '4':
            print("Exiting the manager module.")
            break
        user_input = input("Do you want to perform more operations? Press 'y' for yes and 'n' for no: ").strip()
        if user_input == 'n':
            print("Thank you for using the fruit market.")
            break
        else:
            print("Invalid choice. Please try again.")
        if __name__ == "__main__":
         run_manager_module()
