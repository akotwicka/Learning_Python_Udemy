import math
import time

formulas_list = [
    "abs(x**3 - x**0.5)",
    "abs(math.sin(x) * x**2)"
]

argument_list = []
for i in range(1000000):
    argument_list.append(i / 10)
    i += 1

for formula in formulas_list:
    results_list = []
    print(formula)
    start = time.time()
    for x in argument_list:
        results_list.append(eval(formula))
    print(results_list)
    maximum = max(results_list)
    minimum = min(results_list)
    print("Max value: {}, min value: {}".format(maximum, minimum))
    stop = time.time()
    duration = stop - start
    print('Duration time not compiled: {}'.format(duration))

for formula in formulas_list:
    results_list = []
    print(formula)
    start = time.time()
    compiled_formula = compile(formula, formula, 'eval')
    for x in argument_list:
        results_list.append(eval(compiled_formula))
    maximum = max(results_list)
    minimum = min(results_list)
    print("Max value: {}, min value: {}".format(maximum, minimum))
    stop = time.time()
    duration = stop - start
    print('Duration time compiled: {}'.format(duration))

