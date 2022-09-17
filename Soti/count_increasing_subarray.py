class Count:
    def __init__(self):
        self.cnt=0

    def solve(self,a,m,n):
        vis=set()
        self.ans=[]
        dirn=[(0,1),(1,0)]
        for i in range(m):
            for j in range(n):
                if (i,j) not in vis:
                    self.dfs(i,j,a,vis,dirn,[])
        print(self.ans)
##        return ans%1000000007
        return 0

    def dfs(self,i,j,a,vis,dirn,l):
        if i==len(a)-1 and j==len(a[0])-1:
            self.ans.append(l)
            return
        vis.add((i,j))
        l.append(a[i][j])

        for x in dirn:
            I=i+x[0]
            J=j+x[1]
            if I<0 or J<0 or I>=len(a) or J>=len(a[0]) or (I,J) in vis:
                continue
            if a[I][J]>a[i][j]:
                self.dfs(I,J,a,vis,dirn,l)

m=2
n=2
a=[[1,2,3],[4,5,6],[7,8,9]]
obj=Count()
print(obj.solve(a,m,n))
