from pathlib import Path

nome_arquivo = 'tabela.txt'
tabela_arquivo = Path(nome_arquivo)
tabela_arquivo.touch(exist_ok=True)
i = 0

with open(nome_arquivo, 'r') as arquivo:
    linhas = arquivo.readlines()

    for linha in linhas:
        info = linha.split(';')
        print(f'[{i}] Nome: {info[0].strip()}  Idade: {info[1].strip()}')
        i += 1
