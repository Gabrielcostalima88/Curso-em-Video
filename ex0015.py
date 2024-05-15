km = float(input('Qual a quantidade de km rodado? '))
dias = int(input("Quantidade de dias alugado? "))
total = (km * 0.15) + (dias * 60)
print('Você tera que pagar, R${:.2f}'.format(total))
