t_seg = int(input('Digite um tempo em segundos: '))

horas = (t_seg // 60) // 60
minutos = (t_seg // 60) % 60
segundos = t_seg - ((horas * 60) * 60 + minutos * 60)
print(f'Horas: {horas}\nMinutos: {minutos}\nSegundos: {segundos}')
