moedas = [int(n) for n in input("Valores das moedas separados por espaço: ").split(" ")]
soma_alvo = int(input("Soma desejada: "))

minimo_moedas = [soma_alvo+1] * (soma_alvo+1)
minimo_moedas[0] = 0
for soma in range(1, soma_alvo+1):
    for moeda in moedas:
        if (soma - moeda) < 0:
            continue

        minimo_moedas[soma] = min(minimo_moedas[soma - moeda] + 1, minimo_moedas[soma])

print(minimo_moedas[soma_alvo])