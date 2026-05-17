# Exercício 2

produtos = {"arroz": 4, "feijao": 6, "leite": 9}

print("lists de produtos:", produtos)

produto = input("Qual produto deseja alterar? ")

if produto in produtos:
    novo_preco = float(input(f"Novo preço para '{produto}': R$ "))
    precos[produto] = novo_preco
    print("Dicionário:", produtos)
else:
    print("Produto não encontrado.")
