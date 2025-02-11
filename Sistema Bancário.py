contas = {}

def cadastrar():
    global contas
    conta_nome = input("Digite um nome para a conta: ")
    if conta_nome in contas:
        print(f"Erro: A conta '{conta_nome}' já existe.")
    else:
        saldo_inicial = float(input("Qual o valor do 1º depósito? "))
        if saldo_inicial >= 0 :
          contas[conta_nome] = saldo_inicial
          print(f"Conta '{conta_nome}' criada com sucesso com saldo inicial de R${saldo_inicial:.2f}")
        else:
          print("Valor do depósito negativo, tente novamente.")

    

def depositar():
    global contas
    conta_nome = input("Digite o nome da conta para depósito: ")
    
    if conta_nome in contas:
        valor = float(input("Digite o valor que deseja depositar: "))
        contas[conta_nome] += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso. Saldo atual: R${contas[conta_nome]:.2f}")
    else:
        print(f"Erro: Conta '{conta_nome}' não encontrada.")

def sacar():
    global contas
    conta_nome = input("Digite o nome da conta para saque: ")
    
    if conta_nome in contas:
        valor = float(input("Digite o valor que deseja sacar: "))
        if valor <= contas[conta_nome]:
            contas[conta_nome] -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso. Saldo atual: R${contas[conta_nome]:.2f}")
        else:
            print(f"Você não tem dinheiro suficiente :( , Seu saldo atual é de R${contas[conta_nome]:.2f}")
    else:
        print(f"Erro: Conta '{conta_nome}' não encontrada.")

def transferir():
    global contas
    conta_origem = input("Digite o nome da conta de origem: ")
    
    if conta_origem in contas:
        conta_destino = input("Digite o nome da conta de destino: ")

        if conta_destino in contas:
            valor = float(input("Digite o valor que deseja transferir: "))
            
            if valor <= contas[conta_origem]:
                contas[conta_origem] -= valor
                contas[conta_destino] += valor
                print(f"Transferência de R${valor:.2f} realizada com sucesso da conta '{conta_origem}' para '{conta_destino}'.")
                print(f"Saldo atual da conta '{conta_origem}': R${contas[conta_origem]:.2f}")
            else:
                print(f"Você não tem dinheiro suficiente :( , Seu saldo atual é de R${contas[conta_origem]:.2f}")
        else:
            print(f"Erro: Conta de destino '{conta_destino}' não encontrada.")
    else:
        print(f"Erro: Conta de origem '{conta_origem}' não encontrada.")

def consultar():
    global contas
    conta_nome = input("Digite o nome da conta para consultar o saldo: ")
    
    if conta_nome in contas:
        print(f"Saldo da conta '{conta_nome}': R${contas[conta_nome]:.2f}")
    else:
        print(f"Erro: Conta '{conta_nome}' não encontrada.")

def menu():
    while True:
        print("\nMenu:")
        print("1 - Cadastrar")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Transferir")
        print("5 - Consultar Saldo")
        print("6 - Sair")

        op = input("Escolha uma opção: ")
        
        if op == '1':
            cadastrar()
        elif op == '2':
            depositar()
        elif op == '3':
            sacar()
        elif op == '4':
            transferir()
        elif op == '5':
            consultar()
        elif op == '6':
            print("Fechando o programa...")
            break
        else:
            print("Opção inválida. Escolha um número do Menu.")

menu()