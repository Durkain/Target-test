import json

with open("faturamento.json", encoding='utf-8') as new_json:
    faturamento = json.load(new_json)

day = []
value = []

for dado in faturamento:
    day.append(dado['dia'])
    value.append(dado['valor'])
    if dado['valor'] == 0.0:
        day.pop()
        value.pop()

fatMin = min(value)
indFatMin = value.index(fatMin)

fatMax = max(value)
indFatMax = value.index(fatMax)

fatMed = sum(value)/len(value)

indc = len(value)
count = []
i = 0
while i != indc:
    if float(value[i]) > float(fatMed):
        count.append(value[i])
    i += 1

print(f'O menor valor de faturamento ocorrido no dia {day[indFatMin]} foi de {fatMin}')
print(f'O menor valor de faturamento ocorrido no dia {day[indFatMax]} foi de {fatMax}')
print(f'O Número de dias no mês em que o valor de faturamento diário foi superior à média mensal é de {len(count)}')



