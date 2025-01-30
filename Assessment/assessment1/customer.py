import json
class Customer:
    def __init__(self):
        self.fruit_stock = {}
        self.load_data()

    def load_data(self):
        try:
            with open('fruit_stock.json','r') as file:
                self.fruit_stock = json.load(file)
        except FileNotFoundError:
            self.fruit_stock={}
    
    def view_fruit_stock(self):
        print("VIEW FRUIT STOCK")
        if  self.fruit_stock:
            print(self.fruit_stock)
        else:
            print("Not Available Fruit Stock:")
          
    def run2(self):
        while True:
            print("\n--Customer menu")
            print("1 View Fruit")
            print("2 Exit")
            choice = input("Select an option:")
            if choice == '1':
                self.view_fruit_stock()
            elif choice == '2':
                print("Exiting the customer module")
           
            else:
                print("Invalid choice.Please Try again")
            user_input= input("Do you want to perform more operations? Press 'y' for yes and 'n' for no:").strip()
            if user_input =='n':
                print("Thank you for using the fruit market ")
                exit()