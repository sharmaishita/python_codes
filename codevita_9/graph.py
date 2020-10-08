def largestFactor(num):
    i = 2
    while i*i <= num:
        if(num%i == 0):
           return num//i
        i += 1
    return 1
n,m = map(int,input().split()) 
nliz, mliz, d = [n],[m], dict()
while nliz[-1]!=1 :
    nliz.append(largestFactor(nliz[-1]))
while mliz[-1]!=1 :
    mliz.append(largestFactor(mliz[-1]))
for i in mliz:
        d[i] = 1 if i not in d else d[i]+1
i,j = 0,0
while nliz[i] not in d:
    i += 1
while mliz[j] != nliz[i]:
    j += 1
print(i+j)
    
