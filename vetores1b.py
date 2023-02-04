def soma_vetores(a,b,c,tam):
    for i in range(3):
        c[i] = a[i] + b[i]
    


a = [1,2,3]
b = [1,3,2]
c = [0,0,0]
soma_vetores(a,b,c,3)
print(c)
