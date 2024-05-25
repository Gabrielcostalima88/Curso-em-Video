# gerador de PA
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
cont = 1
termo = p
while cont <= 10:
    print('{} => '.format(termo), end='')
    termo += r
    cont +=1
