# Exercício 10

dados = {"wilkson": 18, "leticia": 19, "gustavo": 23, "prado": 18}
print("Dicionário inicial:", dados)
chave = input("Digite uma chave para remover com pop(): ")
removido = dados.pop(chave)
print(f"Removido com pop(): '{chave}' → {removido}")
print("Após pop():", dados)
item = dados.popitem()
print(f"Removido com popitem(): {item}")
print("Após popitem():", dados)
nova_chave = input("Nova chave para adicionar via update(): ")
novo_valor = int(input("Novo valor: "))
dados.update({nova_chave: novo_valor})
print("Dicionário final:", dados)
