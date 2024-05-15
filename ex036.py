valorC = float(input("Digite o valor da casa:"))
salario = float(input('Digite o salário:'))
anos = int(input('Digite a quantidade de anos para pagar:'))
vp = valorC / (anos * 12)
percentualSalario = salario * 0.3
if vp > percentualSalario:
    print('Financiamento negado! Parcela maior que 30% do salário. Valor da parcela {:.2f}'.format(vp))
else:
    print('O valor da prestação mensal ficou R${:.2f}, dividido em {} anos'.format(vp, anos))
