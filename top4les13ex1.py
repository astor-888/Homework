import random

def create_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(random.randint(-200, 200))
        matrix.append(row)
    return matrix

def add_matrices(m1, m2):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        return None
    result = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m1[0])):
            row.append(m1[i][j] + m2[i][j])
        result.append(row)
    return result

matrix_1 = create_matrix(10, 10)
matrix_2 = create_matrix(10, 10)

print("Матрица 1:")
for row in matrix_1:
    print(row)

print("\nМатрица 2:")
for row in matrix_2:
    print(row)

matrix_3 = add_matrices(matrix_1, matrix_2)

print("\nРезультат сложения:")
for row in matrix_3:
    print(row)

m1 = create_matrix(4, 3)
m2 = create_matrix(4, 3)
print("\nМ1 (4x3):")
for row in m1:
    print(row)
print("М2 (4x3):")
for row in m2:
    print(row)
m3 = add_matrices(m1, m2)
print("Сумма (4x3):")
for row in m3:
    print(row)