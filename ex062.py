# gerador de PA
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
cont = 1
termo = p
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} => '.format(termo), end='')
        termo += r
        cont +=1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total) )