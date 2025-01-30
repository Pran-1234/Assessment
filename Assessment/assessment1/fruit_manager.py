import json
import logging

class Fruit_Manager:
    LOG_FILE = "transaction.log"
    logging.basicConfig(filename=LOG_FILE,level=logging.INFO,format='%(asctime)s -%(message)s')
    
    def log_transaction(message):
        logging.info(message)

    def __init__(self):
        self.fruit_stock={}
        self.load_data()
        
    def load_data(self):
        try:
            with open('fruit_stock.json','r') as file:
                self.fruit_stock = json.load(file)
        except FileNotFoundError:
            self.fruit_stock ={}


    def save_data(self):
        with open('fruit_stock.json','w') as file:
            json.dump(self.fruit_stock,file)
    def add_fruit_stock(self):
        print("ADD FRUIT STOCK")
        fruit_name=input("Enter fruit name to the stock:")
        while True:
            try:
                qty=int(input("Enter the quantity in kg:"))
                price = float(input("Enter the price for kg:"))
                break
            except ValueError:
                print("Invalid input.please enter the proper number or value")
        self.fruit_stock[fruit_name]= {'qty':qty,'price':price}
        self.save_data()
        Fruit_Manager.log_transaction(f"Added {fruit_name}:{qty} kg {price} kg ")
        print(f" {fruit_name} added to the stock.")

        
    
    def view_fruit_stock(self):
       print("VIEW FRUIT STOCK")
       if  self.fruit_stock:
        print(self.fruit_stock)
       else:
         print("No Current fruit stock")
            
         
    def update_fruit_stock(self):
        print("UPDATE FRUIT STOCK")
        fruit_name=input("Enter the fruit name to be updated:")
        if fruit_name in self.fruit_stock:
            while True:
                try:
                    new_qty=int(input("enter the quantity to be updated:"))
                    new_price=int(input("enter new price:"))
                    self.fruit_stock[fruit_name]['qty'] = new_qty
                    self.fruit_stock[fruit_name]['price'] = new_price
                    self.save_data()
                    Fruit_Manager.log_transaction(f"Updated {fruit_name}:{new_qty} kg @ ${new_price} kg")
                    print(f"{fruit_name} stock updated successfully")
                    return
                except ValueError:
                    print("Invalid input.Please enter a proper number")
    def run1(self):
        while True:
            print("\n----Manager menu----")
            print("1 Add fruit stock")
            print("2 View fruit stock")
            print("3 Update Fruit Stock")
            print("4 Exit")
            choice=input("Enter your choice:")
            if choice=='1':
                self.add_fruit_stock()
            elif choice=='2':
                self.view_fruit_stock()
            elif choice=='3':
                self.update_fruit_stock()
            
            elif choice=='4':
                print("Exiting the manager interface")
            else:
                print("Invalid choice.Please try again")
            
            user_input= input("Do you want to perform more operations? Press 'y' for yes and 'n' for no:").strip()
            if user_input =='n':
                print("Thank you for using the fruit market manager")
                exit()
            
                
        
