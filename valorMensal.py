valores = [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]
estados = ["SP", "RJ", "MG", "ES", "Outros"]
porcentagem = []
ind = len(valores)
totalVal = sum(valores)

i = 0
while i != int(ind):
    porcentagem = valores[i] * 100 / totalVal
    print(f"O valor percentual de representação dentro do valor total mensal da distribuidora ao estado de {estados[i]} é de {porcentagem}.")
    i += 1





