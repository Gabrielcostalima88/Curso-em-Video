from itertools import count
nome = str(input('Digite um nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {} '.format(nome.upper()))
print('Seu nome em minúsculas é {} '.format(nome.lower()))
print('Seu nome tem {} letras.'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))