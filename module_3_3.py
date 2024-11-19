# 1
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(*[1, 2, 3])
print_params(**{'a': 2, 'b': 4, 'c': 6})
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

# 2
values_list = [10, 'Второе', False]
values_dict = {'a': 1, 'b': 'letter', 'c': True}
print_params(*values_list)
print_params(**values_dict)

# 3
values_list_2 = [123, 'Alphabet']
print_params(*values_list_2, 42)
