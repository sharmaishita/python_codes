import math
def maxfact(num):
    ret = 1
    i = 2
    while i <=int(math.sqrt(num)+1):
        if(num%i == 0):
           ret = num//i
           break
        i += 1
    return ret
n,m = map(int,input().split()) 
nliz, mliz = [n],[m]
d = {}
while nliz[-1]!=1 :
    nliz.append(maxfact(nliz[-1]))
while mliz[-1]!=1 :
    mliz.append(maxfact(mliz[-1]))
for i in mliz:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
i,j = 0,0
while nliz[i] not in d:
    i += 1
while mliz[j] != nliz[i]:
    j += 1
print(i+j)
    
