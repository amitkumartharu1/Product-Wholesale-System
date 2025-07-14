# Importing read and display functions from read.py
from read import read_products, display_products  # This line reads the product list and displays it

# Importing write and invoice functions from write.py
from write import write_products, invoice, restock_invoice  # This line saves/updates data and creates invoices

# Load all products from the file into a list
products = read_products()  # Reads products.txt and loads all products into a list

# ---------------------------------------------
# this function to display products using read module
# ---------------------------------------------
def display():
    display_products(products)  # Calls display function to show all available products

# ---------------------------------------------
# Function to restock products from a vendor
# ---------------------------------------------
def restock():
    vendor_name = input("Enter to the vendor name: ")  # Ask for vendor name
    total_cost = 0.0  # To calculate total restock cost
    restocked_items = []  # List to track restocked items for invoice

    while True:
        # Ask for product ID and ensure it's numeric
        while True:
            prod_id = input("Enter the product ID to restock (new ID): ")
            if not prod_id.isdigit():
                print("Product ID must be a number.")
                continue
            break

        # Ask for product name and ensure it's alphabetic (with spaces)
        while True:
            name = input("Enter the product name: ").strip()
            if not all(c.isalpha() or c.isspace() for c in name) or not name:
                print("Product name must contain only letters and spaces.")
                continue
            break

        # Ask for product brand and ensure it's alphabetic (with spaces)
        while True:
            brand = input("Enter the product brand: ").strip()
            if not all(c.isalpha() or c.isspace() for c in brand) or not brand:
                print("Brand must contain only letters and spaces.")
                continue
            break

        # Ask for quantity to add
        while True:
            qty_input = input("Enter quantity to add: ")
            try:
                qty_to_add = int(qty_input)
                if qty_to_add < 1:
                    print("Quantity must be a positive number.")
                    continue
                break
            except ValueError:
                print("Please enter a valid integer for quantity!")

        # Ask for cost per unit
        while True:
            cost_input = input("Enter new cost price per unit: ")
            try:
                cost_price = float(cost_input)
                if cost_price < 0:
                    print("Cost price cannot be negative.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number for cost price!")

        # Ask for country and ensure it's alphabetic (with spaces)
        while True:
            country = input("Enter the Country of origin: ").strip()
            if not all(c.isalpha() or c.isspace() for c in country) or not country:
                print("Country must contain only letters and spaces.")
                continue
            break

        # Add new product to the list
        products.append([prod_id, name, brand, qty_to_add, cost_price, country, cost_price * 2])
        restocked_items.append((name, brand, qty_to_add, cost_price))
        total_cost += qty_to_add * cost_price

        # Ask if vendor wants to restock more items
        if input("Do you want to Restock another product? (yes/no): ").lower() != "yes":
            break

    # this line is created restock invoice and update file
    restock_invoice(vendor_name, restocked_items, total_cost)
    write_products(products)

# ---------------------------------------------
# this function to sell products to customers
# ---------------------------------------------
def sale_products():
    customer_name = input("Enter to the customer name: ")  # Ask customer name for invoice
    print("=" * 110)
    total_amount = 0.0  # Track total bill
    sold_items = []  # List to store sold product info for invoice

    while True:  # Loop to sell multiple products in a single invoice
        display()  # Show available products
        print("=" * 110)

        # Ask for product ID to purchase, ensure numeric and exists
        while True:
            prod_id = input("Enter to the product ID to buy: ")
            if not prod_id.isdigit():
                print("Product ID must be a number.")
                continue

            # Check existence exactly once
            match = None
            for p in products:
                if p[0] == prod_id:
                    match = p
                    break
            if not match:
                print("The Product ID not found.")
                continue
            break

        qty = int(input("Enter to the quantity: "))  # Ask quantity
        print("=" * 110)

        # At this point, 'match' is the product dict/list
        p = match

        # Calculate free items, for every 3 items, customer gets 1 free
        free = qty // 3

        if qty + free > p[3]:
            print("Not enough stock. Requested:", qty + free, "Available:", p[3])
            # go back to choosing product or exit
            if input("Do you want to try a different product? (yes/no): ").lower() != "yes":
                break
            else:
                continue

        # this line Reduce from stock (including free)
        p[3] -= (qty + free)
        line_total = qty * p[6]  # Price without free items
        total_amount += line_total  # Add to total bill

        # Save item to sold list
        sold_items.append((p[1], p[2], qty, free, line_total))

        # this lins Confirmation message
        print("Added to cart: " + str(qty) + "+" + str(free) + " free")

        # Ask if customer wants to buy more items
        if input("Do you want to Sell another product? (yes/no): ").lower() != "yes":
            break

    # this line create and save the invoice
    invoice(customer_name, sold_items, total_amount)
    write_products(products)  # Update the products.txt file
