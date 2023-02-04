def junta_vetores(a,b,c,tam1,tam2):
    k = 0
    for i in range(tam1):
        c[k] = a[i]
        k += 1
    for j in range(tam2):
        c[k] = b[j]
        k += 1
    return(k)

a = [1,2,3,4]
b = [7,1,9]
c = [0,0,0,0,0,0,0,0,0,0]
print(junta_vetores(a,b,c,4,3))
    
