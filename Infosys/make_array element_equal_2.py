#operation A[i]=A[i]-1  A[j]=A[j]+1
#time O(n)
def solve(n,a):
    avg=sum(a)//n
    for i in range(n):
        a[i]-=avg
    
    if sum(a)==0:
        return n
    return n-1

if __name__=='__main__':
    n=int(input())
    a=list(map(int,input().split()))
    print(solve(n,a))