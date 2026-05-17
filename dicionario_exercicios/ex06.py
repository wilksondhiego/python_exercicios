# Exercício 6

dicionario = {"nome": "wilkson", "idade": 18, "curso": "Engenharia de softwarer"}
copia = dicionario.copy()
chave = input("Qual chave da cópia deseja alterar? (nome / idade / curso): ")
novo_valor = input(f"Novo valor para '{chave}': ")
copia[chave] = novo_valor
print("Original:", dicionario)
print("Cópia:", copia)
