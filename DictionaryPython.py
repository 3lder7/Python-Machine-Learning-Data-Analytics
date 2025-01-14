#dicionario = {chave:valor} 

dicionario = {'Curso':'Python para ML', 
              'Produtor':'Didática Tech',
              'Preço':'Gratuito', 
              'Nota': 10}
print (dicionario['Preço'])

a = dicionario['Nota']
print(a)

dicionario['Pré-Requisito'] = 'Python Básico'
print(dicionario)

print(dicionario.keys())
print(dicionario.values())

dicionario.clear()
print(dicionario)
#Nas listas encontra o valor pelo índice, no dicionário encontra o valor pela palavra
