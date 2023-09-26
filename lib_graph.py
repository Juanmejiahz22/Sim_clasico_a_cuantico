import calcu_cplx as cal
from matplotlib import pyplot
import numpy as np

def cani(matriz,state,clicks):
    cli = 0
    if len(matriz) == len(state):
        while cli != clicks:
            state = cal.accionmat(matriz,state)
            cli+=1
        return state
    else:
        return "The size is different"

def dou(matriz,state,clicks):
    cli = 0
    oring = state
    if len(matriz) == len(state):
        while cli != clicks:
            state = cal.accionmat(matriz,state)
            cli+=1
        return cal.transicion(state,oring)
    else:
        return "The size is different"

def multipleprobal(matrix,vector,n):
    re = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 1:
                return "No es unitaria"
            else:
                case = 0
                while case != n:
                    case+=1
                    re.append(cal.accionmat(matrix, vector))
    return vector

def graph(res,no,dates,n):
    pyplot.title("El estado del sistema es")
    g = range(len(res))
    pyplot.bar(g,dates,height=1,width=0.9)
    pyplot.xlabel("Vertices")
    pyplot.show()
