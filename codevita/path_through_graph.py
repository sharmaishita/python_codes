from math import sqrt
def func(n):
	i=2
	while i*i<=n:
		if not n%i:
			return n//i
		i+=1
	return 1
x,y=map(int,input().split())

