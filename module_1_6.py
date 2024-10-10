my_dict = {'a' : 'First letter of the alphabet',
           'z' : 'Last letter of the alphabet',
           1 : 'Number',
           'Nikita' : 'my name'
           }
print(my_dict)
print(my_dict['a'])
print(my_dict.get('b'))
my_dict['Age'] = 19
my_dict['My University'] = 'URBAN'
my_dict['Nikita'] = 'Not my name'
a = my_dict.pop('z')
print(a)

my_set = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 'a', 'b', 'a'}
print(my_set)
my_set.update([10, 'c'])
my_set.discard(3)
print(my_set)
