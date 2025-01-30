def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def main():
    while True:
        print("\nSimple Calculator")
        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")
        
        if choice in ['1', '2', '3', '4']:
            num1 = input("Enter first number: ")
            num2 = input("Enter second number: ")
            
            # Check if inputs are valid numbers
            if num1.replace('.', '', 1).isdigit() and num2.replace('.', '', 1).isdigit():
                num1 = float(num1)
                num2 = float(num2)
                
                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
            else:
                print("Invalid input! Please enter numeric values.")
        
        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()