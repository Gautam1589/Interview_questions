from splitwise_using_opps import *
class UserService:
    users=dict()

    max_owe_amt=0
    max_lent_amt=0
    max_owe_user=""
    max_lent_user=""

    def create_expense_list(self,expenses):
        for expense in expenses:
            u1=None
            u2=None

            if expense[0] not in self.users:
                u1=User(expense[0])
            else:
                u1=self.users[expense[0]]

            if expense[1] not in self.users:
                u2=User(expense[1])
            else:
                u2=self.users[expense[1]]

            amount=float(expense[2])
            u1.set_owe(amount+u1.get_owe())
            u2.set_lent(amount+u2.get_len())

            self.users[expense[0]]=u1
            self.users[expense[1]]=u2

            if self.max_owe_amt<u1.get_owe():
                self.max_owe_amt=u1.get_owe()
                self.max_owe_amt=u1.get_user_name()
        
            if self.max_lent_amt<u2.get_lent():
                self.max_lent_amt=u2.get_lent()
                self.max_lent_user=u2.get_user_name()
        return self.users