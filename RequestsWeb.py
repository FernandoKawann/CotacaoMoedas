import requests
import json

def requisicao(moeda):
    try:
        requisicao = requests.get('https://economia.awesomeapi.com.br/json/all')


        cotacao = (json.loads(requisicao.text))

        resultado = {'Nome':cotacao[moeda]['name'], 'Max do dia': cotacao[moeda]['high'], 'Min do dia': cotacao[moeda]['low'],
                     'Valor Atual':cotacao[moeda]['bid'], 'Momento da consulta': cotacao[moeda]['create_date'] }
        return resultado

    except:
        print("Dados não encontrados.")
        return None

