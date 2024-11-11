import dictionary
#Inventory Menu
#1-Add or Update Item
#2-Delete Item
#3-Exit
#The program runs until the user chooses option 3.

def display_menu():
    """Display the Inventory menu."""
    print("\nInventory Menu")
    print("1 - Add or Update Item")
    print("2 - Delete Item")
    print("3 - Exit")

def main():
    inventory_dictionary = {}

    while True:
        display_menu()
        choice = input("choose option 1, 2 or 3: ")

        if choice == '1':
            widget_name = input("Enter the widget name: ")
            quantity = int(input("Enter the quantity: "))
            dictionary.add_inventory(inventory_dictionary, widget_name, quantity)
            print(f"{widget_name} update with quantity {quantity}.")
            print(f"Current inventory: {inventory_dictionary}")

        elif choice == '2':
            widget_name = input("Enter the widget name to delete: ")
            result = dictionary.remove_inventory_widget(inventory_dictionary, widget_name)
            print(result)
            print(f"Current inventory: {inventory_dictionary}")

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invaild choice. Please choose 1, 2, or 3.")

main ()