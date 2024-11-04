import lists
#1-Show the list low /high values
#2-Exit

def main():
    while True:
        print("Menu:")
        print("1 - Show the list low/high value")
        print("2 - Exit")
        choice = input("Enter your choice: ")
#Option 1 prompt the user to enter list values until they opt to stop: Enter a list value 1

        if choice == '1':
            numbers = []
            print("Enter a list values (type 'done' to finish):")
            while True:
                value = input("Enter a list value: ")

                if value.lower() == 'done':
                    break

                try:
                    number = float(value)
                    numbers.append(number)
                except ValueError:
                    print("please enter a valid number and stop when you are ready")
                    continue

#Do you want to enter another value?(Display this after the user enters at least 3 values)

                if len(numbers) >= 3:
                    another = input("Do you want to enter another value? (yes/no): ")
                    if another != 'yes':
                        break

            if numbers:
                lowest_value = lists.get_lowest_list_value(numbers)
                highest_value = lists.get_highest_list_value(numbers)
                print(f"The lowest number is: {lowest_value}")
                print(f"The highest number is: {highest_value}")
            else:
                print("No numbers were entered.")

#The program runs until the user chooses option 2

        elif choice == '2':
            print("Exiting the program.")
            break

        else:
            print("ERROR! Please select 1 or 2.")

main()


