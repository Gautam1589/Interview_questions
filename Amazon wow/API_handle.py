def API(logs):
    res=[]
    reg={}
    login=set()
    logout=set()
    for i in logs:
        s=i.split()
        if s[0]=='register':
            if s[1] not in reg:
                reg[s[1]]=s[2]
                res.append('Registered Successfully')
            else:
                res.append('Username already exists')
        elif s[0]=='login':
            if s[1] in reg and reg[s[1]]==s[2] and s[1] not in login:
                login.add(s[1])
                res.append('Logged In Successfuly')
            else:
                res.append('Login Unsuccessful')
        else:
            if s[1] in reg and s[1] in login:
                login.remove(s[1])
                res.append('Logged Out Successfully')
            else:
                res.append('Logout Unsuccessful')

    return res 

n=int(input())
logs=[]
for i in range(n):
    s=input()
    logs.append(s)
print(API(logs))
