print('Digite 999 para parar de informar números!')
cont = n = soma = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        cont += 1
        soma += n
print('Você digitou {} números e a soma deles é {}'.format(cont, soma))


