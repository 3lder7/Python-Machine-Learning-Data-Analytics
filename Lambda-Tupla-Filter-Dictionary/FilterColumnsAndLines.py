import pandas as pd
alunosDIC = {'Nome': ['Ricardo', 'Pedro', 'Roberto', 'Carlos'], 
             'Nota': [4, 7, 5.5, 9], 
             'Aprovado': ['Não', 'Sim', 'Não', 'Sim']}

alunosDF = pd.DataFrame(alunosDIC)

print(alunosDF)

print(alunosDF['Nome'])
print(alunosDF['Nota'])
print(alunosDF['Aprovado'])

print(alunosDF.loc[[0]])#puxa através do índice
print(alunosDF.loc[0:2])#puxa através do índice

print(alunosDF.loc[alunosDF['Nome'] == 'Pedro'])#puxa a linha que contém o dado "Pedro" na coluna "Nome"
print(alunosDF.loc[alunosDF['Nota'] == 9])#)#puxa a linha que contém o dado 9 na coluna "Nota"