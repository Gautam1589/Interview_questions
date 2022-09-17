
def Min(s):
    d={}
    for i in s:
        d[i]=d.get(i,0)+1
    l=[]
    for i in d:
        l.append([i,d[i]])
    l.sort(key=lambda x:x[1],reverse=True)
    k1,k2=1,0
    cnt=0
    for i in l:
        if k2==9:
            k1+=1
            k2=0
        cnt+=i[1]*k1
        k2+=1
    return cnt
    

s=input()
print(Min(s))
