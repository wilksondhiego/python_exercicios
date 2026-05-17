# Exercício 5

dados = {"banana": "amarelo", "feijao": "marrom", "melancia": "vermelha"}
print("Dicionário atual:", dados)
resposta = input("deseja excluir o dicionario? (sim/não): ")
if resposta == "sim":
    dados.clear()
print("final:", dados)
