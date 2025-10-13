moedas = [int(n) for n in input("Valores das moedas separados por espaço: ").split(" ")]
numero_alvo = int(input("Número desejado: "))

reparticoes = [0] * (numero_alvo+1)
reparticoes[0] = 1
for numero in range(1, numero_alvo+1):
    for moeda in moedas:
        if numero - moeda < 0:
            continue

        reparticoes[numero] += reparticoes[numero - moeda]

print(reparticoes[numero_alvo])