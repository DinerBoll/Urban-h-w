import random

first_cell = random.randint(3, 20)
result = ''
no_pairs = []
for i in range(1, first_cell):
    for l in range(1, first_cell):
        if i == l:
            continue
        elif first_cell % (i + l) == 0 and ((str(i) + str(l)) not in no_pairs):
            result += str(i) + str(l)
            no_pairs.append(str(l) + str(i))
print(first_cell, '- число из первой вставки', '\n' + result, '- нужный пароль')
