def issorted1(lt):    
  for i in range(len(lt)-1):
    if lt[i] <= lt[i+1] :
      continue
    else:
      return(False)
  return(True)

from random import randint

n=int(input())
lt=[]

for i in range(n):
    lt.append(int(input()))
              
                        
while not issorted1(lt) :
            i=randint(0,len(lt)-1)
            j=randint(0,len(lt)-1)
            lt[i],lt[j]=lt[j],lt[i] 

for i in lt:
            print(i,end="")
            
