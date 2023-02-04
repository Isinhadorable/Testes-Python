a = float(input('O valor da reta "a" é: '))
b = float(input('O valor da reta "b" é: '))
c = float(input('O valor da reta "c" é: '))
if a == b and a == c:
    print('equilátero')
elif (b > a and b == c) or (b < a and b == c):
    print('isósceles')
elif (c > a and a == b) or (c < a and a == b):
    print('isósceles')
else:
    print('escaleno')
    
