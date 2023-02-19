a1 = int(input('Введите первый номер члена a1: '))
d = int(input('Введите разность ар.пр. : '))
k = int(input('Введите последний номер члена k: '))

result = []

for i in range(k):
    result.append(a1+i*d)

print('\nВсе члены прогрессии', ' '.join([str(x) for x in result])) 
