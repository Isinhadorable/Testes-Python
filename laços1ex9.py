n = int(input('Número: '))
cont = 0
a = 0
s = n
while cont < n: 
    cont += 1
    s += 1
    if s % 2 == 0:
        a += s
print ('A soma dos números pares: ', a)
