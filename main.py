
import menuPrincipal

booleano = True
while booleano == True:
    print("######################################################################")
    print("Selecione a cotação que deseja saber o preço e digite o Número correspondente:\n1-Dólar USD\n2-Dólar Australiano AUD\n3-Dólar Canadense CAD\n4-Euro EUR\n"
          "5-Libra Esterlina GBP\n6-Peso Argentino ARS\n7-Iene Japonês JPY\n8-Franco Suíço CHF\n9-Bitcoin BTC\n0-Sair do programa\nOpção desejada:")
    opcao=input()
    booleano = menuPrincipal.menu(opcao)






