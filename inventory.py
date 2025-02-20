import sqlite3
from tabulate import tabulate

# CREATE an item
def add_product(name, quantity, price):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)", (name, quantity, price))
    conn.commit()
    conn.close()
    print(f"Product '{name}' added successfully!")

# READ all items
def view_inventory():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()

    if products:
        print(tabulate(products, headers=["ID", "Name", "Quantity", "Price"], tablefmt="grid"))
    else:
        print("No products in inventory.")

# UPDATE an item by ID and quantity
def update_quantity(product_id, quantity_change):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    
    # Fetch current quantity
    cursor.execute("SELECT quantity FROM products WHERE id=?", (product_id,))
    result = cursor.fetchone()
    
    if result:
        new_quantity = result[0] + quantity_change
        if new_quantity < 0:
            print("Error: Not enough stock!")
        else:
            cursor.execute("UPDATE products SET quantity=? WHERE id=?", (new_quantity, product_id))
            conn.commit()
            print(f"Product ID {product_id} updated successfully! New quantity: {new_quantity}")
    else:
        print("Product not found!")
    
    conn.close()

# UPDATE an item by ID and price
def update_price(product_id, price_change):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    # Fetch item price
    cursor.execute("SELECT price FROM products WHERE id=?", (product_id,))
    result = cursor.fetchone()
    
    if result:
        if (price_change < 0):
            print("Price cannot be less than 0.")
        else:
            cursor.execute("UPDATE products SET price=? WHERE id=?", (price_change, product_id))
            conn.commit()
            print(f"Product ID {product_id} updated successfully! New price: {price_change}")
    else:
        print("Product not found!")

# DELETE an item by ID
def delete_product(product_id):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id=?", (product_id,))
    conn.commit()
    conn.close()
    print(f"Product ID {product_id} deleted.")

# AGGREGATE function 1 - getting the total cost of the inventory
def calculate_total():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(quantity * price) FROM products")
    total = cursor.fetchone()[0]
    conn.close()

    if total:
        print(f"Total inventory value is ${total:.2f}")
    else:
        print("Failed to calculate total value.")

# AGGREGATE function 2 - getting out-of-stock inventory using GROUP_CONCAT
def view_oos_items():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT GROUP_CONCAT(name) FROM products WHERE quantity = 0")
    oos = cursor.fetchall()
    conn.close()

    if (oos):
        print(tabulate(oos, headers=["Out-of-stock"], tablefmt="grid"))
    else:
        print("No out-of-stock items in inventory.")

if __name__ == "__main__":
    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. View Inventory")
        print("3. Update Quantity")
        print("4. Update Price")
        print("5. Delete Product")
        print("6. Calculate Total Inventory Value")
        print("7. View out-of-stock Items")
        print("8. Exit")
        
        choice = input("Enter choice: ")

        # Add Product
        if choice == "1":
            name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            add_product(name, quantity, price)

        # View Inventory
        elif choice == "2":
            view_inventory()

        # Update Quantity
        elif choice == "3":
            product_id = int(input("Enter product ID: "))
            quantity_change = int(input("Enter quantity change (+ for restock, - for sale): "))
            update_quantity(product_id, quantity_change)

        # Update Price
        elif choice == "4":
            product_id = int(input("Enter product ID: "))
            price_change = float(input("Enter new price: "))
            update_price(product_id, price_change)

        # Delete Product
        elif choice == "5":
            product_id = int(input("Enter product ID to delete: "))
            delete_product(product_id)

        # Calculate inventory value
        elif choice == "6":
            calculate_total()

        # View out-of-stock items
        elif choice == "7":
            view_oos_items()

        # Exit program
        elif choice == "8":
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please select a valid option.")
