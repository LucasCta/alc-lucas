import numpy

# Operações Com Ponto Flutuante Podem Causar Erros de Arredondamento
def checkFloatEquality(a, b):
    if abs(a - b) < 0.0001:
        return True
    return False

def inversa_eliminacao(mat):
    # Evitando Alterações Externas à Função
    mat = numpy.copy(mat)
    # Gerando a Matriz Identidade
    id = numpy.zeros((len(mat), len(mat)))
    for i in range(len(mat)):
        id[i][i] = 1
    # Verificação de Valores Nulos na Diagonal Principal e Matriz Quadrada
    for i in range(len(mat)):
        if (mat[i][i] == 0):
            raise ValueError("Valor nulo na diagonal principal, por favor utilize um método alternativo.")
        if len(mat) != len(mat[i]):
            raise ValueError("Matriz Utilizada Não é Quadrada")
    # Gerando Matriz Triangular Superior
    for i in range(0, len(mat)):
        for j in range(i + 1, len(mat)):
            if checkFloatEquality(mat[i][i], 0):
                raise ValueError("Divisão por 0 encontrada, por favor utilize outra técnica.")
            d =  mat[j][i]/mat[i][i]
            mat[j] -= mat[i] * d
            id[j] -= id[i] * d
    # Arredondando Erros de Aproximação para Ponto Flutuante
    for i, row in enumerate(mat):
        for j, val in enumerate(row):
            if checkFloatEquality(val, 0):
                mat[i][j] = 0
    # Removendo os Valores de Baixo para Cima
    for i in range(len(mat)-1, -1, -1):
        d = mat[i][i]
        if checkFloatEquality(d,0):
            raise ValueError("Divisão por 0 encontrada, por favor utilize outra técnica.")
        mat[i] /= d
        id[i] /= d
        for j in range(0, i): 
            d = mat[j][i]/mat[i][i]
            mat[j] -= mat[i] * d
            id[j] -= id[i] * d
    # Retorna a Matriz Inversa
    return id

# Função Apenas para Fim de Testes
def genMatrix():
    a = numpy.round(numpy.random.rand(3, 3)*10)
    return a

mat = genMatrix()
print(mat)
print(inversa_eliminacao(mat))