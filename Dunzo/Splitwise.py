import csv
file=open('splitwise.csv')
csvreader=csv.reader(file)

expenses=[]

for expense in csvreader:
    expenses.append(expense)

print(expenses)

users=dict()

for expense in expenses:
    u1=expense[0]
    if u1 not in users:
        users[u1]=[0,0]
    u2=expense[1]
    if u2 not in users:
        users[u2]=[0,0]

max_owe_amt=0
max_lent_amt=0
max_owe_user=""
max_lent_user=""

for expense in expenses:
    u1=expense[0]
    u2=expense[1]
    amount=float(expense[2])

    users[u1][0]+=amount
    users[u2][1]+=amount

    if max_owe_amt<users[u1][0]:
        max_owe_amt=users[u1][0]
        max_owe_amt=u1
    
    if max_lent_amt<users[u2][1]:
        max_lent_amt=users[u2][1]
        max_lent_user=u2

print(users)
print(max_owe_user)
print(max_lent_user)