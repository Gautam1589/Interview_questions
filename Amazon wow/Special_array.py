#Special Array

def reverse(num):

    s=0
    while n:
        r=n%10
        s=s*10+r
        n//=10
    return s

arr=list(map(int,input().split()))
cnt=0

for i in arr:
    for j in range(0,int(i)):
        if j+reverse(j)==int(i):
            cnt+=1
            break

print(cnt)

