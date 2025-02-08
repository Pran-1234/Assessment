# Import the necessary functions from the modules
from fruit_manager import run_manager_module
from customer import run_customer_module

def main():
    """Main entry point for the Fruit Store Console Application."""
    while True:
        print("\n--Fruit Store Application--")
        print("1. Manager Module")
        print("2. Customer Module")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            run_manager_module()  # Call the manager module function
        elif choice == '2':
            run_customer_module()  # Call the customer module function
        elif choice == '3':
            print("Exiting the application. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()