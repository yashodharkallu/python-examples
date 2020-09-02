"""
This shows the usage of property decorators
Python @property is one of the built-in decorators.
The main purpose of any decorator is to change your class methods or attributes
in such a way so that the users need not make any additional changes in their code.
"""


class BankAccount:
    """ Without property decorators"""

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.total = self.name + " has " + self.balance + " dollars in the account"


rajesh = BankAccount("Rajesh", "10000")
rajesh.name = "Sunit"
print(rajesh.name)
print(rajesh.total)


class BankAccount:
    """ With property decorators"""

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    @property
    def total(self):
        return self.name + " has " + self.balance + " dollars in the account"


rajesh = BankAccount("Rajesh", "10000")
rajesh.name = "Sunit"
print(rajesh.name)
print(rajesh.total)


def attach_data(func):
    func.data = 3
    return func


# Mutate the function. Apply decorator to functions
@attach_data
def add(x, y):
    return x + y


print("add(2, 3) : ", add(2, 3))
print("add.data : ", add.data)


# class object as decotrator
class CallCount:
    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)


@CallCount
def hello(name):
    print("Hello {}".format(name))


hello("Roshith")
"""
@CallCount
This is equivalent to >> tst=CallCount(hello("Roshith"))
"""
hello("HelloAgain")
hello("HelloAgain!")
hello("HelloAgain!!")
print("Times we called hello() :",hello.count)


# Instance as a decotrator
class Trace:
    def __init__(self):
        self.enabled=True

    def __call__(self,f):
        def wrap(*args,**kwargs):
            if self.enabled:
                print("Calling {}".format(f))
            return f(*args,**kwargs)
        return wrap


tracer = Trace()


@tracer
def rotate_list(l):
    return l[1:] + [l[0]]





