def intercala_vetores(a,b,c,tam1,tam2):
    k= 0
    j= 0
    for i in range(0,tam1):
        c[k] = a[i]
        k += 1
        if k > i:
            c[k] = b[j]
            j += 1
            k +=1
    return k
    

a =[1,2,3]
b =[5,7,8]
c = [0,0,0,0,0,0]
print(intercala_vetores(a,b,c,3,3))
print (c)
