lista1 = [1,2,3,4,5,6]
lista2 = [4,5,6,7,8,9]

res = list(dict.fromkeys(lista1+lista2))

print(res)