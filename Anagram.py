import itertools
import numpy

file = numpy.genfromtxt("words.txt", delimiter = " ")

# Get characters from user
char_list = input("Enter each letter separated by a space.\n")
char_bank = char_list.replace(" ", "")

# Create bank of possible combinations
word_bank = list(itertools.permutations(char_bank, len(char_bank)))

# Check if words in bank are actual words
for i in word_bank:
    if "".join(i) not in file:
        pass
    else:
        print("".join(i))
