l1=list(map(int,input().split(', ')))
l2=list(map(int,input().split(', ')))

res=''
i,j=0,0

while i<len(l1) and j<len(l2):
    res+=str(l1[i]+l2[j])
    if i<len(l1)-1 or j<len(l2)-1:
        res+=','
    i+=1
    j+=1
while i<len(l1):
    res+=str(l1[i])
    if i<len(l1)-1:
        res+=','
    i+=1
while j<len(l2):
    res+=str(l2[j])
    if j<len(l2)-1:
        res+=','
    j+=1
print(res)
