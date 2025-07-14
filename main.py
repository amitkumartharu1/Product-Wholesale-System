# Import required functions from the operation.py file
from operation import display, sale_products, restock  # import display, sale, and restock functions
#------------------------------
# Define the main function.
#------------------------------
def main():  # main part of program starts here. docstring
    """
    The WeCare Store application shows a welcome banner and menu for user interaction.
    Users can display products, sell products, restock products, or leave the program.
    Depending on the user input, the program calls corresponding functions to accomplish those actions.
    It checking to the invalid input and promts to the user to  enter a valid option or chose
    """

    # Displaying store banner and welcome message.
    print("\n\n\t\t\t- Beauty & Skin Care Products -\n")  # Display the store's banner
    print("\t\tKamalpokhari, City Center    Phone_no: +977-9706880338\n")  # Show location and contact
    print("\t\t- Welcome to the WeCare Store Production. -\n")  # Friendly welcome message.
    print("=" * 110)  # Print a divider line

    
    #------------------------------
    # Start the main menu loop
    #------------------------------
    while True:  # This loop will repeat until the user chooses to exit.
        print("=" * 110)
        print("\nOptions:")  # Show the main menu options.
        print("-" * 80)
        print("1. Enter to the Display Products.")  # Option 1 - Show all products
        print("-" * 80)
        print("2. Enter to the Sale a Product.")  # Option 2 - Sell a product
        print("-" * 80)
        print("3. Enter to the Restock Products.")  # Option 3 - Add more stock
        print("-" * 80)
        print("4. Enter to the  Exit.\n")  # Option 4 - Exit the program
        print("=" * 110)

        # Take user input for the selected option
        wish = input("Enter your wish: ")  # Ask the user to enter a number 1-4

        # Call the appropriate function based on user's choice
        if wish == "1":
            display()  # Call display function to show products
        elif wish == "2":
            sale_products()  # Call sale function to sell products.
        elif wish == "3":
            restock()  # Call restock function to add stock.
        elif wish == "4":
            print("Thanks for visiting Us. Have a nice day!")  # Exit message.
            print("=" * 110)
            break  # Exit the loop and end the program.
        else:
            print("This is Invalid wish. Please enter 1 to 4 digits Only.")  # Handle wrong inputs.
            print("=" * 110)

# this line run the program.
main()  # Call the main function directly to start the program.
