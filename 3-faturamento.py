import json

with open("dados.json", encoding='utf-8') as dadosJson:
    dadosJson = json.load(dadosJson)

def menorMaior(dadosJson):

    menor = None
    maior = None

    for dados in dadosJson:

        if menor is None and dados['valor'] != 0.0:
            menor = dados['valor']
            maior = dados['valor']
        
        else:
            
            if dados['valor'] != 0.0 and dados['valor'] < menor:
                menor = dados['valor']
            
            if dados['valor'] != 0.0 and dados['valor'] > maior:
                maior = dados['valor']

    return menor, maior

def mediaFaturamento(dadosJson):

    acumulador = 0
    count = 0

    for dados in dadosJson:

        if dados['valor'] != 0:
            acumulador += dados['valor']
            count += 1

    media = acumulador/count

    return media

def contDias(dadosJson, media):

    numDias = 0

    for dados in dadosJson:
        
        if dados['valor'] > media:
            numDias += 1

    return numDias

def main(dadosJson):

    menor, maior = menorMaior(dadosJson)
    media = mediaFaturamento(dadosJson)
    numDias = contDias(dadosJson, media)

    print('Menor e maior valor de faturamento ocorrido no mês: {} ~ {}'.format(menor, maior))
    print('Número de dias em que o valor de faturamento diário foi superior à média mensal: ', numDias)

main(dadosJson)
