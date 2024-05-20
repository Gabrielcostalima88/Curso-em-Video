soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
tot_mulher = 0
for p in range(1, 5):
    print('----- {}° PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]')).strip()
    soma_idade += idade
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mn' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        tot_mulher += 1
media_idade = soma_idade / 4
print('A média de idade do grupo é de {} anos, o homem mais velho tem {} anos e se chama {} e ao todo {} mulheres tem menos de 20 anos'.format(media_idade, maior_idade_homem, nome_velho, tot_mulher))
