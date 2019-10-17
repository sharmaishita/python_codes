import math
i = float(input())
n = int(input())
n-=2
acc=[]
while(n):
	l=[]
	l = input().split()
	l = [int(l[i]) if i != 2 else l[i] for i in range(4) ]
	acc.append(l)
	n-=1
i = float(input())
totali = i*365
ci=0
for i in acc:
	ci += 0.08 * i[3]
difi = totali-ci

#print(acc)

pos=0
for i in range(len(acc)):
	if acc[i][0] != (acc[i+1][0]-1) :
		pos = i
		break
#print(acc[pos+1])
if acc[pos+1][2] == 'debit':
	b2=acc[pos+1][3] + acc[pos+1][1]
else:
	b2=acc[pos+1][3] - acc[pos+1][1]
	
difi -= 0.08*b2

b1 = ((difi *100)/8)
a1 = b1-acc[pos][3]
a2 = b2-b1
if acc[pos][3] < b1:
	print (acc[pos][0]+1 , round(a1) , 'credit' , round(b1))
else:
	print (acc[pos][0]+1 , abs(round(a1)) , 'debit' , round(b1))
if b1 < b2:
	print (acc[pos][0]+2 , round(a2) , 'credit' , round(b2))
else:
	print (acc[pos][0]+2 , abs(round(a2)) , 'debit' , round(b2))
#print(b1,b2)
