n=int(input())
b=list(map(int,input().split()))
s=set(b)
x= [ b.count(i) for i in s]
print(max(x))
