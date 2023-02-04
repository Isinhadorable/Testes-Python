preço = float(input('Preço da unidade: '))

quant = int(input('Quantidade da peça: '))

soma1 = preço * quant

desc = soma1 * 0.1

total = soma1 - desc

print('O valor total a pagar é:', total)
