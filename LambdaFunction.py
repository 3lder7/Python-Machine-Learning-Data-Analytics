def somaQuadrado(a, b):
    somaQ = a**2 + b**2
    return somaQ
print(somaQuadrado(2,3))

somaQuadrado2 = lambda a, b: a**2 + b**2
print(somaQuadrado2(2,3))

x= lambda f : f/2
print(x(10))