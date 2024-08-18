def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c=[1, 2, 3])

value_list = ['Milk', 12, True]
value_dict = {'a': 45, 'b' : 'письмо', 'c' : False}

print_params(*value_list)
print_params(**value_dict)

value_list_2 = ['книга', 85]
print_params(*value_list_2, 42)