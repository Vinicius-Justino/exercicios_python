altura, largura = [int(n) for n in input("Dimensões da matriz separadas por espaço: ").split(" ")]

linha_anterior = [0] * largura

for _ in range(altura):
    linha_atual = [0] * largura
    linha_atual[0] = 1

    for i in range(1, largura):
        linha_atual[i] = linha_atual[i - 1] + linha_anterior[i]
    
    linha_anterior = linha_atual.copy()

print(linha_anterior[-1])