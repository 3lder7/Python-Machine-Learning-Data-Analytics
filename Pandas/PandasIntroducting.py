import pandas as pd
alunos = {'Nome': ['Ricardo', 'Pedro', 'Roberto', 'Carlos'], 
          "Nota": [4, 7, 5.5, 9], 
          "Aprovado": ['Não', 'Sim', 'Não', 'Sim']}
dataframe = pd.DataFrame(alunos)
print(dataframe)

import numpy as np
objeto1 = pd.Series([2, 6, 9, 10, 5])#vertical
print(objeto1)

array1 = np.array([2, 6, 9, 10, 5])#horizontal unidimensional
print(array1)
array2=np.array([(2, 6, 9, 10, 5), (8, 7, 3, 1, 4)])#horizontal bidimensional
print(array2)

objeto2 = pd.Series(array1)#Series é um array unidimensional
print(objeto2)
