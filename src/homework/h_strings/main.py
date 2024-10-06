#
import string

from examples.h_strings import strings

def main():
    print("Menu: 1.Hamming Distance. 2.DNA Complement. 3.Exit")
    Options = int(input("Input the number of what you need: "))

    if Options == 1:
        dna1 = input("DNA1: ")
        dna2 = input("DNA2: ")
        result = strings.get_hamming_distance(dna1, dna2)
        print("Result: ", result)
    elif Options == 2:
        dna = input("Enter DNA Sequence: ")
        result_1 = strings.get_dna_complement(dna)
        print("Result: ", result_1)
    elif Options == 3:
        print("Exit")
        exit()
    
main ()


