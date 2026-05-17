# Exercício 8

alunos = {"wilkson": 6, "yvis": 7.0, "pedro": 9.5}
print("Alunos cadastrados:", list(alunos.keys()))
nome = input("Digite o nome do aluno: ")
nota = alunos.get(nome, "Aluno não encontrado.")
print(f"Resultado para '{nome}':", nota)
