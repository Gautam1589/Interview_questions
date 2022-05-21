s=input()
vowel=['a','e','i','o','u']
con=[]
for i in range(97,123):
    if chr(i) not in vowel:
        con.append(chr(i))
n=len(con)

l=list(s)
for i in range(len(l)):
    flag=0
    if l[i] in vowel:
        l[i]=l[i].upper()
    elif l[i].lower() in con:
        if isupper(l[i]):
            flag=1
        l[i]=con[(con.index(l[i])+3)%n]
        if flag==1:
            l[i]=l[i].upper()
            
        
print(s)
print(''.join(l))
print(s)

