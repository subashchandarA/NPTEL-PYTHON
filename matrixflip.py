        

def matrixflip(mlt,d):
  lt=[]
  for e in mlt:
      lt.append(e[:])
 
  if(d=='h') :
     for i in range(len(lt)):
        lt[i].reverse()
     return(lt)
  nlt=[] 
  if(d=='v'):
     for i in range(len(lt)-1,-1,-1):
        print(lt[i])
lt=[[1,2],[3,4],[5,6]]
print(matrixflip(lt,'v'))
print(lt)
