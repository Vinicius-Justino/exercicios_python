with open("correspondencias.txt") as correspondencias:
    with open("cola.txt", "w") as cola:
        cola.write("const cola = { \n")
        while True:
            linha_atual = correspondencias.readline().split(" ")
            if len(linha_atual) == 1:
                break

            cola.write(f'"{linha_atual.pop(0)}": [')

            for cifra in linha_atual:
                cola.write(f'"{cifra[0:2]}"')

                if linha_atual.index(cifra) == len(linha_atual) - 1:
                    cola.write("],\n")
                else:
                    cola.write(", ")
            
        cola.write("} \n")
