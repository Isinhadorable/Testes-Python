l = 0
c = 0
while l != '!':
    l = input('A letra é: ')
    print('Letra: ', l)
    if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u':
        c += 1
print('A quantidade de vogais lidas: ', c)
