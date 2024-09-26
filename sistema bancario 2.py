menu = '''
[1] Deposito        [2] Saque
[3] Extrato         [4] Sair
'''

saldo = 0
limite = 500
extrato = ""
limiteSaque = 3
numeroDeSaque = 0

while True:
    opcao = int(input(menu))
    
    if opcao == 1:
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == 2:
        valor = float(input("Informe o valor do saque: "))
        saldoExcedido = valor > saldo
        limiteExcedido = valor > limite
        saqueExcedido = numeroDeSaque >= limiteSaque
        
        if saldoExcedido:
            print("Operação falhou! Saldo insuficiente.")
        elif limiteExcedido:
            print("Operação falhou! O valor do saque excede o limite.")
        elif saqueExcedido:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numeroDeSaque += 1
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == 3:
        print("\n============ EXTRATO ============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}\n")
        print("=================================")
    
    elif opcao == 4:
        print("Saindo...")
        break
    
    else:
        print("Operação inválida! Selecione novamente a operação desejada.")
