import pandas as pd
alunosDIC = {'Nome': ['Ricardo', 'Pedro', 'Roberto', 'Carlos'], 
             'Nota': [4, 7, 5.5, 9], 
             'Aprovado': ['Não', 'Sim', 'Não', 'Sim']}

alunosDF = pd.DataFrame(alunosDIC)

print(alunosDF)

print(alunosDF.head())#exibe 5 primeiras
print(alunosDF.shape)#exibe números de linhas e columas
print(alunosDF.describe())#calcula diversas informações (quantidade, media, porcentagem)

