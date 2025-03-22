from database import Database

# Base class for common fields using inheritance
class User:
    def __init__(self, name, contact, email, password):
        self.name = name
        self.contact = contact
        self.email = email
        self._password = password  # Encapsulation

    def validate(self):
        if not all([self.name, self.contact, self.email, self._password]):
            return "Fill all empty fields!"
        if not self.contact.isdigit() or len(self.contact) != 10:
            return "Invalid contact number!"
        return None

# Product Manager class inheriting from User
class ProductManager(User):
    def __init__(self, name, contact, email, password):
        super().__init__(name, contact, email, password)
        self.db = Database()

    def register(self):
        validation = self.validate()
        if validation:
            return validation
        query = "INSERT INTO product_managers (name, contact, email, password) VALUES (%s, %s, %s, %s)"
        return self.db.execute_query(query, (self.name, self.contact, self.email, self._password))

    def login(self, email, password):
        query = "SELECT * FROM product_managers WHERE email = %s AND password = %s"
        result = self.db.fetch_query(query, (email, password))
        return len(result) > 0

    def add_product(self, name, stock, price):
        query = "INSERT INTO products (name, stock, price) VALUES (%s, %s, %s)"
        return self.db.execute_query(query, (name, stock, price))

    def view_stocks(self):
        query = "SELECT * FROM products"
        return self.db.fetch_query(query)

# Customer class inheriting from User
class Customer(User):
    def __init__(self, name, contact, email, password):
        super().__init__(name, contact, email, password)
        self.db = Database()
        self.__balance = 0.0  # Private field

    def register(self):
        validation = self.validate()
        if validation:
            return validation
        query = "INSERT INTO customers (name, contact, email, password, balance) VALUES (%s, %s, %s, %s, %s)"
        return self.db.execute_query(query, (self.name, self.contact, self.email, self._password, self.__balance))

    def login(self, email, password):
        query = "SELECT * FROM customers WHERE email = %s AND password = %s"
        result = self.db.fetch_query(query, (email, password))
        return len(result) > 0

    def purchase_stock(self, product_id, quantity):
        query = "SELECT stock, price FROM products WHERE id = %s"
        product = self.db.fetch_query(query, (product_id,))
        if not product or product[0][0] < quantity:
            return "Insufficient stock!"
        total = product[0][1] * quantity
        if self.__balance < total:
            return "Insufficient balance!"
        self.__balance -= total
        self.db.execute_query("UPDATE customers SET balance = %s WHERE email = %s", (self.__balance, self.email))
        self.db.execute_query("UPDATE products SET stock = stock - %s WHERE id = %s", (quantity, product_id))
        self.db.execute_query("INSERT INTO orders (customer_id, product_id, quantity, total) VALUES (%s, %s, %s, %s)",
                             (self.get_id(), product_id, quantity, total))
        return "Purchase successful!"

    def view_orders(self):
        query = "SELECT p.name, o.quantity, o.total FROM orders o JOIN products p ON o.product_id = p.id WHERE customer_id = %s"
        return self.db.fetch_query(query, (self.get_id(),))

    def get_id(self):
        query = "SELECT id FROM customers WHERE email = %s"
        result = self.db.fetch_query(query, (self.email,))
        if result:
            return result[0][0]
        raise ValueError("Customer ID not found")