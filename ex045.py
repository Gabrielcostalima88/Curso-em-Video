# pedra papel tesoura
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Digite a sua jogada: '))
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('jogador jogou {} '.format(itens[jogador]))
print('-=' * 11)
if computador == 0: #pedra
    if jogador == 0:
        print('EMPATOU!, TENTE NOVAMENTE')
    if jogador == 1:
        print('JOGADOR VENCEU!')
    if jogador == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1: # papel
    if jogador == 0:
        print('COMPUTADOR VENCEU!')
    if jogador == 1:
        print('EMPATOU!, TENTE NOVAMENTE')
    if jogador == 2:
        print('JOGADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2: #tesoura
    if jogador == 0:
        print('JOGADOR VENCEU!')
    if jogador == 1:
        print('COMPUTADOR VENCEU!')
    if jogador == 2:
        print('EMPATOU!, TENTE NOVAMENTE')
    else:
        print('JOGADA INVÁLIDA')
else:
    print('JOGADA INVÁLIDA!')
