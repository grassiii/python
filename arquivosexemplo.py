def menuarquivos():
    print('\n[1] Adicionar linha.')
    print('[2] Ler linhas')
    print('[3] Deletar linhas')
    print('[4] Sair')
    return int(input('Digite a opção desejada: '))


while True:

    opc = menuarquivos()
    lista = []

    match opc:

        case 1:
            with open('arquivo.txt', 'a') as arquivo:
                new_text = input('Digite o texto que deseja adicionar ao arquivo: ')
                arquivo.write(new_text + '\n')
        case 2:
            with open('arquivo.txt', 'r') as arquivo:
                linhas = arquivo.readlines()
                print('\n')
                for linha in linhas:
                    print(linha.strip())
        case 3:
            palavra = input('Digite a palavra que deseja apagar: ')

            with open('arquivo.txt', 'r') as arquivo:
                linhas = arquivo.readlines()
                for linha in linhas:
                    if linha.strip() != palavra:
                        lista.append(linha)

            with open('arquivo.txt', 'w') as arquivo:
                arquivo.writelines(lista)

        case 4:
            print('Encerrando programa...')
            break
        case _:
            print('Opção inválida, por favor, digite uma opção válida!')
