tempo_estudado = 0
hrs_min = input().split(':')
hrs_min = [int(x) for x in hrs_min]
horas = str(hrs_min[0])
minutos = str(hrs_min[1])
tempo_estudado = horas+":"+minutos
print(tempo_estudado)