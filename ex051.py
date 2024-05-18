i = int(input('Digite o primeiro termo: '))
p = int(input('Digite a razão: '))
cont =  i + (10 - 1) * p
for c in range(i, cont + p , p):
    print('{} '.format(c), end='=> ')
print('FIM')
