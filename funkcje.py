def double(x):
    return 2 * x


def root(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x / 2

number = 8

transform_list = [double, root, div2, negative]

tmp_return_value = number

for pos in transform_list:
    tmp_return_value = pos(tmp_return_value)
    print(tmp_return_value)