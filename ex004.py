n = int(input('Digite um número: '))

n_list = list((1, 1))

for i in range(2, n):
    n_list.append(n_list[i - 2] + n_list[i - 1])

print(n_list)
