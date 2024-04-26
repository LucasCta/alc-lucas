import numpy as np

def backsub(mat,b):
    #Verifica Presença de Zeros na Diagonal da Matriz Triangular
    for i in range(0, len(mat)):
        if (mat[i][i] == 0):
            raise ValueError("Triangular Matrix With Diagonal Value 0")
    #Inicia o Vetor de Resultados
    result = np.zeros(len(b))
    #Backsubstution
    for i in range(len(b)-1, -1, -1):
        sum = 0
        for j in range(len(b)-1, i-1, -1):
            sum += mat[i][j] * result[j]
        result[i] = (b[i][0] - sum) / mat[i][i]
    return result

def generateTest(mSize=5):
    matT = np.triu(np.round(np.random.rand(mSize, mSize) * 20 - 10))
    b = np.round(np.random.rand(mSize,1) * 20 - 10) + 1
    return matT, b

matT, b = generateTest()
print("mat: ", matT, "\n", "b: ", b)
print("result: ", backsub(matT,b))
