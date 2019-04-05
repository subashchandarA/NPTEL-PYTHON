def intreverse(n):
    r=0
    while(n>0):
        x=n%10
        r=r*10+x
        n=n//10
    return(r)
x=int(input("enter a number "))
k=intreverse(x)
print("reverse ",k)
