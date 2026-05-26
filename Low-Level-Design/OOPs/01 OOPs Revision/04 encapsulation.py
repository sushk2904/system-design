class Bank:
    def __init__(self, name:str, balance:int) -> None:
        self.name :str = name
        #private
        self.__balance :int = balance

    """We will have to create a gette function to access the balance now but still wont be 
    able to actually change the value of the balance parameter
                  This function is called *Getter* function"""
    #Getter
    def get_balance(self) -> None:
        print(f"the balance is {self.__balance}\n")
    
    #Setter
    def set_balance(self, new_amount:int) -> None:
        self.__balance =  new_amount
    
    def __isServerLive(self) -> bool:
        return True

    def deposit(self, amount:int) -> None:
        if self.__isServerLive == True:
            self.__balance += amount
            print(f"The current balance after depositing is {self.__balance}\n")
        else:
            print(f"Server is currently offline")
    def withdraw(self, amount:int) -> None:
        if amount > self.__balance:
            print("Insufficient Balance\n")
        else:
            self.__balance-=amount
            print(f"Amount withdrawn is {amount}, current balance is {self.__balance}\n")

b1 = Bank("Sushant", 10000)
b1.deposit(1000)
b1.get_balance()
b1.withdraw(7500)

"""b1.__isServerLive() try to run this, this will give error since it is a private method accessible
only internally not by external user"""