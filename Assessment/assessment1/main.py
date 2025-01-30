from fruit_manager import Fruit_Manager
from customer import Customer
def main():
    print("WELCOME TO THE FRUIT MARKET ")
    print("1) Manager")
    print("2) Customer")
    
    role=input("Select Your role:")

    if role =="1":
        fruit_manager = Fruit_Manager()
        fruit_manager.run1()
    
    elif role == "2":
        customer=Customer()
        customer.run2()
    
    else:
        print("Invalid role selected")
    
main()
               
    