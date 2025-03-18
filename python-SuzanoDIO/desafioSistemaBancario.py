saldo = 0
limite = 500
extrato = ""
numero_saques = 1
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
    global extrato
    global numero_saques
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
        print(f"Saldo Atual: R${saldo}")
        valor = float(input("Digite o valor do saque: "))
        sacar(valor)
    
    elif(opcao == "e"):
        print("Extrato")
        mostrar_extrato()
    
    elif(opcao == "q"):
        break

    else:
        print("Opção inválida")
