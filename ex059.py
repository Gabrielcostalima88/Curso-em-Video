n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('''Qual a sua opção?
     [1] somar 
     [2] multiplicar 
     [3] maior 
     [4] novos números
     [5] sair. ''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma dos número {} e {} é: {}'.format(n1, n2,soma))
    if opcao == 2:
        multiplica = n1 * n2
        print('A multiplicação entre {} e {} é: {}'.format(n1, n2, multiplica))
    if opcao == 3:
        if n1 > n2:
            print('O maior valor é {}'.format(n1))
        else:
            print('O maior valor é {}'.format(n2))
    if opcao == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
print('Fim do programa! Volte sempre!')


