class Customer:
    last_id=0
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        Customer.last_id += 1
        self.id = Customer.last_id

    def __repr__(self):
        return 'Customer[{},{},{}]'.format(self.id, self.firstname, self.lastname)


class Account:
    last_id = 0
    def __init__(self, customer, type_of_account):
        self.customer = customer
        Account.last_id += 1
        self.id = Account.last_id
        self.type_of_account = type_of_account
        self._balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise IncorrectAmountException("Incorrect amount", self._balance)
        self._balance += amount

    def calc_interest(self, t):
        if self.type_of_account == 'SavingAccount':
            print("Your interest in account %s in %s years is [%s]" % (self.id, t, self._balance * (1.1 ** t - 1)))
            self._balance = self._balance * 1.1 ** t
        else:
            print('Your account does not have interest')

    def charge(self, amount):
        if amount < 0:
            raise IncorrectAmountException("Incorrect amount", self._balance)
        if amount > self._balance:
            raise InsufficientBalanceException("Insufficient Balance, current balance is: ", self._balance)
        self._balance -= amount

    def __repr__(self):
        return '{}[{},{},{},{}]'.format(self.__class__.__name__, self.id, self.customer.lastname, self._balance, self.type_of_account)

class Bank:
    def __init__(self):
        self.account_list = []
        self.customer_list = []

    def create_customer(self, firstname, lastname):
        c = Customer(firstname, lastname)
        self.customer_list.append(c)
        return c

    def create_account(self, customer, type_of_account):
        a = Account(customer, type_of_account)
        self.account_list.append(a)
        return a


    def transfer(self, acco_id1 , acco_id2, amount):
        if amount < 0:
            raise IncorrectAmountException("Incorrect amount")
        for account in self.account_list:
            if account.id == acco_id1:
                if amount > account._balance:
                    raise InsufficientBalanceException("Insufficient Balance, current balance is: " + str(account._balance), account._balance)
                account._balance -= amount

        for account in self.account_list:
            if account.id == acco_id2:
                account._balance += amount





    def __repr__(self):
        return 'Bank[{},{}]'.format(self.customer_list, self.account_list)


class BankException(Exception):
    def __init__(self, msg, balance=-100):
        super().__init__(msg)
        self.balance = balance

class IncorrectAmountException(BankException):
    pass

class InsufficientBalanceException(BankException):
    pass



bank = Bank()

c1 = bank.create_customer('Anna', 'Smith')
print(c1)
c2 = bank.create_customer('John', 'Brown')
print(c2)
a1 = bank.create_account(c1, 'CheckingAccount')
print(a1)
a2 = bank.create_account(c2, 'SavingAccount')
print(a2)

try:
    a2.deposit(1000)
    a1.deposit(100)
    print(a1)
    print(a2)
    a2.calc_interest(5)
    a1.calc_interest(5)
    bank.transfer(2, 1, 500)
    print('-------')
    print(bank)
    print('-------')
    a1.charge(200)
    print(a1)
    a1.charge(150)
    print(a1)
except IncorrectAmountException as iae:
    print('Incorrect.. Exception raised: ' + str(iae))
except InsufficientBalanceException as iae:
    print('Exception raised: ' + str(iae))
