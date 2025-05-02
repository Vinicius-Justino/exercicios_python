palavra = input("Palavra para embaralhar: ")

anagramas_possiveis = []
def monta_anagramas(anagrama_atual):
    global palavra

    if (len(anagrama_atual) == len(palavra) - 1):
        global anagramas_possiveis

        anagrama_atual.append([indice for indice in range(len(palavra)) if indice not in anagrama_atual][0])
        anagramas_possiveis.append(anagrama_atual)
        return
    
    for i in [indice for indice in range(len(palavra)) if indice not in anagrama_atual]:
        novo_anagrama = anagrama_atual.copy()
        novo_anagrama.append(i)
        monta_anagramas(novo_anagrama)

monta_anagramas([])

with open(f"{palavra}.txt", "w") as saida:
    anagramas_anotados = []

    for anagrama in anagramas_possiveis:
        palavra_nova = ""

        for i in anagrama:
            palavra_nova += palavra[i]
        
        if palavra_nova not in anagramas_anotados:
            saida.write(f"{palavra_nova}\n")
            anagramas_anotados.append(palavra_nova)