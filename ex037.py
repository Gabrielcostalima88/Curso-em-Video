# conversor de decimal
n = int(input('Digite um número inteiro:'))
d = int(input('Você deseja converter o número digitado em qual base? 1-Binário, 2- Octal, 3- Hexadecimal '))
if d == 1:
    print('O número {} transformado em binário é {}'.format(n, bin(n)))
elif d == 2:
    print('O número {} transformado em octal é {}'.format(n, oct(n)))
elif d == 3:
    print('O número {} transformado em hexadecimal é {}'.format(n, hex(n)))
else:
    print('Valor inválido')

