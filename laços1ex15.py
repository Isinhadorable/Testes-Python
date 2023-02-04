n = int(input('Número: '))
c = 1
while True:
    if (c * c) > n:
        c -= 1
        break
    c +=1
print(c * c)
