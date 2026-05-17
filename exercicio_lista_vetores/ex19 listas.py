lista = [[1, 2, 3]]

def kadane(lista):

    max_atual = max_global = lista[0]

    for num in lista[1:]:
        max_atual = max(num, max_atual + num)
        max_global = max(max_global, max_atual)

    return max_global
