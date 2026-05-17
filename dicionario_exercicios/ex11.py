
usuarios = {"dudu": 50, "dede": 29, "dinho": 27}
opcao = ""
while opcao != "0":
    print("\n--- MENU ---")
    print("1  - Exibir todos os usuários")
    print("2  - Buscar usuário (get)")
    print("3  - Adicionar usuário")
    print("4  - Atualizar idade")
    print("5  - Remover usuário (pop)")
    print("6  - Remover último inserido (popitem)")
    print("7  - Criar cópia e alterar valor (copy)")
    print("8  - Inicializar com fromkeys")
    print("9  - Atualizar com outro dicionário (update)")
    print("10 - Limpar todos os dados (clear)")
    print("11 - Criar dicionário com dict() e tuplas")
    print("0  - Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        print("Nomes  (keys)  :", list(usuarios.keys()))
        print("Idades (values):", list(usuarios.values()))
        print("Pares  (items) :", list(usuarios.items()))
    elif opcao == "2":
        nome = input("Nome do usuário: ")
        resultado = usuarios.get(nome, "Usuário não encontrado.")
        print("Resultado:", resultado)
    elif opcao == "3":
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        usuarios[nome] = idade
        print("Usuário adicionado:", usuarios)
    elif opcao == "4":
        nome = input("Nome do usuário a atualizar: ")
        if nome in usuarios:
            nova_idade = int(input("Nova idade: "))
            usuarios[nome] = nova_idade
            print("Dicionário atualizado:", usuarios)
        else:
            print("Usuário não encontrado.")
    elif opcao == "5":
        nome = input("Nome do usuário a remover: ")
        if nome in usuarios:
            removido = usuarios.pop(nome)
            print(f"Removido: '{nome}' → {removido}")
            print("Dicionário:", usuarios)
        else:
            print("Usuário não encontrado.")
    elif opcao == "6":
        if usuarios:
            item = usuarios.popitem()
            print("Removido com popitem():", item)
            print("Dicionário:", usuarios)
        else:
            print("Dicionário vazio.")

    elif opcao == "7":
        if usuarios:
            copia = usuarios.copy()
            nome = input("Qual usuário da cópia deseja alterar? ")
            if nome in copia:
                nova_idade = int(input("Nova idade na cópia: "))
                copia[nome] = nova_idade
            print("Original:", usuarios)
            print("Cópia   :", copia)
        else:
            print("Dicionário vazio.")
    elif opcao == "8":
        entrada = input("Nomes separados por vírgula: ")
        nomes = [n.strip() for n in entrada.split(",")]
        idade_padrao = int(input("Idade padrão: "))
        novo_dic = dict.fromkeys(nomes, idade_padrao)
        print("Criado com fromkeys():", novo_dic)
        usuarios.update(novo_dic)
        print("Dicionário principal após update():", usuarios)
    elif opcao == "9":
        qtd = int(input("Quantos usuários informar? "))
        novos = {}
        for i in range(qtd):
            nome = input(f"  Nome {i + 1}: ")
            idade = int(input(f"  Idade {i + 1}: "))
            novos[nome] = idade
        usuarios.update(novos)
        print("Dicionário após update():", usuarios)
    elif opcao == "10":
        confirmacao = input("Tem certeza? (sim/não): ")
        if confirmacao == "sim":
            usuarios.clear()
            print("Dicionário limpo:", usuarios)
    elif opcao == "11":
        qtd = int(input("Quantos pares informar? "))
        tuplas = []
        for i in range(qtd):
            nome = input(f"  Nome {i + 1}: ")
            idade = int(input(f"  Idade {i + 1}: "))
            tuplas.append((nome, idade))
        novo = dict(tuplas)
        print("Criado com dict():", novo)
        substituir = input("Substituir o dicionário principal? (sim/não): ")
        if substituir == "sim":
            usuarios = novo
            print("Dicionário principal:", usuarios)
    elif opcao == "0":
        print("Encerrando. Até logo!")
    else:
        print("Opção inválida.")
