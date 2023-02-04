n = int(input('O número é: '))
dois_dmd = n % 100
dois_dme = (n - dois_dmd) // 100
soma = dois_dme + dois_dmd
raiz = soma * soma
if raiz == n:
    print('sim')
else:
    print('não')
  
