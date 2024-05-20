num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
if tot == 2:
    print('O número {} foi divisível {} vezes. Portanto ele é um número primo!'.format(num, tot))
print('O número {} foi divisível {} vezes'.format(num, tot))
