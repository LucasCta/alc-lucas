import numpy as np
from matplotlib import pyplot as plt

l1, l2 = 20.0, 15.0

def rotate(theta):
  thetar = theta / 180.0 * np.pi
  rot = np.array([[np.cos(thetar), -np.sin(thetar), 0],
                  [np.sin(thetar),  np.cos(thetar), 0],
                  [0,               0,              1]])
  return rot

#Gera Matriz de Translacao
def translate(dist):
  rot = np.array([[1, 0, dist],
                  [0, 1, 0],
                  [0, 0, 1]])
  return rot
  
def bracoRobo(theta1, theta2):
    #Gera Matriz de Rotacao
    xlist = np.array([0])
    ylist = np.array([0])
    spoint = [[0],
              [0],
              [1]]
             
    #Mudanca para a ponta do primeiro braco
    T = rotate(theta1)
    T = np.matmul(T, translate(l1))
    
    middlePoint = np.matmul(T, spoint)
    xlist = np.append(xlist, middlePoint[0][0])
    ylist = np.append(ylist, middlePoint[1][0])
    
    #Mudanca para a ponta do segundo braco
    T = np.matmul(T, rotate(theta2))
    T = np.matmul(T, translate(l2))
    
    finalPoint = np.matmul(T, spoint)
    xlist = np.append(xlist, finalPoint[0][0])
    ylist = np.append(ylist, finalPoint[1][0])
    
    xlist, ylist = np.round(xlist, 1), np.round(ylist, 1)
    print("Posicao do Efetuador Final: X={}cm, Y={}cm".format(xlist[-1], ylist[-1]))
    
    plt.figure(figsize=(5,5))
    plt.xlim(0, 50), plt.ylim(0, 50)
    plt.plot(xlist, ylist, "bo-")
    for i in range(len(xlist)):
        plt.text(xlist[i], ylist[i], f'({xlist[i]}, {ylist[i]})')
    plt.show()

    return (xlist[-1], ylist[-1])

print(bracoRobo(10,35))
