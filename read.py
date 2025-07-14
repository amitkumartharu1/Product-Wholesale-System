# File that stores product information
products_file = "products.txt"


# --------------------------------------------
# this function to read product data from a file
# --------------------------------------------
def read_products():
    products = []  # Initialize an empty list to store product details

    # Open the file in read mode
    with open(products_file, "r") as file:
        for line in file:
            # Remove newline and tab characters from the line
            line = line.replace("\n", "").replace("\t", "")
            
            # this line Skip empty lines
            if not line:
                continue

            #clean any newline/tab from each part
            parts = [p.replace("\n", "").replace("\t", "") for p in line.split(",")]

            # Each product line must have exactly 6 values (ID, Name, Brand, Qty, Cost, Country)
            if len(parts) != 6:
                print("Skips line:", line)
                continue

            # Unpack parts into variables
            prod_id, name, brand, qty, cost, country = parts

            try:
                qty = int(qty)        # Convert quantity to integer
                cost = float(cost)    # Convert cost to float
            except ValueError:
                # If conversion fails, print a message and skip this line
                print("Skip to the line with invalid numbers:", line)
                continue

            # Calculate selling price (double the cost)
            selling_price = cost * 2

            # Append the product data to the products list
            products.append([
                prod_id,
                name,
                brand,
                qty,
                cost,
                country,
                selling_price
            ])

    # Return the list of products
    return products


# --------------------------------------------
# Function to display the products in a table
# --------------------------------------------
def display_products(products):
    print("\n\nThe Available Products:")

    # Table headers
    headers = ["ID", "Product", "Brand", "Stock", "Selling Price", "Country"]

    # this line Combine headers and product rows
    rows = [headers]  # Add headers as the first row
    for p in products:
        rows.append([
            str(p[0]),               # Product ID
            str(p[1]),               # Product Name
            str(p[2]),               # Brand
            str(p[3]),               # Quantity in stock
            str(round(p[6], 2)),     # Selling price (rounded to 2 decimals)
            str(p[5])                # Country of origin
        ])

    # Calculate max column width for each column
    col_widths = [0] * len(headers)
    for row in rows:
        for i in range(len(row)):
            col_widths[i] = max(col_widths[i], len(row[i]))  # Update max width per column

    # Print each row with proper alignment
    for row in rows:
        line = ""
        for i in range(len(row)):
            item = row[i]
            space = col_widths[i] - len(item) + 2  # Add padding (2 spaces)
            line += item + " " * space
        print(line)

    # Print a separator line below the table
    print("-" * (sum(col_widths) + 2 * len(headers)))  # Adjusted for total width including spaces


# --------------------------------------------
# Driver code and runs when file is executed
# --------------------------------------------
print("=" * 110)             # Print a separator line
product_list = read_products()  # Read all products from file
display_products(product_list)  # Display all products in a table format
