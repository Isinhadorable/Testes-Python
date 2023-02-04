lanterior = 0
c = 1
letra = input('Letra maiúscula: ')
while True:
    lanterior = letra
    letra = input('Letra maiúscula: ')
    c += 1
    if letra < lanterior:
        break
print(c)    
