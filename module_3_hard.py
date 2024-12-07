data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

sum_main = 0

def calculate_structure_sum(obj):
    global sum_main
    if isinstance(obj, list): #Проверяем на тип данных (список)
        for item in obj: #Проверяем каждый элемент списка
            calculate_structure_sum(item) #Отправляем на проверку по типу данных и так по кругу пока не будет строка или число и все остальные также
    elif isinstance(obj, dict):
        for key, value in obj.items():
            sum_main += len(key)
            calculate_structure_sum(value)
    elif isinstance(obj, set):
        for item in obj:
            calculate_structure_sum(item)
    elif isinstance(obj, tuple):
        for item in obj:
            calculate_structure_sum(item)
    elif isinstance(obj, int):
        sum_main += obj
    elif isinstance(obj, str):
        sum_main += len(obj)

calculate_structure_sum(data_structure)
print(sum_main)
