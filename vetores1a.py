def copia_vetor(a,b,tam):
    for i in range(tam):
        b[i]=a[i]

a = [1,2,3]
b = [0,0,0]
copia_vetor(a,b,3)
print(b)
