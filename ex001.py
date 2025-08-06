reais = int(input('Digite uma quantidade de reais: R$'))

print(f'Notas de R$100: {reais // 100}\nNotas de R$50: {(reais % 100) // 50}')
print(f'Notas de R$10: {(reais % 50) // 10}\nNotas de R$1: {(reais % 10) // 1}')
