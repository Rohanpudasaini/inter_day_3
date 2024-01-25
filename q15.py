# 15. Imagine you are designing a banking application. What would a
# customer look like? What attributes would she have? What methods
# would she have?
class Bank:
    def __init__(self, name="Bank Bank", phone_no:str= "+123456", total_number_of_account:int= 0) -> None:
        self.name = name
        self.phone_no = phone_no
        self.total_number_of_account = total_number_of_account

    def get_total_number_of_account(self):
        return self.total_number_of_account
    def increase_account_count(self):
        self.total_number_of_account +=1

# class Account(Bank):
    # def __init__(self, userId:int, total_ammount:float, type_of_account:str):

class Account(Bank):
    def __init__ (self, userId, total_amount, type_of_account):
        self.userId = userId
        self.total_amount = total_amount
        self.type_of_account = type_of_account
        super().__init__()
        super().increase_account_count()

# class Test(Account):
#     def __init__(self, userId, total_amount, type_of_account):
#         super().__init__(userId, total_amount, type_of_account)
    
class User(Account):
    def __init__ (self, first_name, last_name, account_no, total_amount:int=500, type_of_account:str="checking"):
        self.first_name = first_name
        self.last_name = last_name
        self.account_no = account_no
        self.total_amount = total_amount
        self.type_of_account = type_of_account
        super().__init__(userId=self.account_no, total_amount=self.total_amount, type_of_account= type_of_account)

    def deposit_money(self, money:int):
        self.total_amount += money
        print(f"Deposited {money}rs sucessfully")


    def withdraw_money(self, money:int):
        if money > 0 and self.total_amount > money:
            self.total_amount -= money
            print(f"Withdraw {money}rs sucessfully")
        else:
            print("Something went wrong!!!!!")

    def print_user_info(self):
        return f"The user {self.first_name} {self.last_name} have a {self.type_of_account} account with account number {self.account_no} and currently have {self.total_amount} in their account"

user1 = User("Rohan", "Pudasaini", 123)
print(user1.get_total_number_of_account())
print(user1.print_user_info())


        