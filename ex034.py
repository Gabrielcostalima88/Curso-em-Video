sal = float(input('Digite o salário: '))
if sal > 1250.00:
    ns = (sal * 0.1) + sal
    print('Novo salário é R${:.2f}'.format(ns))
else:
    ns = (sal * 0.15) + sal
    print("Novo salário é R${:.2f}".format(ns))
