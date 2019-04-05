def matched(s):
  n=0
  max=0
  for c in s:
    if c == "(":
      n=n+1
      if max < n:
        max=n        
    if c == ")" :
      n=n-1
    if (n < 0):
      return(False,max)
  if n == 0:
    return (True,max)
  else:
    return (False,max)

  
def nestingdepth(s):
  res,m=matched(s)
  if res :
     return (m)
  else:
    return (-1)

print(nestingdepth(")(())("))
