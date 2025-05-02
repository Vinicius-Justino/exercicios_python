def monta_torre(altura, coluna_inicial, coluna_destino):
    if altura == 1:
        print(f"{coluna_inicial} -> {coluna_destino}")
        return
    
    coluna_destino_torre_acima = [coluna for coluna in range(1, 4) if coluna not in [coluna_inicial, coluna_destino]][0]
    monta_torre(altura - 1, coluna_inicial, coluna_destino_torre_acima)
    print(f"{coluna_inicial} -> {coluna_destino}")
    monta_torre(altura - 1, coluna_destino_torre_acima, coluna_destino)

altura_torre = int(input("Altura da torre: "))
monta_torre(altura_torre, 1, 3)