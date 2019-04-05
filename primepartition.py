def isprime(x):
  for i in range(2,x):
    if(x%i ==0):
      return (False)
  else:
    return (True)

def primepartition(m):
  if(m < 2):
    return (Fasle)
  lt=[]
  for i in range(2,m) :
    if(isprime(i)):
      lt.append(i)
  print(lt)
  for i in range(0,len(lt)):
    for j in range(0,len(lt)):
      if(i != j and lt[i]+lt[j] == m):
        return (True)
  return (False)

m=72
print(primepartition(m))
