import copy
lt=[]
n= int(input())
for i in range(n):
        name = input()
        score = float(input())
        lt.append([score,name])
print(lt)
newlt=copy.deepcopy(lt)
lt.sort()
print(lt)
#print(newlt)

while( len(lt) > 1  and  lt[-1][0]==lt[-2][0]):
        lt.remove(lt[-1])
        n=n-1


if(n>1):
        score=lt[-2][0]
else:
        score=lt[-1][0]

i=0
while(i<len(newlt)):
        if(score== newlt[i][0]):
                 print(newlt[i][1])
        i=i+1 
