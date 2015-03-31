def test():
    """Stupid test function"""
    L = []
    for i in range(100):
        L.append(i)


def filter_list_slow(arr):
    output = []
    for element in arr:
        if element % 2:
            output.append(element)
    return output


def filter_list_faster(arr):
    return filter(lambda x: x % 2, arr)


def filter_list_comprehension(arr):
    return [element for element in arr if element % 2]


def modify(x):
    return x * x * x + 3 * x * x + 5 * x

>>> %timeit map(modify, ARR)
10 loops, best of 3: 184 ms per loop

>>> %timeit map(lambda x: x * x * x + 3 * x * x + 5 * x, ARR)
10 loops, best of 3: 186 ms per loop

>>> %timeit [x * x * x + 3 * x * x + 5 * x for x in ARR]
10 loops, best of 3: 135 ms per loop

def find_x(arr, min_val):
    return [element for element in arr if element > min_val][0]

def find_x_loop(arr, min_val):
    for element in arr:
        if element > min_val:
            return element

def find_x_gen(arr, min_val):
    return next(element for element in arr if element > min_val)