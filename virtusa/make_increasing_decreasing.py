n,k=tuple(map(int,input().split()))
num=list(map(int,input().split()))

res=[]
num.sort()
for i in range(n):
    if i==k:
        break
    res.append(num[i])
for i in range(n-1,-1,-1):
    if i==k-1:
        break
    res.append(num[i])
print(res)
