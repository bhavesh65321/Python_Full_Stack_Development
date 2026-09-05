#Encapsulation Implementation ##
#Encapsulation is the process of wrapping up variables and method into single entity, its put restriction on accessing variables and method directly and 
#prevent the accidential modification, an object variable can be change by an object method. 
#Ex - Account department
#1.public - anywhere is the project
#2.private - within the same module
#3.protected - within the same class

# class Account:
#     def __init__(self,name, age, balance : int) -> None:
#         self.name : str = name
#         self.age : int = age
#         self.balance : int = balance ## public attribute it voilates the encapsulation principle because it can be accessed directly from the object. and its modifiy the critical data.

#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}, Balance: {self.balance}")


# account = Account("John", 20, 1000)
# account.display()
# account.balance = 0
# account.display()


##getter method - when any attribute is private or non accessiable, to access that attribute we use getter method
##setter method - when we want to update private attribute then we use setter method.

class Account:
    def __init__(self,name, age, balance : int) -> None:
        self.name : str = name
        self._age : int = age ## protected attribute it can be accessed within the class and its child class.
        self.__balance : int = balance ## now balance is private attribute so it can't be directly accessiable by object.
        self.__total : int = 1000000

    
    def get_balance(self):  ## getter method
        return self.__balance

    def set_balance(self, balance): ## setter method
        self.__balance = balance
        print(f"the current balance is {balance}")

    #private method
    def __CompleteBankBalance(self):
        self.__total += self.__balance
        print(f"Bank total is {self.__total}")

        


    

    

    # def display(self):
    #     print(f"Name: {self.name}, Age: {self.age}, Balance: {self.__balance}")


# account = Account("John", 20, 1000)
# # print(account.__balance)  ## can't accessible dsirectly
# print(account.get_balance())
# account.set_balance(3000)
# print(account._age) ## protected attribute can be accessed within the class and its child class.



class FixedAccount(Account):
    def __init__(self,name, age, balance : int) -> None:
        super().__init__(name, age, balance)
        self.__balance = 100000
    

FA = FixedAccount("John", 20, 1000)
print(FA.get_balance())





