r = float(input('O raio da circunferência é: '))
l = float(input('O lado do quadrado é: '))
area_c = (3.14 * r) ** 2
area_q = l ** l
if area_q < area_c:
    print('esconde')
else:
    print('não esconde')
