def listtype(l):
  return(type(l) == type([]))

def recflat(lt,item):
    for e in item:
        if listtype(e):
            recflat(lt,e)
        else:
            lt.append(e)
  
    

def flatten(x):
    rlt=[] 
    for item in x:
        if listtype(item):
            recflat(rlt,item)
        else:
            rlt.append(item)
    return (rlt)
    




l=flatten([1,2,[3],[4,[5,6]]])
print(l)
l=flatten([1,2,3,(4,5,6)])
print(l)
