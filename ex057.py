sexo = str(input('Digite seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'FM':
    sexo = str(input('Dados inválidos. Por favor informe o sexo [F/M]')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))