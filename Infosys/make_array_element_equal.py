#operation A[i]=A[j]
#time O(NlogN)

from heapq import *

def solve(n,k,a):
    if k>=n-1:
        return 1
    d={}
    for i in a:
        d[i]=d.get(i,0)+1

    heap=[]
    for i in d:
        heappush(heap,(d[i],i))

    while k>0 and heap:
        if heap[0][0]>k:
            break
        v,key=heappop(heap)

        k-=v

    return len(heap)
    #d.sort(key=lambda x:d[x])
    # for i in d:
    #     if k>0 and k>=d[i]:
    #         k-=d[i]
    #         d[i]=0

    # cnt=0
    # for i in d:
    #     if d[i]>0:
    #         cnt+=1
    # return cnt

if __name__=='__main__':
    n=int(input())
    k=int(input())
    a=list(map(int,input().split()))
    print(solve(n,k,a))