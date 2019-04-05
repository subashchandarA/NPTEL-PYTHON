#NPTEL_Flames_game
s1=input("Enter the first person name")
s2=input("Enter the second person name")
s1=s1.lower()
s1=s1.replace(" ","")
s2=s2.lower()
s2=s2.replace(" ","")

#print(s1,s2)
lt1=list(s1)
lt2=list(s2)

i=0
for x in range(len(lt1)):
   if lt1[i] in lt2:
       temp=lt2.index(lt1[i])
       lt1.pop(i)
       lt2.pop(temp)
   else:
       i=i+1
print(lt1,lt2)
n=len(lt1)+len(lt2)

lt=list("FLAMES")

while len(lt) >1:
    i=n%len(lt)
    lt.pop(i)
print(lt[0])
print(n)
