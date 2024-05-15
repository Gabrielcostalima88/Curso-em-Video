d = float(input('Digite a distância em KM:'))
print('Você está prestes a fazer uma viagem de {}KM'.format(d))
if d <= 200:
   p = d * 0.50
else:
    p = d * 0.45
print('O valor da passagem é R${:.2f}'.format(p))
