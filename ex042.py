# tipo triângulo
l1 = float(input('Digite o primeiro seguimento:'))
l2 = float(input('Digite o segundo seguimento:'))
l3 = float(input('Digite o terceiro seguimento:'))
if l1 < l3 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os seguimentos acima podem formar um triângulo.', end='')
    if l1 == l2 and l2 == l3:
        print('EQUILÁTERO')
    elif l1 != l2 != l3 != l1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os seguimentos acima não podem formar um triângulo.')
