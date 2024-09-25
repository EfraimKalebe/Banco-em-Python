
menu = '''

[1]depósito        [2]saque

[3]extrato          [4]sair

'''

saldo = 0
limite = 500
extrato = ""
limiteSaque = 3
numeroDeSaque = 0
while True:
    opcao = input(menu)
    if opcao == 1:
        valor = float(input("Informe o valor do depósito."))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! o valor informado e invalido.")
    elif opcao == 2:
        valor = float(input("Informe o valor do saque: "))
        saldoExcedido = valor > saldo
        limiteExcedido = valor > limite
        saqueExcedido = numeroDeSaque >= limiteSaque
        if  saldoExcedido:
            print("Operação falhou, saldo excedido.")
        elif limiteExcedido:
            print("Operação falhou, o valor do saque excede o limite.")
        elif saqueExcedido:
            print("Operação falhou, número máximo de saque excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numeroDeSaque = 1
        else:
            print("Operação falhou, valor informado é inválido.")
    elif opcao == 3:
        print("\n============ EXTRATO ============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: RS${saldo:.2f}\n")
        print("=================================")
    elif opcao == 4:
        print("saindo...")
    else:
        print("Operação inválida, selecione novamente a operação desejada.")