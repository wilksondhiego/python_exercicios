lista = [1, 2, 3]
def permutacoes (lista):
    if len(lista) == 1:
        return [lista]

    resultado = []

    for i in range(len(lista)):
        atual = lista[i]
        resto = lista[:i] + lista[i+1:]

        for p in permutacoes(resto):
            resultado.append([atual] + p)

    return resultado
