from datetime import datetime


class Account:
    """Simple Account class with balance"""

    @staticmethod
    def _current_time():
        return datetime.now().strftime("%d-%b-%Y %H:%M:%S")

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_list.append((Account._current_time(), -amount))
        else:
            print('Amount must be more than 0 and no more than balance!')

    def show_balance(self):
        print('Account statement:')
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = 'deposit'
            else:
                tran_type = 'withdraw'
                amount *= -1
            print('{} | {} | {}'.format(date, tran_type, amount))


if __name__ == '__main__':
    sunit = Account('Sunit', 0)
    sunit.deposit(1000)
    sunit.withdraw(500)
    sunit.deposit(1000)
    sunit.show_balance()
