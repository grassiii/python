def lista_opcoes():
    print('[1] Soma')
    print('[2] Subtração')
    print('[3] Multiplicação')
    print('[4] Divisão')
    print('[5] Sair')
    return int(input('Escolha uma opção: '))


def valores():
    n = list()
    n.append(int(input('Digite um número: ')))
    n.append(int(input('Digite outro número: ')))
    return n


match(lista_opcoes()):
    case 1:
        n = valores()
        print(f'{n[0]} + {n[1]} = {n[0] + n[1]}')
    case 2:
        n = valores()
        print(f'{n[0]} - {n[1]} = {n[0] - n[1]}')
    case 3:
        n = valores()
        print(f'{n[0]} x {n[1]} = {n[0] * n[1]}')
    case 4:
        n = valores()
        print(f'{n[0]} / {n[1]} = {n[0] / n[1]}')
    case 5:
        print('Programa encerrado...')
    case _:
        print('Digite um número válido!')
