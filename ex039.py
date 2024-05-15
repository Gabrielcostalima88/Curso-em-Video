from datetime import datetime
ano_atual = datetime.now().year
ano = int(input('Digite o seu ano de nascimento: '))
r = (ano_atual - ano)
if r < 18:
    print('Faltam {} anos para você alistar!'.format(18 - r))
elif r == 18:
    print('Esse é seu ano de alistamento!')
else:
    print('O seu ano de alistamento já passou faz {} anos'.format(r - 18))
