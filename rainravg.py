def rainaverage(lt):
    d={}
    dct={}
    for t in lt:
        city=t[0]
        rain=t[1]
        if city in d:
            d[city]=(d[city]*dct[city]+rain)/(dct[city]+1)
            dct[city]=dct[city]+1
            
        else:
            d[city]=rain*1.0
            dct[city]=1
    newlt=[]
    for k in sorted(d):
        newlt=newlt+[(k,d[k])]

    return (newlt)

lt=rainaverage([(1,2),(1,3),(2,3),(1,1),(3,8)])
print(lt)
