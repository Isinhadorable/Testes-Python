n = int(input('O número é: '))
contador = 0
n_menos_um = n - 1
while n_menos_um > 0:
    print('O número é: ', n_menos_um)
    contador += 1
    n_menos_um -= 1
print('Foram impressos', contador, 'números')
