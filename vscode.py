import pandas as pd
from pathlib import Path

caminho_arquivo = Path('alunos.csv')
if not caminho_arquivo.exists():
    with open(caminho_arquivo, 'w') as arquivo:
        arquivo.write('')

with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write('Nome,Idade\n')
    arquivo.write("Gabriela,20\n")
    arquivo.write("Diego,25\n")
    arquivo.write("Isabela,22\n")
    arquivo.write("Ana,20\n")
    arquivo.write("Henrique,24\n")
    arquivo.write("Bruno,22\n")
    arquivo.write("Carla,19\n")
    arquivo.write("Joao,26\n")
    arquivo.write("Felipe,23\n")
    arquivo.write("Eduarda,21\n")

with open('alunos.csv', 'r') as arquivo:
    linhas = arquivo.readlines()
    df = pd.read_csv('alunos.csv')
    df_ordenado = df.sort_values(by='Nome').reset_index(drop=True)
    print(df_ordenado)
    print('\nPessoa mais velha do arquivo: ')
    print(df.loc[[df['Idade'].idxmax()]].to_string(index=False))
    print('\nPessoa mais nova do arquivo: ')
    print(df.loc[[df['Idade'].idxmin()]].to_string(index=False))