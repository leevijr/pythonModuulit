def parilliset(lista):
    palautusLista=[]
    for x in lista:
        if not x%2:
            palautusLista.append(x)
    return palautusLista



listani=[-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(listani)
print(parilliset(listani))