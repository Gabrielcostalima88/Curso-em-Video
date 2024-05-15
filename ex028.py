from random import randint
from time import sleep
secreto = randint(1,10)
n = int(input('Digite um número de 1 a 10:'))
print('Processando...')
sleep(2)
if n == secreto:
    print('Você acertou, parabéns!')
else:
    print('Você perdeu! Eu pensei no número {}'.format(secreto))
