#pattern

n=int(input())

for i in range(n):
    for j in range(n):
        if i==0 and j==n-1:
            print('*')
        elif i==0 or i==n-1:
            print('*',end='')
        elif j==0:
            print('*',end='')
        elif j==n-1 and i!=0 and i!=n-1:
            print('*')
        else:
            print(' ',end='')
