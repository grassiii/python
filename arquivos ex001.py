from pathlib import Path

nome_arquivo = 'numeros.txt'
caminho_arquivo = Path(nome_arquivo)
caminho_arquivo.touch(exist_ok=True)

while True:
    item = input('Digite um número para adicionar a lista, ou "Sair" para encerrar o programa: ')
    if item.isnumeric():
        with open(caminho_arquivo, 'a') as arquivo:
            arquivo.write(item + '\n')
    elif item == 'Sair' or item == 'sair':
        with open(caminho_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            print('')
            for linha in linhas:
                print(linha.strip())
            print('\nPrograma encerrado...')
            break

