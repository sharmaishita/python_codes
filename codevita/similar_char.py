n=int(input())
s=input()
q=int(input())
dic={}
pre=[]
for i in s:
	if i in dic:
		dic[i]+=1
	else:
		dic[i]=0
	pre.append(dic[i])
while(q):
	q-=1
	p=int(input())
	#c=s[:p-1].count(s[p-1])
	print(pre[p-1])
