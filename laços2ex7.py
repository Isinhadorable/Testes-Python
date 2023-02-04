n = int(input('Forneça o número: '))
if n == 2 or n == 3:
        print('primo')
for i in range (2,n-1):
    if n % i == 0:
        print('não primo')
        break
    else:
        print('primo')
        break
