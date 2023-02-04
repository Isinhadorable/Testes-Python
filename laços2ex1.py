numero =int(input('Número natural: '))
contador = 1
t = 0 
while t  < numero:
    t = contador * (contador + 1) * (contador + 2)
    contador += 1
if t == numero:
        print('triangular')
else:
        print('não triangular')
