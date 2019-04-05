# matrix transpose
def transpose(lt):
    #print(lt)
    m=len(lt)
    r=[]
    for i in lt[0]:
        r.append([])
    

    for i in range(len(lt)):
        for j in range(len(lt[i])):
            r[j].append(lt[i][j])

    return(r)
                       





print(transpose([[1,1,1],[2,2,2],[3,3,3]]))
