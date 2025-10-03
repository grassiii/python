from pathlib import Path

nome_arquivo = 'animais.txt'
animais_arquivo = Path(nome_arquivo)
animais_arquivo.touch(exist_ok=True)

animal = input('Digite o nome de um animal: ')

with open(animais_arquivo, 'r') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        if linha.strip() == animal:
            print(f'{animal} foi encontrado na lista!')
            break

