alan=int(input())
wish=list(map(int,input().split()))
teacher=[]
c=0
a=wish[0]
for i in range(1,alan):
    teacher.append([a,wish[i]])
for i in range(len(teacher)):
    if(teacher[i][0]+teacher[i][1]>=teacher[i][0]*teacher[i][1]):
        c+=1
print(c)
