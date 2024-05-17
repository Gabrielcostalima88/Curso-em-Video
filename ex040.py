# calcula a média de 2 notas
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m < 5.0:
    print('Média abaixo de 5.0: REPROVADO!')
elif m >= 5 and m < 7:
    print('Média entre 5.0 e 6.9: RECUPERAÇÃO!')
else:
    print('Média 7.0 ou superior: APROVADO!')
