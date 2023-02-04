n = int(input('O número é: '))
contador = 0
while n > 1:
    n -= 1
    print('O número é: ', n)
    contador += 1
print('Foram impressos', contador, 'números')
