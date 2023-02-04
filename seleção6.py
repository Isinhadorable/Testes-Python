a = float(input('O coeficiente "a" é: '))
b = float(input('O coeficiente "b" é: '))
c = float(input('O coeficiente "c" é: '))
delta = b ** 2 - 4 * a * c
raiz_1 = (-b + (delta ** 0.5)) / (2 * a)
raiz_2 = (-b - (delta ** 0.5)) / (2 * a)
if delta <= 0:
    print('não existem raízes reais')
else:
    print('As raízes são: ', raiz_1, "e", raiz_2)
