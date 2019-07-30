import itertools

'''Liczba doskonala'''
def get_factors(x):
    ret_list = []
    for i in range(1, x):
        if x % i == 0:
            ret_list.append(i)
    return ret_list

print(get_factors(20))

candidate_list = [i for i in  range(1, 10001)]

filtered_list = list(itertools.filterfalse(lambda x: sum(get_factors(x)) != x, candidate_list))

for each in filtered_list:
    print("{} and it's factors: {}".format(each, get_factors(each)))


'''10 pierwszych liczb pierwszych'''


def check_if_has_dividers(x):
    for i in range(2, x):
        if x % i == 0:
            return True
    else:
        return False

# not optimal:
prime_numbers = list(itertools.filterfalse(lambda x: check_if_has_dividers(x), range(1, 10000)))
print(prime_numbers)

print(prime_numbers[:10])

prime_numbers = itertools.islice(itertools.filterfalse(lambda x: check_if_has_dividers(x), range(10000000)), 10)
print(list(prime_numbers))

