def zera_ind_par(a,tam):
    for i in range(0,tam,2):
        a[i] = 0

a= [1,2,3,4,5]
zera_ind_par(a,5)
print(a)
