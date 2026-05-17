# Exercício 7

nomes_novos= input("Digite nomes separados por vírgula: ")
nomes = [nome.strip() for nome in nomes_novos.split(",")]
dicionario = dict.fromkeys(nomes, 0)
print("Dicionário criado com fromkeys():", dicionario)
