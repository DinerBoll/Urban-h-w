calls = 0


def count_calls():  # Подсчитывает вызовы остальных функций
    global calls
    calls += 1


def string_info(x):
    count_calls()
    info = (len(x), x.upper(), x.lower())
    return info


def is_contains(a, b):
    count_calls()
    a = a.upper()
    for i in b:
        b.remove(i)
        b.append(i.upper())
    if a in b:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
