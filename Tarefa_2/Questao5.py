import numpy

def checkFloatEquality(a, b):
    if abs(a - b) < 0.0001:
        return True
    return False

def simpleDotProduct(u, v):
    val = 0
    for i in range(len(u)):
        val += u[i] * v[i]
    return val

def gaussJordanMethod(mat):
    mat = numpy.copy(mat)
    id = numpy.identity(len(mat))
    for i in range(0, len(mat)):
        for j in range(i + 1, len(mat)):
            d =  mat[j][i]/mat[i][i]
            mat[j] -= mat[i] * d
            id[j] -= id[i] * d
    for i, row in enumerate(mat):
        for j, val in enumerate(row):
            if checkFloatEquality(val, 0):
                mat[i][j] = 0
    for i in range(len(mat)-1, -1, -1):
        d = mat[i][i]
        mat[i] /= d
        id[i] /= d
        for j in range(0, i): 
            d = mat[j][i]/mat[i][i]
            mat[j] -= mat[i] * d
            id[j] -= id[i] * d
    return id

def is_orthogonal_by_definition(mat):
    #Verify By Checking if AInverse = ATranspose
    #(Strict Definition)
    inverse = gaussJordanMethod(mat)
    transpose = numpy.transpose(mat)
    print("Inverse: ", inverse, '\n')
    print("Transpose: ", transpose, '\n')
    for i, row in enumerate(transpose):
        for j, val in enumerate(row):
            if not checkFloatEquality(val, inverse[i][j]):
                return False
    #Verify By Multiplying A * ATranspose = Identity
    #(Implication of Definition)
    id = numpy.identity(len(mat))
    mult = mat @ transpose
    print("Mat * MatT: ", mult, '\n')
    for i, row in enumerate(mult):
        for j, val in enumerate(row):
            if not checkFloatEquality(val, id[i][j]):
                return False
    return True

def is_orthogonal_by_vectors(mat):
    matT = numpy.transpose(mat)
    #Verify if Columns have Unit Length
    for column in matT:
        quadraticSum = 0
        for value in column:
            quadraticSum += value**2
        if not checkFloatEquality(quadraticSum, 1):
            return False
    print("Columns Have Unit Lenght!\n")
    #Verify Ortogonality with Other Columns
    for i in range(len(matT) - 1):
        for j in range(i + 1, len(matT)):
            dp = simpleDotProduct(matT[i], matT[j])
            if not checkFloatEquality(dp, 0):
                print("Columns are not Orthogonal With Eachother.\n")
                return False
    print("Columns are Orthogonal With Eachother!\n")
    return True


print("a) P2: \n")

mat = numpy.array(
    [[-.40825, .43644, .80178],
     [-.8165, .21822, -.53452],
     [-.40825, -.87287, .26726]]
)

print("Matrix: ", mat, '\n')
print("By Definition: ", is_orthogonal_by_definition(mat), '\n')
print("By Vectors: ", is_orthogonal_by_vectors(mat), '\n')

print("a) P2: \n")

mat = numpy.array(
    [[-.51450, .48507, .70711],
     [-.68599, -.72761, 0.0000],
     [.51450, -.48507, .70711]]
)

print("Matrix: ", mat, '\n')
print("By Definition: ", is_orthogonal_by_definition(mat),'\n')
print("By Vectors: ", is_orthogonal_by_vectors(mat), '\n')

print("b) P1: \n")

mat = numpy.array(
    [[-.58835, .70206, .40119],
     [-.78446, -.37524, -.49377],
     [-.19612, -.60523, .77152]]
)

print("Matrix: ", mat, '\n')
print("By Definition: ", is_orthogonal_by_definition(mat),'\n')
print("By Vectors: ", is_orthogonal_by_vectors(mat), '\n')

print("b) P2: \n")

mat = numpy.array(
    [[-.47624, -0.4264, .30151],
     [.087932, .86603, -.40825],
     [-.87491, -.26112, .86164]]
)

print("Matrix: ", mat, '\n')
print("By Definition: ", is_orthogonal_by_definition(mat),'\n')
print("By Vectors: ", is_orthogonal_by_vectors(mat), '\n')

#mat = numpy.array([[10.0,3.0,4.0],[5.0,1.0,2.0],[11.0,12.0,13.0]])
#print(is_orthogonal_by_definition(mat))
#print(is_orthogonal_by_vectors(mat))

#mat = numpy.array([[-1.0, 0.0],[0.0, -1.0]])
#print(is_orthogonal_by_definition(mat))
#print(is_orthogonal_by_vectors(mat))

#mat = numpy.array([[3/7, 2/7, 6/7],[-6/7, 3/7, 2/7],[2/7, 6/7, -3/7]])
#print(is_orthogonal_by_definition(mat))
#print(is_orthogonal_by_vectors(mat))