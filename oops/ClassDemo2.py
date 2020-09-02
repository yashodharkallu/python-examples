#!/usr/bin/python

class BankAccount(object):
    defaultAccNumber = 1        # Class Attribute

    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
        self.accountNumber = BankAccount.defaultAccNumber
        BankAccount.defaultAccNumber = BankAccount.defaultAccNumber + 1

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print('Not enough balance!')
        else:
            self.balance -= amount

    def getBalance(self):
        return self.balance

if __name__ == '__main__':
    myObj = BankAccount('Omkar', 1000)
    myObj.deposit(1000)
    print(myObj.getBalance())
    myObj.withdraw(500)
    print(myObj.getBalance())

print("\n____________________________________Abstract Base Classes (abc)_____________________________________________")

"""
Abstract class to serve as a “skeleton” for a subclass
  - instantiating the base class is impossible; and
  - forgetting to implement interface methods in one of the subclasses raises an error as early as possible.
"""
import abc              # Abstract Base Classes (abc)


class My_ABC_Class(object):
    """
    To create an Abstract Base Class, set the `__metaclass__` magic method
    to `abc.ABCMeta`. This will mark the respective class as an AbstractBase Class.
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def set_val(self, val):
        return

    @abc.abstractmethod
    def get_val(self):
        return

# Abstract Base Class defined above ^^^

# Custom class inheriting from the above Abstract Base Class, below

class MyClass(My_ABC_Class):

    def set_val(self, input):
        self.val = input

    def get_val(self):
        print("\nCalling the get_val() method")
        print("I'm part of the Abstract Methods defined in My_ABC_Class()")
        return self.val

    def hello(self):
        print("\nCalling the hello() method")
        print("I'm *not* part of the Abstract Methods defined in My_ABC_Class()")

my_class = MyClass()

my_class.set_val(10)
print(my_class.get_val())
my_class.hello()