from random import randint
from time import sleep
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que vocÊ consegue adivinhar qual foi? ')
acertou = False
c = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    c += 1
    if computador < jogador:
        print('Digite um número menor!')
    if computador > jogador:
        print('Digite um número maior!')
    if jogador == computador:
        acertou = True
print('Acertou após {} tentativas'.format(c))