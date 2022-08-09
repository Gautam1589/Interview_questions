
t=int(input())
for j in range(t):
    n=int(input())
    old_pass=input()
    old_pass=list(old_pass)

    sp,up,lw,dig=0,0,0,0
    for i in old_pass:
        if i.isupper():
            up+=1
        elif i.islower():
            lw+=1
        elif i.isdigit():
            dig+=1
        elif i in ['@','#','*','&']:
            sp+=1
    
    if len(old_pass)>=7:
        if up==0:
            old_pass.append('A')
        if lw==0:
            old_pass.append('a')
        if sp==0:
            old_pass.append('@')
        if dig==0:
            old_pass.append('1')
    elif len(old_pass)<7:
        if up==0:
            old_pass.append('A')
        if lw==0:
            old_pass.append('a')
        if sp==0:
            old_pass.append('@')
        if dig==0 or len(old_pass)<7:
            k=1
            while len(old_pass)<7:
                old_pass.append(str(k))
                k+=1
    
    print('Case #'+str(j+1)+':',''.join(old_pass))
        











    # if len(old_pass)<7:
    #     k=1
    #     for j in range(len(old_pass),7+1):
    #         old_pass.append(str(k))
    #         k+=1
    # old_pass.extend(['a','A','@'])
    # print('Case #'+str(i+1)+':',''.join(old_pass))