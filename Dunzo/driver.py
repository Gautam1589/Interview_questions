from userservice import *
import csv
class Driver:
    expenses=[]
    user_service=UserService()
    def main(self):
        file=open('splitwise.csv')
        csvreader=csv.reader(file)

        for expense in csvreader:
            self.expenses.append(expense)
    
        users=self.user_service.create_expense_list(self.expenses)

        for username,user in users.items():
            print(username,"owes",user.get_owe())

        for username, user in user.items():
            print(username,"lent", user.get_lent())
        
        print(self.user_service.max_owe_user)
        print(self.user_service.max_lent_user)


if __name__=='__main__':
    driver=Driver()
    driver.main()
