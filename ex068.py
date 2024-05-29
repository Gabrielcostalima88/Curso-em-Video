# jogo par e ímpar
from random import randint
v = 0
while True:
    sort = randint(0,10)
    jogador = int(input('Digite um valor: '))
    tot = jogador + sort
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {sort}. Total de {tot}')
    if tipo == 'P':
        if tot % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if tot % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')