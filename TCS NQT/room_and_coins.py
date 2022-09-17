def solve(arr,n,k):
    l,r=0,0
    curr=0
    while r<n:
        curr+=arr[r]
        if curr==k:
            return [l+1,r+1]
        elif curr<k:
            r+=1
        else:
            l+=1
    return -1


n,k=tuple(map(int,input().split()))
arr=list(map(int,input().split()))
print(solve(arr,n,k))
