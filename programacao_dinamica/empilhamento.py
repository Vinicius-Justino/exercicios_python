caixas = [(5,2,1), (2,5,3), (4,5,1), (3,4,1), (2,1,2), (4,1,2), (5,3,3), (4,1,5), (2,2,4)]

caixas_arrumadas = [caixas.pop(0)]
for _ in range(len(caixas)):
    caixa = caixas.pop(0)

    for i in range(len(caixas_arrumadas)):
        if caixa[0] < caixas_arrumadas[i][0]:
            caixas_arrumadas.insert(i, caixa)
        elif i == len(caixas_arrumadas) - 1:
            caixas_arrumadas.append(caixa)

alturas_pilhas = [caixa[2] for caixa in caixas_arrumadas]
for i in range(1, len(caixas_arrumadas)):
    pilhas_empilhaveis = [alturas_pilhas[j] for j in range(i) if caixas_arrumadas[j][0] < caixas_arrumadas[i][0] and caixas_arrumadas[j][1] < caixas_arrumadas[i][1]]
    alturas_pilhas[i] = max(pilhas_empilhaveis, default=0) + caixas_arrumadas[i][2]

print(max(alturas_pilhas))