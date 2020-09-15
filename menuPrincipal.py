import RequestsWeb
import menuSecundario
booleano = True
def menu(opcao):
    if opcao =='0':
       return False

    elif opcao =='1':
        resultado = RequestsWeb.requisicao('USD')
        for chaves, valores in resultado.items():
            print(chaves, ':', valores)
        booleano = menuSecundario.menu()
        return booleano

    elif opcao == '2':
        resultado = RequestsWeb.requisicao('AUD')
        for chaves, valores in resultado.items():
            print(chaves, ':', valores)
        booleano = menuSecundario.menu()
        return booleano

    elif opcao == '3':
        resultado = RequestsWeb.requisicao('CAD')
        for chaves, valores in resultado.items():
            print(chaves, ':', valores)
        booleano = menuSecundario.menu()
        return booleano

    elif opcao == '4':
        resultado = RequestsWeb.requisicao('EUR')
        for chaves, valores in resultado.items():
            print(chaves, ':', valores)
        booleano = menuSecundario.menu()
        return booleano

    elif opcao == '5':
        resultado = RequestsWeb.requisicao('GBP')
        for chaves, valores in resultado.items():
            print(chaves, ':', valores)
        booleano = menuSecundario.menu()
        return booleano

    elif opcao == '6':
        resultado = RequestsWeb.requisicao('ARS')
        for chaves, valores in resultado.items():
            print(chaves, ':', valores)
        booleano = menuSecundario.menu()
        return booleano

    elif opcao == '7':
        resultado = RequestsWeb.requisicao('JPY')
        for chaves, valores in resultado.items():
            print(chaves, ':', valores)
        booleano = menuSecundario.menu()
        return booleano

    elif opcao == '8':
        resultado = RequestsWeb.requisicao('CHF')
        for chaves, valores in resultado.items():
            print(chaves, ':', valores)
        booleano = menuSecundario.menu()
        return booleano

    elif opcao == '9':
        resultado = RequestsWeb.requisicao('BTC')
        for chaves, valores in resultado.items():
            print(chaves, ':', valores)
        booleano = menuSecundario.menu()
        return booleano

    else:
        print("Opção inválida!")
        return True