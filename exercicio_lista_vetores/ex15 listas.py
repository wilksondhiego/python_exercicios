lista = [1, 2, 3, 4, 5]
n = 2

lista_rotacionada = lista[-n:] + lista[:-n]

print(lista_rotacionada)