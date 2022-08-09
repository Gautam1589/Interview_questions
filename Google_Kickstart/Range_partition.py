def solve(self,n,nums,d,a,b,s1,s2):
        if s1==0 and s2==0:
            return True
        if n==0:
            return False
        if s in d:
            return d[s]
        
        d[s]=solve(n-1,nums,s-nums[n-1],d) or solve(n-1,nums,s,d)
        return d[s]


t=int(input())
for i in range(t):
    n,x,y=tuple(map(int,input().split()))
    s=(n*(n+1))//2
    if s%(x+y)!=0:
        print('Case #'+str(i+1)+':','IMPOSSIBLE')
    else:
        k=s//(x+y)
        s1=x*k
        s2=y*k
        nums=[]
        for i in range(1,n+1):
            nums.append(i)
        alan=[]
        barbara=[]
        solve(n,nums,{},alan,barbara,s1,s2)