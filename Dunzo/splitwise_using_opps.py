class User:
    def __init__(self,username):
        self.__username=username
        self.__lent=0
        self.__owe=0

    def get_username(self):
        return self.__username
    
    def get_lent(self):
        return self.__lent

    def get_owe(self):
        return self.__owe

    def set_user_name(self,username):
        self.__username=username
    
    def set_len(self,lent):
        self.__lent=lent

    def set_owe(self,owe):
        self.__owe=owe