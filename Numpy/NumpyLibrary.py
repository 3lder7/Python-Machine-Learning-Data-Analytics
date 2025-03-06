import numpy as np

a = np.array([1,2,3])#função dentro do pacote Numpy
print(a)

b = np.array([(2, 5, 7),(5, 3, 9), (4, 6, 5)])#matriz
print(b)

c = np.zeros((4, 3))#uma matriz de zeros de tamanho 4x3
print(c)

d = np.ones((3, 4))#uma matriz de uns de tamanho 3x4
print(d)

e = np.eye(10)#diagonal principal da amtriz possui 1 e restantes 0
print(e)

print(b.max())#exibe o maior valor da matriz
print(b.min())#exibe o menor valor da matriz
print(b.sum())#soma todos os elementos da matriz
print(b.mean())#média de todos os elementos
print(b.std())#calcula o desvio padrão (?)
