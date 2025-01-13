import random
cidades = ['São Paulo', 'Salvador', 'Rio de Janeiro', 'Porto Alegre']
escolhida = random.choice(cidades)
print(escolhida)

a = [1,2,3]
a.append(4)
print(a)

b=[5, 6, 7]
for item in b:
    a.append(item)#passa a adicionar todos da lista B, na lista A
print(a)