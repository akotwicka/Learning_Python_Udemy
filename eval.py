import math

argument_list = []

for i in range(100):
    argument_list.append(i/10)

print(argument_list)

formula = input('Insert formula where x is an argument: ')

for x in argument_list:
    print(eval(formula))