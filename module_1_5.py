immutable_var = (1, 2, 3, 'hello')
print('Immutable tuple:', immutable_var)
#immutable_var[0] = 0 выдается ошибка тк кортеж неизменный
#print(immutable_var)
mutable_list = [1, 2, 3, 'bye']
mutable_list[0] = 0
print('Mutable_list:', mutable_list)
