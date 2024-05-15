v = float(input('Digite a velocidade do carro: '))
if v > 80.0:
    m = (v - 80.0) * 7
    print('Você ultrapassou o limite de velocidade permitido que é 80km/h, a sua multa é de R${:.2f}'.format(m))
print('Tenha um bom dia! Dirija com segurança!')