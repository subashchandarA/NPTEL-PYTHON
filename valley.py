# strictly decreasing and then strictly increasing only
#decreasing and increasing length min 2 each

def valley(lt):
    if(len(lt)<3):
        return ( False)
    

    for i in range(len(lt)-1):
        if lt[i]>lt[i+1]:
            point=i
            continue
        else:
            point=i
            break
    else:
        print("decreasing only ")
        return ( False )
    if point==0:
        return ( False)
    
    for j in range (point,len(lt)-1):
        if lt[j]<lt[j+1]:
            np=j
            continue
        else:
            np=j
            return (False)
    else:
        return(True)
    
    if np==point :
        return(False)
    else:
        return (True)
   
print(valley([5,11,12,14]))
