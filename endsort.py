#lt=[int(x) for x in input().split()]
#print(lt)
lt=[4,5,1,2,8,3]
st=0
ht=[]
d=-1
for i in range(0,len(lt)-1):
    if(st==0):
        ht.append([])
        d=d+1
        print("")
        ln=1
        st=1
    if(lt[i] < lt[i+1]):
        print(lt[i],end=" ")
        ht[d].append(lt[i])
    else:
        print(lt[i],end=" ")
        ht[d].append(lt[i])
        st=0
if(st==0):
    print("")
    ht.append([])
    d=d+1
    ht[d].append(lt[-1])
    print(lt[-1])
else:
    ht[d].append(lt[-1])
    print(lt[-1])
print(ht)
   
