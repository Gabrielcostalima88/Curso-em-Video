# calculadora IMC
peso = float(input('Digite o seu peso:'))
altura = float(input('Digite a sua altura:'))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu IMC está abaixo da média. {:.2f}'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC está ideal, {:.2f}'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC está um pouco acima, SOBREPESO {:.2f}'.format(imc))
elif imc >= 30 and imc <40:
    print('Seu IMC está em {:.2f}, OBESIDADE!'.format(imc))
else:
    print('Seu IMC é de {:.2f}, OBESIDADE MÓRBIDA!'.format(imc))

