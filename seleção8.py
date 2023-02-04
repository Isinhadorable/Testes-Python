a = float(input('O valor da reta "a" é: '))
b = float(input('O valor da reta "b" é: '))
c = float(input('O valor da reta "c" é: '))
if a > ((c - b) ** 2) ** (0.5) and a < ((c + b) ** 2) ** (0.5):
    print('formam')
elif b > ((a - c) ** 2) ** (0.5) and b < ((a + c) ** 2) ** (0.5):
    print('formam')
elif c > ((a - b) ** 2) ** (0.5) and c < ((a + b) ** 2) ** (0.5):
    print('formam')
else:
    print('não formam')
