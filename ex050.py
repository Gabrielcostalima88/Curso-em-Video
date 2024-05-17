s = 0
for c in range(0,7):
    v = int(input('Digite um valor'))
    if v % 2 == 0:
        s = s + v
print('A soma dos números pares digitados foi {}'.format(s))
