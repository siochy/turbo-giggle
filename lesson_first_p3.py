import functools


list_of_strings = ['asdvsDv', 'iLgbilgjb', 'svbkJKijdio', 'Iuqwyepo']

# strings from list to one string
strings_connector = functools.reduce(lambda i, j: i + ' ' + j, list_of_strings).lower()
print(strings_connector)


some_list = ['fskduvk', 7219, 12.67, 'sdgkusv', [1, 2, 3], 78, 16.98]

# filter list resulting string and integer elements
strings_and_ints = list(filter(lambda x: type(x) in [int, str], some_list))
print(strings_and_ints)


some_tuple = ('sdudvh', 728, ('ki', ' uy', 'iop'), [1, 8.87, 90], 34, 76.098, 'ajlsfi')

# double elements in iterable if it's not integer
double_not_int = map(lambda x: x * 2 if type(x) is not int else x, some_tuple)
print(list(double_not_int))
