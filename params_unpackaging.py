def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = ['HappyNY', 2025, False]
values_dict = {'a': 25,'b': 'january', 'c': 'NY'}

print_params(**values_dict)
print_params(*values_list)

values_list_2 = [25, 'Hello']
print_params(*values_list_2, 42)