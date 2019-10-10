# python_codes
To upload python codes
l=[]
size=int(input("Enter size"))
for i in range(0,size):
    num=int(input("Enter elemnets"))
    l.append(num)
print("List:",l)
ch=int(input("Enter your choice 1.Ascending or 2. Descending"))
if ch==1:
    for i in range(0,len(l)-1):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
                temp=l[i]
                l[i]=l[j]
                l[j]=temp
    print("List:",l)
if ch==2:
    for i in range(0,len(l)-1):
        for j in range(i+1,len(l)):
            if l[i]<l[j]:
                temp=l[i]
                l[i]=l[j]
                l[j]=temp
        
    print("List:",l)    

