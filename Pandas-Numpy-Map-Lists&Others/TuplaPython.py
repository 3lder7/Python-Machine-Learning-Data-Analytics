lista = [1,2,3]
lista[0] = 5
print(lista)

tupla = (6,8,4)#tupla é uma lista que não pode ser alterada
#tupla[0] = 30
#print(tupla)

del lista[0]
print(lista)

novaTupla = tuple(lista)
print(novaTupla)#exibe a tupla com parentêses

numero = (3)#int
numero = (3,)#tuple