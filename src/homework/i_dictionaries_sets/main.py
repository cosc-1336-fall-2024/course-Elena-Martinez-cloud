import dictionary
#1-Get p distance matrix
#2-Exit
#The program runs until the user chooses option 2
def main():
    while True:
        print("Menu:")
        print("1 - Get p distance matrix")
        print("2 - Exit")
        selection = input("Choose option 1 or 2: ")

        if selection == '1':
            # Option 1 prompt the user for a list, 
            # call the get_p_distance_matrix function and display the result.
            input_strings = input("Enter the DNA string seperated with commas: ")
            
            dna_list = [s.strip().split() for s in input_strings.split(',')]
            
            if all(len(s)== len(dna_list[0])for s in dna_list):
                distance_matrix = dictionary.get_p_distance_matrix(dna_list)
                for row in distance_matrix:
                    print(" ".join(f"{value:.5f}" for value in row))
            else:
                print("Error! The DNA has to be equal length")
        elif selection == '2':
            print("Exiting")
            break
        else:
            print("Invalid! Try Again.")

main ()
