pessoa = {"nome": "Guilherme", "idade": 28}
pessoa = dict(nome="Guilherme", idade = 28)
pessoa["telefone"] = "3333-1234" #adiciona novo valor

contatos={#like a database
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3333-5678"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3333-9999"}
}

telefone= contatos["giovanna@gmail.com"]["telefone"] #acessa o valor do dicionário
print(telefone)


for chave in contatos:
    print(chave)#imprime as chaves
    print(contatos[chave])#imprime os valores
