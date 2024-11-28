
print(f"Welcome to Python Bank!")

class Banking:

    #Initial Account Holder and Balance using Constructor
    def __init__(self, user_name, initial_balance):

        self.name = user_name
        self.balance = initial_balance

        print(f"\nAccount Holder Name: {self.name}")
        print(f"Balance: ৳{self.balance}")


    #Deposit Amount Function
    def deposit(self, deposit_amount=0):

        if deposit_amount > 0:
            self.balance += deposit_amount
            return self.balance
        else:
            print(f"Sorry! You can't deposit ৳ {deposit_amount}.")


    #Withdrawal Amount Function
    def withdraw(self, withdraw_amount):

        if self.balance >= withdraw_amount:
            if  withdraw_amount > 0:
                self.balance -= withdraw_amount
                return self.balance
            else:
                print(f"Sorry! You can't withdraw ৳ {withdraw_amount}.")

        else:
            print(f"Withdrawal amount is exceed the available balance")

    #Balance Inquiry Function
    def get_balance(self):
        return self.balance

bankingObj = Banking("Golam Maula", 1000)

deposit_amount = int(input("\nEnter deposit amount: "))

bankingObj.deposit(deposit_amount)

if bankingObj.balance is not None: 
    print(f"After deposit, Balance: ৳{bankingObj.get_balance()}")

withdraw_amount = int(input("\nEnter withdraw amount: "))

bankingObj.withdraw(withdraw_amount)

if bankingObj.balance is not None: 
        print(f"After withdrawal, Balance: ৳{bankingObj.get_balance()}")





