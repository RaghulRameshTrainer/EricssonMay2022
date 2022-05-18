class Account():
    def __init__(self,name,pan,deposit):
        self.name=name
        self.pan=pan
        self.__balance=deposit  #public, protected(_) , private(__)
        self.user=pan[:4]+name
        self.password=name+'@123'

    def getBalance(self):
        return self.__balance
    def setBalance(self,amt):
        self.__balance=self.__balance+amt