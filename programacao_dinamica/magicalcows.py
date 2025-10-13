maximo_vacas, quantidade_fazendas, quantidade_visitas = [int(n) for n in input().split(" ")]
fazendas_dobrando = 0

fazendas = [int(input()) for _ in range(quantidade_fazendas)]
dias_visitas = [int(input()) for _ in range(quantidade_visitas)]

dias = [quantidade_fazendas]
for _ in range(max(dias_visitas)):
    fazendas_dobrando *= 2
    dias.append(len(fazendas) + fazendas_dobrando)

    for _ in range(len(fazendas)):
        fazenda = fazendas.pop(0)
        if fazenda * 2 <= maximo_vacas:
            fazendas.append(fazenda * 2)
        else:
            fazendas_dobrando += 2
            dias[-1] += 1

for i in dias_visitas:
    print(dias[i])