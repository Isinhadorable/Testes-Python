n = int(input('Forneça um número: '))
divisão = 0
resultado = ""
while n != 0:
    divisão = n // 2
    resto = n % 2
    n = divisão 
    resultado = str(resto) + resultado
print(resultado)

