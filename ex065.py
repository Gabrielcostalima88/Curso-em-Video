resp = 'S'
maior = cont = media = menor = soma_m = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    resp = str(input('Quer continuar? [S/N] ')).upper().strip() [0]
    cont += 1
    soma_m += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma_m / cont
print('Você digitou {} números e a média foi {:.2f} o maior valor é {} e o menor {}'.format(cont, media, maior, menor))
