#tabuada
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    for c in range(1,11):
            print(f"A sua tabuada é: {n} x {c} = {n*c}")
print('Programa tabuada encerrado. Volte sempre!')
