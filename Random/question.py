class Credit:
    def __init__(self,cn,ch,bank,expiry_date,balance,limit):
        self.__card_number=cn
        self.__card_holder=ch
        self.__bank=bank
        self.__expiry_date=expiry_date
        self.__balance=balance
        self.__limit=limit

    def get_card_number(self):
        return self.__card_number
    def get_card_holder(self):
        return self.__card_holder
    def get_bank(self):
        return self.__bank
    def get_expiry_date(self):
        return self.__expiry_date
    def get_balance(self):
        return self.__balance
    def get_limit(self):
        return self.__limit
    def set_balance(self,amt):
        self.__balance=self.__balance+amt

def make_payment(card_list,p,pd):
    max_=-1
    flag=0
    for card in card_list:
        if card.get_expiry_date()[::-1]>pd[::-1]:
            rem=card.get_limit()-card.get_balance()
            if max_< rem and p<=rem:
                max_=rem
                obj=card
                flag=1
    if flag==1:
        obj.set_balance(p)
        return obj
    else:
        return None
    

if __name__=='__main__':
    n=int(input())
    card_list=[]
    for i in range(n):
        cn=input()
        ch=input()
        bank=input()
        expiry=input()
        balance=int(input())
        limit=int(input())
        card=Credit(cn,ch,bank,expiry,balance,limit)
        card_list.append(card)
    
    payment=int(input())
    payment_date=input()
    res=make_payment(card_list,payment,payment_date)
    if res==None:
        print("Payment not Completed")
    else:
        print("Card details after payment")
        print(res.get_card_number(),",",res.get_limit()-res.get_balance(),",",res.get_balance())