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

# DELETE an item by ID
def delete_product(product_id):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id=?", (product_id,))
    conn.commit()
    conn.close()
    print(f"Product ID {product_id} deleted.")

# AGGREGATE function - getting the total cost of the inventory
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

if __name__ == "__main__":
    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. View Inventory")
        print("3. Update Quantity")
        print("4. Delete Product")
        print("5. Calculate Total Inventory Value")
        print("6. Exit")
        
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            add_product(name, quantity, price)

        elif choice == "2":
            view_inventory()

        elif choice == "3":
            product_id = int(input("Enter product ID: "))
            quantity_change = int(input("Enter quantity change (+ for restock, - for sale): "))
            update_quantity(product_id, quantity_change)

        elif choice == "4":
            product_id = int(input("Enter product ID to delete: "))
            delete_product(product_id)

        elif choice == "5":
            calculate_total()

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please select a valid option.")
