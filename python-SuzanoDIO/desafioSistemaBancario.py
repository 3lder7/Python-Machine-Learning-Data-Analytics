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
    print("Digite o valor a ser depositado")
    valor = float(input())
    saldo += valor
    extrato += f"Déposito no valor de: {valor}"
    #print("Deseja fazer mais depósitos?"
    #"[s] Sim"
    #"[n] Não")
    #input(opcao)
    #if(opcao == "s"):
    #   while


while True:

    opcao = input(menu)

    if(opcao == "d"):
        print("Depósito")

    elif(opcao == "s"):
        print("Saque")
    
    elif(opcao == "e"):
        print("Extrato")
    
    elif(opcao == "q"):
        break

    else:
        print("Opção inválida")
