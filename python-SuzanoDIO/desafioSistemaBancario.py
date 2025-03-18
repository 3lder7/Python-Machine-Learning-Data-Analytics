saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3 #constante

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

def depositar(valor):
    global saldo
    global extrato
    saldo += valor
    extrato += (f"Depósito: R$ {valor:.2f}\n")

def sacar(valor):
    global saldo
    global numero_saques
    if(numero_saques < LIMITE_SAQUES):
        if(valor <= saldo + limite):
            saldo -= valor
            global extrato
            extrato += (f"Saque: R$ {valor:.2f}\n")
            numero_saques += 1
        else:
            print("Saldo insuficiente")
    else:
        print("Limite de saques atingido")

def mostrar_extrato():
    global extrato
    print(extrato)
    
while True:

    opcao = input(menu)

    if(opcao == "d"):
        print("Depósito")
        valor = float(input("Digite o valor do depósito: "))
        depositar(valor)

    elif(opcao == "s"):
        print("Saque")
        valor = float(input("Digite o valor do saque: "))
        sacar(valor)
    
    elif(opcao == "e"):
        print("Extrato")
        mostrar_extrato()
    
    elif(opcao == "q"):
        break

    else:
        print("Opção inválida")
