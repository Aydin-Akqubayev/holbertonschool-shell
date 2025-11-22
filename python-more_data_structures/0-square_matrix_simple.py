#!/usr/bin/python3
def square_matrix_simple(matrix):
    answ = []
    for i in range(len(matrix)):
        res = []
        for j in range(len(matrix[i])):
            res.append(matrix[i][j]**2)
        answ.append(res)
    return answ
