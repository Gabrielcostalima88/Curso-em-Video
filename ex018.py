import math
n = float(input('Digite um número:'))
seno = math.sin(math.radians(n))
cosseno = math.cos(math.radians(n))
tan = math.tan(math.radians(n))
print('O ângulo de {} tem o SENO de {:.2f} '.format(n, seno))
print('O ângulo de {} tem o COSSENO de {:.2f} '.format(n, cosseno))
print('O ângulo de {} tem a TANGENTE de {:.2f} '.format(n, tan))
