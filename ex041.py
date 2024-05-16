from datetime import datetime
ano_atual = datetime.now().year
ano_nascimento = int(input('Digite o ano de nascimento: '))
anos =ano_atual - ano_nascimento
if anos <= 9:
    print('Até 9 anos: MIRIM')
elif anos <= 14:
    print('Até 14 anos: INFANTIL')
elif anos <= 19:
    print('Até 19 anos: JUNIOR')
elif anos <=25:
    print('Até 25 anos: SÊNIOR')
else:
    print('Acima de 25 anos: MASTER')
