capacidade_elevador = int(input("Capacidade do elevador: "))

melhor_anterior = [0] * (capacidade_elevador+1)
melhores_preenchimentos = [0] * (capacidade_elevador+1)

for peso in [int(n) for n in input("Pesos separados por espaço: ").split(" ")]:
    for capacidade in range(1, capacidade_elevador+1):
        if (capacidade - peso) < 0:
            continue
        elif capacidade == peso:
            melhores_preenchimentos[peso] = max(1, melhor_anterior[peso])
        elif melhor_anterior[capacidade - peso] == 0:
            continue

        melhores_preenchimentos[capacidade] = max(melhor_anterior[capacidade - peso] + 1, melhor_anterior[capacidade])
    
    melhor_anterior = melhores_preenchimentos.copy()
    
melhor_preenchimento = melhores_preenchimentos[capacidade_elevador]
print(melhor_preenchimento if melhor_preenchimento > 0 else "impossivel")