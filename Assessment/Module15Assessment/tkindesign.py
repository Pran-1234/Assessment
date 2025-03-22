import tkinter as tk
from tkinter import messagebox, ttk
from businesslogic import ProductManager, Customer

class ProductManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Product Management System")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f0f0")
        self.logged_in_manager = None
        self.logged_in_customer = None
        self.show_main_menu()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_main_menu(self):
        self.clear_window()
        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.pack(expand=True)
        tk.Label(frame, text="Welcome to Product Management System", font=("Helvetica", 18, "bold"), bg="#f0f0f0").pack(pady=20)
        tk.Button(frame, text="Product Manager", font=("Helvetica", 12), width=20, command=self.manager_menu, bg="#4CAF50", fg="white").pack(pady=10)
        tk.Button(frame, text="Customer", font=("Helvetica", 12), width=20, command=self.customer_menu, bg="#2196F3", fg="white").pack(pady=10)
        tk.Button(frame, text="Exit", font=("Helvetica", 12), width=20, command=self.root.quit, bg="#f44336", fg="white").pack(pady=10)

    def manager_menu(self):
        self.clear_window()
        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.pack(expand=True)
        tk.Label(frame, text="Manager Menu", font=("Helvetica", 16, "bold"), bg="#f0f0f0").pack(pady=20)
        tk.Button(frame, text="Register", font=("Helvetica", 12), width=20, command=self.manager_register, bg="#4CAF50", fg="white").pack(pady=10)
        tk.Button(frame, text="Login", font=("Helvetica", 12), width=20, command=self.manager_login, bg="#2196F3", fg="white").pack(pady=10)
        tk.Button(frame, text="Back", font=("Helvetica", 12), width=20, command=self.show_main_menu, bg="#f44336", fg="white").pack(pady=10)

    def customer_menu(self):
        self.clear_window()
        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.pack(expand=True)
        tk.Label(frame, text="Customer Menu", font=("Helvetica", 16, "bold"), bg="#f0f0f0").pack(pady=20)
        tk.Button(frame, text="Register", font=("Helvetica", 12), width=20, command=self.customer_register, bg="#4CAF50", fg="white").pack(pady=10)
        tk.Button(frame, text="Login", font=("Helvetica", 12), width=20, command=self.customer_login, bg="#2196F3", fg="white").pack(pady=10)
        tk.Button(frame, text="Back", font=("Helvetica", 12), width=20, command=self.show_main_menu, bg="#f44336", fg="white").pack(pady=10)

    def manager_register(self):
        self.form_window("Manager Registration", ProductManager)

    def customer_register(self):
        self.form_window("Customer Registration", Customer)

    def form_window(self, title, user_class):
        win = tk.Toplevel(self.root)
        win.title(title)
        win.geometry("400x500")
        win.configure(bg="#f0f0f0")
        frame = tk.Frame(win, bg="#f0f0f0")
        frame.pack(pady=20, padx=20, expand=True)
        tk.Label(frame, text=title, font=("Helvetica", 16, "bold"), bg="#f0f0f0").grid(row=0, column=0, columnspan=2, pady=10)
        fields = ["Name", "Contact", "Email", "Password"]
        entries = {}
        for i, field in enumerate(fields):
            tk.Label(frame, text=f"{field} *", font=("Helvetica", 12), bg="#f0f0f0").grid(row=i+1, column=0, pady=10, sticky="e")
            entry = tk.Entry(frame, font=("Helvetica", 12), width=25)
            if field == "Password":
                entry.config(show="*")
            entry.grid(row=i+1, column=1, pady=10)
            entries[field] = entry
        tk.Button(frame, text="Register", font=("Helvetica", 12), command=lambda: self.register(user_class, entries, win), bg="#4CAF50", fg="white").grid(row=len(fields)+1, column=0, columnspan=2, pady=20)

    def register(self, user_class, entries, win):
        user = user_class(
            entries["Name"].get(),
            entries["Contact"].get(),
            entries["Email"].get(),
            entries["Password"].get()
        )
        result = user.register()
        if result is True:
            messagebox.showinfo("Success", "Registration successful!", parent=win)
            win.destroy()
        else:
            messagebox.showerror("Error", result, parent=win)

    def manager_login(self):
        win = tk.Toplevel(self.root)
        win.title("Manager Login")
        win.geometry("400x300")
        win.configure(bg="#f0f0f0")
        frame = tk.Frame(win, bg="#f0f0f0")
        frame.pack(pady=20, padx=20, expand=True)
        tk.Label(frame, text="Manager Login", font=("Helvetica", 16, "bold"), bg="#f0f0f0").grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(frame, text="Email *", font=("Helvetica", 12), bg="#f0f0f0").grid(row=1, column=0, pady=10, sticky="e")
        email_entry = tk.Entry(frame, font=("Helvetica", 12), width=25)
        email_entry.grid(row=1, column=1, pady=10)
        tk.Label(frame, text="Password *", font=("Helvetica", 12), bg="#f0f0f0").grid(row=2, column=0, pady=10, sticky="e")
        password_entry = tk.Entry(frame, font=("Helvetica", 12), show="*", width=25)
        password_entry.grid(row=2, column=1, pady=10)
        tk.Button(frame, text="Login", font=("Helvetica", 12), command=lambda: self.validate_manager_login(email_entry.get(), password_entry.get(), win), bg="#2196F3", fg="white").grid(row=3, column=0, columnspan=2, pady=20)

    def validate_manager_login(self, email, password, win):
        manager = ProductManager("", "", email, password)
        if manager.login(email, password):
            self.logged_in_manager = manager
            messagebox.showinfo("Success", "Login successful!", parent=win)
            win.destroy()
            self.manager_dashboard()
        else:
            messagebox.showerror("Error", "Invalid email or password!", parent=win)

    def customer_login(self):
        win = tk.Toplevel(self.root)
        win.title("Customer Login")
        win.geometry("400x300")
        win.configure(bg="#f0f0f0")
        frame = tk.Frame(win, bg="#f0f0f0")
        frame.pack(pady=20, padx=20, expand=True)
        tk.Label(frame, text="Customer Login", font=("Helvetica", 16, "bold"), bg="#f0f0f0").grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(frame, text="Email *", font=("Helvetica", 12), bg="#f0f0f0").grid(row=1, column=0, pady=10, sticky="e")
        email_entry = tk.Entry(frame, font=("Helvetica", 12), width=25)
        email_entry.grid(row=1, column=1, pady=10)
        tk.Label(frame, text="Password *", font=("Helvetica", 12), bg="#f0f0f0").grid(row=2, column=0, pady=10, sticky="e")
        password_entry = tk.Entry(frame, font=("Helvetica", 12), show="*", width=25)
        password_entry.grid(row=2, column=1, pady=10)
        tk.Button(frame, text="Login", font=("Helvetica", 12), command=lambda: self.validate_customer_login(email_entry.get(), password_entry.get(), win), bg="#2196F3", fg="white").grid(row=3, column=0, columnspan=2, pady=20)

    def validate_customer_login(self, email, password, win):
        customer = Customer("", "", email, password)
        if customer.login(email, password):
            self.logged_in_customer = customer
            messagebox.showinfo("Success", "Login successful!", parent=win)
            win.destroy()
            self.customer_dashboard()
        else:
            messagebox.showerror("Error", "Invalid email or password!", parent=win)

    def manager_dashboard(self):
        self.clear_window()
        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.pack(expand=True)
        tk.Label(frame, text="Product Manager Dashboard", font=("Helvetica", 18, "bold"), bg="#f0f0f0").pack(pady=20)
        tk.Button(frame, text="Add Product", font=("Helvetica", 12), width=20, command=self.add_product_form, bg="#4CAF50", fg="white").pack(pady=10)
        tk.Button(frame, text="View Stocks", font=("Helvetica", 12), width=20, command=self.view_stocks, bg="#2196F3", fg="white").pack(pady=10)
        tk.Button(frame, text="Logout", font=("Helvetica", 12), width=20, command=self.logout, bg="#f44336", fg="white").pack(pady=10)

    def customer_dashboard(self):
        self.clear_window()
        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.pack(expand=True)
        tk.Label(frame, text="Customer Dashboard", font=("Helvetica", 18, "bold"), bg="#f0f0f0").pack(pady=20)
        tk.Button(frame, text="Purchase Stock", font=("Helvetica", 12), width=20, command=self.purchase_stock_form, bg="#4CAF50", fg="white").pack(pady=10)
        tk.Button(frame, text="View Orders", font=("Helvetica", 12), width=20, command=self.view_orders, bg="#2196F3", fg="white").pack(pady=10)
        tk.Button(frame, text="Logout", font=("Helvetica", 12), width=20, command=self.logout, bg="#f44336", fg="white").pack(pady=10)

    def add_product_form(self):
        win = tk.Toplevel(self.root)
        win.title("Add Product")
        win.geometry("400x400")
        win.configure(bg="#f0f0f0")
        frame = tk.Frame(win, bg="#f0f0f0")
        frame.pack(pady=20, padx=20, expand=True)
        tk.Label(frame, text="Add Product", font=("Helvetica", 16, "bold"), bg="#f0f0f0").grid(row=0, column=0, columnspan=2, pady=10)
        fields = ["Name", "Stock", "Price"]
        entries = {}
        for i, field in enumerate(fields):
            tk.Label(frame, text=f"{field} *", font=("Helvetica", 12), bg="#f0f0f0").grid(row=i+1, column=0, pady=10, sticky="e")
            entries[field] = tk.Entry(frame, font=("Helvetica", 12), width=25)
            entries[field].grid(row=i+1, column=1, pady=10)
        tk.Button(frame, text="Add", font=("Helvetica", 12), command=lambda: self.add_product(entries, win), bg="#4CAF50", fg="white").grid(row=len(fields)+1, column=0, columnspan=2, pady=20)

    def add_product(self, entries, win):
        name = entries["Name"].get()
        stock = entries["Stock"].get()
        price = entries["Price"].get()
        if not all([name, stock, price]):
            messagebox.showerror("Error", "Fill all fields!", parent=win)
            return
        try:
            stock = int(stock)
            price = float(price)
            if self.logged_in_manager.add_product(name, stock, price):
                messagebox.showinfo("Success", "Product added successfully!", parent=win)
                win.destroy()
            else:
                messagebox.showerror("Error", "Failed to add product!", parent=win)
        except ValueError:
            messagebox.showerror("Error", "Stock must be an integer and Price must be a number!", parent=win)

    def view_stocks(self):
        stocks = self.logged_in_manager.view_stocks()
        win = tk.Toplevel(self.root)
        win.title("Product Stocks")
        win.geometry("500x400")
        win.configure(bg="#f0f0f0")
        frame = tk.Frame(win, bg="#f0f0f0")
        frame.pack(pady=20, padx=20, fill="both", expand=True)
        tk.Label(frame, text="Product Stocks", font=("Helvetica", 16, "bold"), bg="#f0f0f0").pack(pady=10)
        tree = ttk.Treeview(frame, columns=("ID", "Name", "Stock", "Price"), show="headings", height=10)
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("Stock", text="Stock")
        tree.heading("Price", text="Price")
        tree.column("ID", width=50)
        tree.column("Name", width=150)
        tree.column("Stock", width=100)
        tree.column("Price", width=100)
        for stock in stocks:
            tree.insert("", "end", values=stock)
        tree.pack(fill="both", expand=True)
        tk.Button(frame, text="Close", font=("Helvetica", 12), command=win.destroy, bg="#f44336", fg="white").pack(pady=10)

    def purchase_stock_form(self):
        win = tk.Toplevel(self.root)
        win.title("Purchase Stock")
        win.geometry("400x300")
        win.configure(bg="#f0f0f0")
        frame = tk.Frame(win, bg="#f0f0f0")
        frame.pack(pady=20, padx=20, expand=True)
        tk.Label(frame, text="Purchase Stock", font=("Helvetica", 16, "bold"), bg="#f0f0f0").grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(frame, text="Product ID *", font=("Helvetica", 12), bg="#f0f0f0").grid(row=1, column=0, pady=10, sticky="e")
        product_id_entry = tk.Entry(frame, font=("Helvetica", 12), width=25)
        product_id_entry.grid(row=1, column=1, pady=10)
        tk.Label(frame, text="Quantity *", font=("Helvetica", 12), bg="#f0f0f0").grid(row=2, column=0, pady=10, sticky="e")
        quantity_entry = tk.Entry(frame, font=("Helvetica", 12), width=25)
        quantity_entry.grid(row=2, column=1, pady=10)
        tk.Button(frame, text="Purchase", font=("Helvetica", 12), command=lambda: self.purchase_stock(product_id_entry.get(), quantity_entry.get(), win), bg="#4CAF50", fg="white").grid(row=3, column=0, columnspan=2, pady=20)

    def purchase_stock(self, product_id, quantity, win):
        if not all([product_id, quantity]):
            messagebox.showerror("Error", "Fill all fields!", parent=win)
            return
        try:
            product_id = int(product_id)
            quantity = int(quantity)
            result = self.logged_in_customer.purchase_stock(product_id, quantity)
            if "successful" in result:
                messagebox.showinfo("Success", result, parent=win)
                win.destroy()
            else:
                messagebox.showerror("Error", result, parent=win)
        except ValueError:
            messagebox.showerror("Error", "Product ID and Quantity must be integers!", parent=win)

    def view_orders(self):
        orders = self.logged_in_customer.view_orders()
        win = tk.Toplevel(self.root)
        win.title("Your Orders")
        win.geometry("500x400")
        win.configure(bg="#f0f0f0")
        frame = tk.Frame(win, bg="#f0f0f0")
        frame.pack(pady=20, padx=20, fill="both", expand=True)
        tk.Label(frame, text="Your Orders", font=("Helvetica", 16, "bold"), bg="#f0f0f0").pack(pady=10)
        tree = ttk.Treeview(frame, columns=("Name", "Quantity", "Total"), show="headings", height=10)
        tree.heading("Name", text="Product Name")
        tree.heading("Quantity", text="Quantity")
        tree.heading("Total", text="Total")
        tree.column("Name", width=200)
        tree.column("Quantity", width=100)
        tree.column("Total", width=100)
        for order in orders:
            tree.insert("", "end", values=order)
        tree.pack(fill="both", expand=True)
        tk.Button(frame, text="Close", font=("Helvetica", 12), command=win.destroy, bg="#f44336", fg="white").pack(pady=10)

    def logout(self):
        self.logged_in_manager = None
        self.logged_in_customer = None
        self.show_main_menu()

if __name__ == "__main__":
    root = tk.Tk()
    app = ProductManagementApp(root)
    root.mainloop()