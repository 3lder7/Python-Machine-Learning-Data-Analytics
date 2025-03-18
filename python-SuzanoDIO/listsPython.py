frutas =["laranja", "maçã", "uva"]
letras = list("python")
numeros = list(range(11))
print(frutas)
print(letras)
print(numeros)

#matriz
matriz =[
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])#[1 , "a", 2]
print(matriz[0][0])#1
print(matriz[0][-1])#2
print(matriz[-1] [-1])#c

#fatiamento
lista=["p", "y", "t", "h", "o", "n"]

print(lista[2:])
print(lista[:2])
print(lista[1:3])
print(lista[0:3:2])
print(lista[::])

#filtro
numeros2=[1,30,21,2,9,65,34]
pares=[]

for numero in numeros:
    if numero % 2 ==0:
        pares.append(numero)
        print(pares)