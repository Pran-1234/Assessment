import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None
        try:
            # Connect without a database to create it if needed
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",  # Replace with your MySQL username
                password=""   # Replace with your MySQL password if any
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                self.cursor.execute("CREATE DATABASE IF NOT EXISTS product_management")
                print("Database 'product_management' created or already exists")
                self.connection.database = "product_management"  # Switch to the database
                self.create_tables()
                print("Successfully connected to MySQL database")
            else:
                print("Failed to connect to MySQL database")
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
        finally:
            if self.connection and self.connection.is_connected() and not self.connection.database:
                self.cursor.close()
                self.connection.close()

    def create_tables(self):
        if not self.cursor or not self.connection.is_connected():
            print("No database connection available to create tables")
            return
        # Product Managers Table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS product_managers (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                contact VARCHAR(15),
                email VARCHAR(255) UNIQUE,
                password VARCHAR(255)
            )
        """)
        # Customers Table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                contact VARCHAR(15),
                email VARCHAR(255) UNIQUE,
                password VARCHAR(255),
                balance DOUBLE DEFAULT 0.0
            )
        """)
        # Products Table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                stock INT,
                price DOUBLE
            )
        """)
        # Orders Table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INT AUTO_INCREMENT PRIMARY KEY,
                customer_id INT,
                product_id INT,
                quantity INT,
                total DOUBLE,
                FOREIGN KEY (customer_id) REFERENCES customers(id),
                FOREIGN KEY (product_id) REFERENCES products(id)
            )
        """)
        self.connection.commit()
        print("Tables created successfully")

    def execute_query(self, query, params=None):
        if not self.cursor or not self.connection.is_connected():
            print("No database connection available")
            return False
        try:
            self.cursor.execute(query, params or ())
            self.connection.commit()
            return True
        except Error as e:
            print(f"Error executing query: {e}")
            return False

    def fetch_query(self, query, params=None):
        if not self.cursor or not self.connection.is_connected():
            print("No database connection available")
            return []
        try:
            self.cursor.execute(query, params or ())
            return self.cursor.fetchall()
        except Error as e:
            print(f"Error fetching query: {e}")
            return []

    def close(self):
        if self.connection and self.connection.is_connected():
            if self.cursor:
                self.cursor.close()
            self.connection.close()
            print("Database connection closed")

if __name__ == "__main__":
    db = Database()
    db.close()