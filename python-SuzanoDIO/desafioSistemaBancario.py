# Sistema Bancário Simples

def menu(opcao):


    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [c] Cadastrar Conta
    [u] Exibir Contas Cadastradas
    [a] Cadastrar Usuário

    [q] Sair
    => """

def depositar(saldo, extrato, valor):
    saldo += valor
    extrato += (f"Depósito: R$ {valor:.2f}\n")

def sacar(valor, saldo, numero_saques, limite):
    
    if (numero_saques <= 3):
        if(valor >= limite):
            print("ERRO! Você só pode sacar até R$500,00")#limite de 500
        else:
            if(valor > saldo):
                print("Saldo Insuficiente")
                print(f"Saldo Atual: R${saldo}")
            else:
                saldo -= valor
                extrato += (f"Saque no valor de: R$ {valor}\n")
                print(f"Saldo Restante: R${saldo}")
                print(f"{numero_saques}")
                numero_saques += 1 #incrementa
    else:
        print("Número de saques diários atingidos")

def mostrar_extrato(extrato):
    
    print(extrato)

def cadastrar_usuario(nome, data_nascimento, cpf, endereco):
    nome = ""
    data_nascimento = ""
    cpf = 0
    #o endereço é uma string com o formato: logradouro, numero, bairro, cidade, estado"
    endereco = ""

    cpf = input("Digite seu CPF (somente número): ")
    if cpf in usuarios:
        print("CPF já cadastrado.")
        return
    else:
        nome = input("Digite seu nome: ")
        data_nascimento = input("Digite sua data de nascimento: ")
    #o enredeço é uma string com o formato: logradouro, numero, bairro, cidade, estado
        endereco = input("Digite seu endereço: ")
        usuarios[cpf] = {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "endereco": endereco
        }
    
    print(f"Usuário {nome} cadastrado com sucesso!")

def criar_conta(agencia, numero_conta, usuario):
    numero_conta = 0

    print("Usuário que deseja criar uma conta")
    cpf = input("Digite seu CPF (somente número): ")
    numero_conta += 1 #incrementa o número da conta a cada nova conta criada
    contas[numero_conta] = {
        "agencia": agencia,
        "extrato": "",
    }

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 1
    LIMITE_SAQUES = 3 #constante
    agencia = "0001"
    usuarios={}# dicionário para armazenar os usuários
    contas = {} # dicionário para armazenar as contas

    while True:
        opcao = input(menu)

        if(opcao == "d"):
            print("Depósito")
            valor = float(input("Digite o valor do depósito: "))
            depositar(valor)

        elif(opcao == "s"):
            print("Saque")
            print(f"Saldo Atual: R${saldo}")
            valor = float(input("Digite o valor do saque: "))
            sacar(valor)
        
        elif(opcao == "e"):
            print("Extrato")
            mostrar_extrato()
        
        elif(opcao == "c"):
            print("Cadastrar Usuário")
            cadastrar_usuario()
        elif(opcao == "q"):
            break
        elif(opcao == "u"):
            print("Exibir Usuários Cadastrados")    
            exibir_usuarios()

        else:
            print("Opção inválida")