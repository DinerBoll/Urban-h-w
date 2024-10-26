numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = None
for i in numbers:
    if i == 1:
        continue
    else:
        count = 0
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                count += 1
                break
        if count == 0:
            primes.append(i)
        else:
            not_primes.append(i)
print(primes, not_primes)
