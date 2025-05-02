chave = "?QUM!LVD? QPAIKSROD BTYWHJ?FE FE!NCZGBT ODVLXMUQP !ORS?IAP!"
matriz_chave = [[coluna for coluna in linha] for linha in chave.split()]

potenciais_cifras = {}
for caracter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ!?":
    potenciais_cifras[caracter] = []

for linha in range(len(matriz_chave)):
    for coluna in range(len(matriz_chave[linha])):
        letra_atual = matriz_chave[linha][coluna]

        for mod_linha,mod_coluna in [[1, 1], [1, 0], [0, 1]]:
            coords_flanco1 = [linha - mod_linha, coluna - mod_coluna]
            coords_flanco2 = [linha + mod_linha, coluna + mod_coluna]

            if not ((0 <= coords_flanco1[0] < len(matriz_chave)) and (0 <= coords_flanco1[1] < len(matriz_chave[linha]))):
                continue
            elif not ((0 <= coords_flanco2[0] < len(matriz_chave)) and (0 <= coords_flanco2[1] < len(matriz_chave[linha]))):
                continue

            flanco1 = matriz_chave[coords_flanco1[0]][coords_flanco1[1]]
            flanco2 = matriz_chave[coords_flanco2[0]][coords_flanco2[1]]

            potenciais_cifras[letra_atual].append("".join(sorted(flanco1 + flanco2)))

conta_ocorrencias = {}
for letra in potenciais_cifras.keys():
    for cifra in potenciais_cifras[letra]:
        try:
            if letra not in conta_ocorrencias[cifra]:
                conta_ocorrencias[cifra].append(letra)
        except KeyError:
            conta_ocorrencias[cifra] = [letra]

with open("correspondencias.txt", "w") as correspondencias:
    for letra in potenciais_cifras.keys():
        correspondencias.write(f"{letra}")

        for cifra in potenciais_cifras[letra]:
            if len(conta_ocorrencias[cifra]) == 1:
                correspondencias.write(f" {cifra}")
        
        correspondencias.write("\n")