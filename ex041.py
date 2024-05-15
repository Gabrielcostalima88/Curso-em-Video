from datetime import datetime
ano_atual = datetime.now().year
ano_nascimento = int(input('Digite o ano de nascimento: '))
anos =ano_atual - ano_nascimento
if anos <= 9:
    print('Até 9 anos: MIRIM')
elif anos > 9 and anos <= 14:
    print('Até 14 anos: INFANTIL')
elif anos > 14 and anos <= 19:
    print('Até 19 anos: JUNIOR')
elif anos == 20:
    print('Até 20 anos: SÊNIOR')
else:
    print('Acima de 20 anos: MASTER')
