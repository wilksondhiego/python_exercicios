# Exercício 1

pessoa = {"nome": "wilkson", "idade": 18, "cidade": "pará"}

print("Dicionário:", pessoa)

chave = input("Digite uma chave (nome / idade / cidade): ")

if chave in pessoa:
    print(f"Valor de '{chave}':", pessoa[chave])
else:
    print("indisponivel.")
