      
class Bank:
    number_of_user = {}
    balance = 0
    loan_amount = 0
    is_loan_open = True
    def __init__(self,name) -> None:
        self.name = name
        
    def create_account(self,name,email,password,primary_deposit):
        self.account_number = 1000+len(Bank.number_of_user)
        self.person = {}
        Bank.balance+=primary_deposit
        self.person["name"] = name
        self.person["email"] = email
        self.person["password"] = password
        self.person["balance"] = primary_deposit
        Bank.number_of_user[self.account_number] = self.person
        print(f"Account Created Successfully ! \n Your account number is: {self.account_number}")

    def see_all_user(self):
       all_key = Bank.number_of_user.keys()
       for k in all_key:
            value = Bank.number_of_user[k]
            print(f"Name: {value["name"]} || Balance: {value["balance"]}")

class User(Bank):
    def __init__(self,name,email,password,primary_deposit) -> None:
        self.name = name
        self.email = email
        self.primary_deposit = primary_deposit
        self.password = password
        self.loan = 0
        self.history ={}
        self.history["1. primary_deposit"]=primary_deposit
        self.create_account(name,email,password,primary_deposit)
        super().__init__(name)
    def check_balance(self,account_number):
        print(Bank.number_of_user[account_number]["balance"])
    def deposit(self,amount,account_number):
        Bank.balance+=amount
        Bank.number_of_user[account_number]["balance"]+=amount
        self.history[str(len(self.history)+1)+". deposit amount"] = amount
    def withdraw(self,amount, account_number):
        Bank.balance-+amount
        Bank.number_of_user[account_number]["balance"]-=amount
        self.history[str(len(self.history)+1)+". withdraw amount"] = amount
    
    def check_history(self):
        for key,value in self.history.items():
            print(key,value)
    
    def take_loon(self,amount,account_number):
        if self.is_loan_open and amount/2 <= Bank.number_of_user[account_number]["balance"]:
            print(f"Your loan is request {amount} is accepted.")
            Bank.balance-=amount
            Bank.loan_amount+=amount
        else:
            print(f"Your balance is {Bank.number_of_user[account_number]["balance"]}. So your loan amount can't be more then {Bank.number_of_user[account_number]["balance"]*2}")
    
    def transfer_balance(self,amount,sender_account_number, receiver_account_number):
        Bank.number_of_user[sender_account_number]["balance"]-=amount
        Bank.number_of_user[receiver_account_number]["balance"]+=amount

class Admin(Bank):
    def check_balance(self):
        print(self.balance)
    def check_total_loan(self):
        print(self.loan_amount)
    def turn_on_off_loan_feature(self):
        if Bank.balance<=Bank.loan_amount:
            Bank.is_loan_open = False

# Creating a bank 
bank = Bank("JONOTA")

# creating user account 
user1 = User("shawon","shawon@gmail.com",2342,1500)
user2 = User("Korim","Korim@gmail.com",2334,1000)

# after creating account checking the all user info
print("- "*30)
bank.see_all_user()

# checking balance using account number
print("- "*30)
user1.check_balance(1000)
user1.check_balance(1001)

# Deposit to the account using account_number with deposit amount
user1.deposit(3000,1000)
user2.deposit(5000,1001)

# after deposit checking the balance 
print("- "*30)
user1.check_balance(1000)
user1.check_balance(1001)

# withdraw from account using account_number and withdraw amount
user1.withdraw(1500, 1000)
user2.withdraw(2000,1001)

# after withdraw checking the balance 
print("- "*30)
user1.check_balance(1000)
user1.check_balance(1001)

# after those operation checking the account history 

user1.check_transaction_history()
print("- "*30)
user2.check_transaction_history()

# taking loan using account_number and loan amount base on condition first loan is rejected but second loan is accepted 

user1.take_loon(15000,1000)
user1.take_loon(5000,1000)



# Before transfer balance checking the balance
print("- "*30)
user1.check_balance(1000)
user1.check_balance(1001)

# transfer balance from one account to another account using sender_account_number and receiver_account_number with transfer amount

user1.transfer_balance(500,1000,1001)

# after transfer balance checking the balance
print("- "*30)
user1.check_balance(1000)
user1.check_balance(1001)


#________ADMIN_________#

admin = Admin("Maruf Khan")

admin.check_balance()

admin.check_total_loan()

# loan feature will be of if total loan is greater than total bank balance amount 
admin.turn_on_off_loan_feature()