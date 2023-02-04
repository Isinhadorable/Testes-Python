nanterior = 0
n = 1
c = 0
n = int(input('número: '))
while n !=0:
    divisão = n % 10 
    nanterior = divisão
    n = n // 10
    if nanterior <= n % 10:
        print('não')
        break
