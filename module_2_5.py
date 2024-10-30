def get_matrix(n, m, value):  # n-line, m-column
    matrix = []
    if (n <= 0) or (m <= 0):
        return matrix
    else:
        for i in range(n):
            empty_list = []
            for j in range(m):
                empty_list.append(value)
            matrix.append(empty_list)
        return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
result4 = get_matrix(-1, 2, 13)
print(result1)
print(result2)
print(result3)
print(result4)
