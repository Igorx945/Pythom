lista = []
while True:
    print("Opções:")
    print("1. Adicionar um item à lista")
    print("2. Remover um item da lista")
    print("3. Exibir a lista")
    print("4. Gravar lista")
    print("5. Sair")

    escolha = int(input("Digite sua escolha (1-5): "))

    if escolha == 1:
        novo_item = input("Digite o item a ser adicionado: ")
        lista.append(novo_item)
        print("Item adicionado!")

    elif escolha == 2:
        if len(lista) > 0:
            remove_item = input("Digite o item a ser removido: ")
            if remove_item in lista:
                lista.remove(remove_item)
                print("Item removido!")
            else:
                print("Item não encontrado na lista.")
        else:
            print("Lista vazia.")

    elif escolha == 3:
        print("Lista atual:")
        print(lista)
    elif escolha == 4:
        nome_arq = input("Digite o nome do arquivo")
        with open(nome_arq,"w") as arquivo:
            for item in lista:
                arquivo.write(item+"\n")
        print("Arquivo gravado com sucesso!",nome_arq)
    elif escolha == 5:
        print("Até mais!")
        break
    else:
        print("Escolha inválida. Por favor, tente novamente.")
