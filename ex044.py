# calculadora fora de pagamento
print('{:=^40}'.format(' LOJAS ARAUJO '))
valor = float(input('Digite o valor do produto: R$'))
print('''Escolha uma das opções abaixo como forma de pagamento:
[1] - À vista DINHEIRO / CHEQUE. 10% DESCONTO
[2] - À vista cartão 5% DESCONTO
[3] - 2x CARTÃO PREÇO NORMAL
[4] - 3x ou mais  CARTÃO 20% ACRÉSCIMO''')
opcao = int(input('Selecione a forma de pagamento:'))
if opcao == 1:
    resultado = valor - (valor * 0.1)
    print('Valor a ser pago com 10% de desconto R${:.2f}'.format(resultado))
elif opcao == 2:
    resultado = valor - (valor * 0.05)
    print('Valor a ser pago com 5% de desconto R${:.2f}'.format(resultado))
elif opcao == 3:
    print('Valor a ser pago em 2x no cartão R${:.2f}'.format(valor))
elif opcao == 4:
    resultado = valor + (valor * 0.2)
    print('O valor a ser pago em 3x ou mais com acréscimo de 20% fica R${:.2f}'.format(resultado))
else:
    print('Valor inválido')



