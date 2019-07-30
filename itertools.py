import itertools as it
import math

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

list_of_permutations = []

for permutation in it.permutations(notes, 4):
    list_of_permutations.append(permutation)
    print(permutation)

amount = math.factorial(len(notes)) / math.factorial((len(notes) - 4))
print("4-notes melody, notes cannot repeat - it is variation without repeating - there are {} possibilities".format(amount))

print("Checking: {}".format(len(list_of_permutations)))

list_of_combinations = []

for combination in it.product(notes, repeat = 4):
    list_of_combinations.append(combination)
    print(combination)

amount = math.pow(len(notes), 4)
print("4-notes melody - notes can repeat - it is variation with repeating - there are {} possibilities".format(amount))

print("Checking: {}".format(len(list_of_combinations)))