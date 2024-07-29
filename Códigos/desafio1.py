# Desafio de Projeto: Criando um Sistema Bancário
# Desenvolvido por: Rute Miranda Ferreira

menu = """

Olá! Selecione a opção desejada:

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor_deposito = float(input("\nInforme o valor do depósito: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"

            print("\nDepósito realizado com sucesso!")

        else:
            print("\nO valor informado é inválido. Operação cancelada!")
    
    elif opcao == "2":
         valor_saque = float(input("\nInforme o valor do saque: "))

         if valor_saque > saldo:
             print("\nSaldo insuficiente. Operação cancelada!")
        
         elif valor_saque > limite:
             print("\nO valor solicitado ultrapassa o limite máximo de R$ 500,00 por saque. Operação cancelada!")
        
         elif numero_saques >= LIMITE_SAQUES:
             print("\nNúmero máximo de saques excedido. Operação cancelada!")

         elif valor_saque > 0:
             saldo -= valor_saque
             numero_saques += 1
             extrato += f"Saque: R$ {valor_saque:.2f}\n"

             print("\nSaque realizado com sucesso!")

         else: 
             print ("\nO valor informado é inválido. Operação cancelada!")
        
    elif opcao == "3":
         
         if extrato == "":
             print("\nNão foram realizadas movimentações")

         else:
            print("\n================ EXTRATO ================\n")
            print(extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")

    elif opcao == "0":
        break

    else:
        print("\nOperação inválida, por favor selecione novamente a opção desejada.")