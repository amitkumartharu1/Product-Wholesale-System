from datetime import datetime  # Import to get current date and time for invoice filenames and timestamps

# ----------------------------
# this function to write all products to a file 
# ----------------------------
def write_products(products_list, products_file="products.txt"):
    # Open the file in write mode
    with open(products_file, "w") as file:
        for p in products_list:
            # Convert product data to comma-separated string
            line = str(p[0]) + ", " + str(p[1]) + ", " + str(p[2]) + ", " + str(p[3]) + ", " + str(p[4]) + ", " + str(p[5]) + "\n"
            file.write(line)  # Write each product line to the file


# ----------------------------
# this function to create a sales invoice for the customer
# ----------------------------
def invoice(customer_name, sold_items, total_cost):
    # this line create a unique filename using customer name and current time
    date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = "sales_invoice_" + customer_name + "_" + date_str + ".txt"

    # This line Start building the invoice content
    content = "SALES INVOICE\n"
    content += "Date: " + str(datetime.now()) + "\n"
    content += "Customer: " + customer_name + "\n\n"

    # this line Create table headers
    content += "Product             Brand           Qty Sold  Free     Price\n"
    content += "-" * 70 + "\n"

    #this line Add sold product details
    for name, brand, qty, free, line_total in sold_items:
        line = name.ljust(20)         # Left-align product name
        line += brand.ljust(15)       # Left-align brand
        line += str(qty).ljust(10)    # Quantity sold
        line += str(free).ljust(8)    # Free quantity
        line += str(round(line_total, 2)).ljust(12)  # Price rounded to 2 decimals
        content += line + "\n"        # Add this line to content

    #this line Add total cost at the end
    content += "\nTotal Amount: Rs. " + str(round(total_cost, 2)) + "\n"

    # Write the content to the invoice file
    with open(filename, "w") as f:
        f.write(content)

    # Print the invoice content and confirmation message
    print("\n" + content)
    print("Invoice created: " + filename)


# ----------------------------
# this function to create a restock invoice for the supplier
# ----------------------------
def restock_invoice(vendor_name, restocked_items, total_cost):
    # this line create unique filename using vendor name and timestamp
    date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = "restock_invoice_" + vendor_name + "_" + date_str + ".txt"

    # Start building restock invoice content
    content = "RESTOCK INVOICE\n"
    content += "Date: " + str(datetime.now()) + "\n"
    content += "Supplier: " + vendor_name + "\n\n"

    # this line Create table headers
    content += "Product             Brand           Qty       Cost/Item\n"
    content += "-" * 60 + "\n"

    # this line Add restocked product details
    for name, brand, qty, cost in restocked_items:
        line = name.ljust(20)            # Product name
        line += brand.ljust(15)          # Brand
        line += str(qty).ljust(10)       # Quantity added
        line += str(round(cost, 2)).ljust(12)  # Cost per item
        content += line + "\n"           # Add this line to content

    #Add total cost at the end
    content += "\nTotal Amount: Rs. " + str(round(total_cost, 2)) + "\n"

    # Write content to file
    with open(filename, "w") as f:
        f.write(content)

    # Print invoice content and confirmation
    print("\n" + content)
    print("Restock invoice created: " + filename)
