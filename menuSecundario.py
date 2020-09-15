def menu():
    opcao = input("\nDeseja Realizar uma nova consulta?\n1-Sim.\n0-Não, sair do programa.\nOpção Desejada:")

    if opcao == '0':
        return False
    elif opcao == '1':
        return True
    else:
        print("Opção Inválida!")