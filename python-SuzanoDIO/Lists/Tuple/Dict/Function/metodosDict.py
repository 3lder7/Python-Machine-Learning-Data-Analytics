contatos={
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3333-5678"},
    "guilhermino@gmail.com": {"nome": "Guilhermino", "telefone": "3333-9999"}
}
copia = contatos.copy()#copia o dicionário
copia["guilherme@gmail.com"] = {"nome": "Gui"}
#manipular dicionarios sem alterar o original


#contatos.clear()#limpa o dicionário
#print(contatos)