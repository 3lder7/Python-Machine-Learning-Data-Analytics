def salvar_carro(marca, modelo, ano, placa):
    print(f"Salvando informações do carro: {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Palio", "Fiat", 2010, "ABC-1234")#desvantagem = usuario altera ordem dos argumentos
salvar_carro(marca="Palio", modelo="Fiat", ano=2010, placa="ABC-1234")#vantagem = mantém os valores corretos, independente da ordem