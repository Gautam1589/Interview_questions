#uber coding round

#taxy scheduling
def find_trips(time,arr):
    t=0
    for i in arr:
        t+=(time//i)
    return t

def binary_search(n,arr):
    low=0
    high=max(arr)*n
    while low<high:
        mid=(low+high)//2
        trips=find_trips(mid,arr)
        if trips>n:
            high=mid
        else:
            low=mid+1
    return high
        
if __name__=='__main__':
    n=int(input())
    arr=list(map(int,input().split()))
    print(binary_search(n,arr))
