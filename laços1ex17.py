p = int(input('Número p: '))
q = int(input('Número q: '))
c = 0
if p < q:
    print('a')
else:
    while p >= q:
        p -= q
        c += 1
print('O resultado da divisão é: ', c)

