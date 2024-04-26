import numpy as np
import time

def lowerTriangle(mat, b):
    for i in range(0, len(mat)):
        for j in range(i + 1, len(mat)):
            d =  mat[j][i]/mat[i][i]
            mat[j] -= mat[i] * d
            b[j][0] -= b[i][0] * d
    return mat, b

def backSubstitution(mat,b):
    result = np.zeros(len(b))
    for i in range(len(b)-1, -1, -1):
        sum = 0
        for j in range(len(b)-1, i-1, -1):
            sum += mat[i][j] * result[j]
        result[i] = (b[i][0] - sum) / mat[i][i]
    return result

def reverseRowReduction(mat, b):
    for i in range(len(b)-1, -1, -1):
        b[i][0] /= mat[i][i]
        for j in range(0, i):
            b[j][0] -= mat[j][i] * b[i][0]
    return b

def genMatrix():
    a = np.round(np.random.rand(10000, 10000)*10) + 1
    b = np.round(np.random.rand(10000,1)*10) + 1
    #a = np.array([[2.0,3.0,-1.0,-1.0,-1.0],
    #          [-1.0,-2.0,-2.0,2.0,1.0],
    #          [1.0,1.0,1.0,-1.0,-2.0],
    #          [1.0,-1.0,1.0,1.0,-3.0],
    #          [-1.0,2.0,-1.0,2.0,1.0]])
    #b = np.array([[-4.0],[10.0],[-8.0],[-6.0],[4.0]])
    return a, b

a, b = genMatrix()
a, b = lowerTriangle(a,b)

start = time.time()
backSubstitution(a,b)
totalTime = time.time() - start

print("Back Substitution total time = {}\n".format(totalTime))

a, b = genMatrix()
a, b = lowerTriangle(a,b)

start = time.time()
reverseRowReduction(a, b)
totalTime = time.time() - start

print("Reverse Row Reduction total time = {}\n".format(totalTime))
