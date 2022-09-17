k=int(input())
l1=list(map(int,input().split()))
for i in range(k):
    max1=0
    for j in range(i,len(l1)):
        if max1<l1[j]:
            max1=l1[j]
            element=j
    if element!=i:
        l1[i],l1[element]=l1[element],l1[i]
print("".join(map(str,l1)))
    
    
