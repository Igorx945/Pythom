import os

def mostrarLista(lista):
    print("Lista atual:", lista)

def lista():
    lista = []
    while True:
        print(" Escolha uma opção:")
        print("1 - Adicionar item na lista")
        print("2 - Excluir um item da lista")
        print("3 - Mostrar lista")
        print("4 - Gravar lista")
        print("5 - Ler um arquivo de lista epecifico")
        print("6 - Sair")

        opc = input("Digite a opção desejada: ")

        if opc == '1':
            novo_item = input("Digite um novo item para adicionar na lista: ")
            lista.append(novo_item)
        elif opc == '2':
            itemExcluir = input("Digite o item a ser excluído da lista: ")
            if itemExcluir in lista:
                lista.remove(itemExcluir)
            else:
                print("O item não está na lista.")
        elif opc == '3':
            mostrarLista(lista)
        elif opc == '4':
            arquivo = input("Digite o nome do arquivo a ser gravado: ")
            try:
                with open(arquivo, 'w') as f:
                    f.write(str(lista))
                print("Lista gravada com sucesso no arquivo", arquivo)
            except Exception as e:
                print("Erro ao gravar o arquivo:", e)
        elif opc == '5':
            arquivos = os.listdir()
            print("Lista de Arquivos disponíveis:")
            for arquivo in arquivos:
                print(arquivo)
            arquivoEscolhido = input("Digite o nome do arquivo para ler: ")
            try:
                with open(arquivoEscolhido, 'r') as f:
                    lista = eval(f.read())
                    mostrarLista(lista)
            except Exception as e:
                print("Erro ao ler o arquivo:", e)
        elif opc == '6':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida.")
lista()