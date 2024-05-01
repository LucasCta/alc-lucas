import numpy

def colVecDotProduct(u, v):
    mat = [[0 for i in u] for i in u]
    for i, vu in enumerate(u):
        for j, vi in enumerate(v[0]):
            mat[i][j] = vi * vu[0]
    return mat

def norm(u):
    r = 0
    for val in u:
        r += val[0] ** 2
    return r**0.5

def matNorm(mat):
    r = 0
    for vec in mat:
        for val in vec:
            r += val**2
    return r**0.5

def getResults(u, v):
    uvt = colVecDotProduct(u, numpy.transpose(v))
    ruvt = numpy.linalg.matrix_rank(uvt)
    u2v2 = norm(u) * norm(v)
    uvt2 = matNorm(uvt)
    print("Posto uvT = ", ruvt)
    print("||u||2 ||v||2  = ", u2v2)
    print("||uvT||2 = ", uvt2)

for n in [5, 10, 25]:
    u = numpy.random.rand(n, 1)
    v = numpy.random.rand(n, 1)
    getResults(u, v)