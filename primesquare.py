def isprime(n):
  for i in range (2,n):
    if(n % i == 0):
      return (False)
  else:
    return(True)

def issquare(n):
   
    for i in range(1,n//2+1):
      if i*i == n :
        return(True)
    return(False)  
      
  
  
def primesquare(lt):
  
  if isprime(lt[0]) :
    for i in range(0,len(lt),2):
      if isprime(lt[i]) :
        continue
      else:
        return (False)
    for i in range(1,len(lt),2):
      if issquare(lt[i]) :
        continue
      else:
        return (False)
       
  else:
    for i in range(0,len(lt),2):
      if issquare(lt[i]) :
        continue
      else:
        return (False)
    for i in range(1,len(lt),2):
      if isprime(lt[i]) :
        continue
      else:
        return (False)
  return(True)    
res=primesquare([11,13,17])
print(res)


