def percentRepresen(dados):

    total = 0

    for uf in dados:
        total += dados[uf]

    percentuais = {}

    for uf in dados:

        percentuais[uf] = (dados[uf] * 100)/total

    return percentuais

percentuais = percentRepresen({'SP': 67836.43, 'RJ': 36678.66, 'MG': 29229.88, 'ES': 27165.48, 'Outros': 19849.53})
print(percentuais)