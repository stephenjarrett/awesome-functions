#Matrix Addition
import random

def matrix_addition():
    print('Matrix Addition I and II')
    matrix1 = [[random.randint(1, 9), random.randint(1, 9)], [
        random.randint(1, 9), random.randint(1, 9)]]
    matrix2 = [[random.randint(1, 9), random.randint(1, 9)], [
        random.randint(1, 9), random.randint(1, 9)]]
    print('Matrix 1: ' + str(matrix1))
    print('Matrix 2: ' + str(matrix2))
    matrix3 = []
    print('The sum of matrix 1 + matrix 2 is:')
    for x in range(len(matrix1)):
        matrix1_1 = matrix1[x]
        matrix2_2 = matrix2[x]
        matrix3a = []
        for y in range(len(matrix1_1)):
            matrix1_1num = matrix1_1[y]
            matrix2_2num = matrix2_2[y]
            matrix3a.append(matrix1_1num + matrix2_2num)
        matrix3.append(matrix3a)
    print(matrix3)
    print()
    return matrix3