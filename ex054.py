from datetime import date
atual = date.today().year
tot_maior = 0
tot_menor = 0
for c in range(1, 8):
    nasc = int(input('Digite o ano de nascimento da {}º pessoa: '.format(c)))
    idade = atual - nasc
    if idade >= 21:
        tot_maior += 1
    else:
        tot_menor += 1
print('Existem {} maiores de idade e {} menores idade'.format(tot_maior, tot_menor))
