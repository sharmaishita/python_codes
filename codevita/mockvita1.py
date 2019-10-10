s=input()
temp=s
q= int(input())
x =[]
while(q):
	t=list(input().split())
	t[1] = int(t[1])
	x.append(t)
	q-=1

res = []
t=[]
for i in x:
	#t=[]
	L1 = s[0 : i[1]] 
	L2 = s[i[1] :] 
	R1 = s[0 : len(s)-i[1]] 
	R2 = s[len(s)-i[1] : ] 
	if i[0] == 'L':
		s=L2 + L1
	else:
		s=R2 + R1
	res.append(s[0])
	print(s)

s=''.join(i for i in res)
print(s)
if s in temp :
	print('YES')
else:
	print('NO') 


