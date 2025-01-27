import pandas as pd

# Ler arquivo Excel
dados = pd.read_excel("arquivo1.xlsx")
print(dados.head())


# Ler o arquivo CSV
dados2 = pd.read_csv("athlete_events.csv/athlete_events.csv")
print(dados2.head())