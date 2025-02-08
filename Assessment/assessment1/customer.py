import json

fruit_stock = {}

def load_data():
    """Load fruit stock data from JSON file."""
    global fruit_stock
    try:
        with open('fruit_stock.json', 'r') as file:
            fruit_stock = json.load(file)
    except FileNotFoundError:
        fruit_stock = {}

def view_fruit_stock():
    """View all available fruit stock."""
    print("VIEW FRUIT STOCK")
    #checking availabilty 
    if fruit_stock:
        print(fruit_stock)
    else:
        print("Not Available Fruit Stock.")
def run_customer_module():
    """Run the customer interface."""
    load_data()  # Load existing data at the start
    while True:
        print("\n--Customer Menu--")
        print("1. View Fruit")
        print("2. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            view_fruit_stock()
        elif choice == '2':
            print("Exiting the customer module.")
            break
        else:
            print("Invalid choice. Please try again.")

        user_input = input("Do you want to perform more operations? Press 'y' for yes and 'n' for no: ").strip()
        if user_input == 'n':
            print("Thank you for using the fruit market.")
            break
    if __name__ == "__main__":
     run_customer_module()