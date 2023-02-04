n = int(input('Forneça o número: '))
nanterior = 0
restoanterior = -1
c = 0
resto = 0
while True:
    c += 1
    if c > 0:
        nanterior = n
        n = n % 10
        restoanterior = resto
        resto = (n % 2)
    if resto != restoanterior:
        print('possui')
        break
    else:
        print('não possui')
        break
    
