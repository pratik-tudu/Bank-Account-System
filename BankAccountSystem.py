class BankAccount:
    defaultAccNumber=1
    dict_pin={}  # dict to store pin of diff accounts
    acc_transaction={}   # creating a dict to store transactions inside a list as a value and acc no as key
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        self.accountNumber=self.defaultAccNumber
        BankAccount.defaultAccNumber+=1
        print(f"Account created for {self.name}.")
        print(f"Initial balance: {self.balance}")
        BankAccount.__genPin(self)
        self.acc_transaction[self.accountNumber]=[]   # sets the value of transaction dict as a list
        self.acc_transaction[self.accountNumber].append(f"Initial Balance: {self.balance}")

    def deposit(self,amount):
        print(f"Deposit: {amount}")
        self.balance+=amount
        self.acc_transaction[self.accountNumber].append(f"Deposited {amount}    --  Updated Balance : {self.balance}")  
    def withdraw(self,amount):
        pin=input("Enter 4 digit pin: ")
        orgpin=BankAccount.dict_pin[self.accountNumber]
        if(pin==orgpin):
            if(self.balance>=amount):
                self.balance-=amount
                print(f"Withdraw: {amount}")
                self.acc_transaction[self.accountNumber].append(f"Withdrawl {amount}    --  Updated Balance : {self.balance}")
            else:
                print("Not enough balance!")
        else:
            print("Incorrect pin!")
    def getBalance(self):
        print(f"Balance: {self.balance}")
    def __genPin(self):
        while(True):
            pin=input("Create 4 digit Pin: ")
            if pin.isdigit() and len(pin)==4:
                BankAccount.dict_pin[self.accountNumber]=pin
                break
            else:
                print("Invalid Key! Key must be of 4 digits.")
        

    
    def showTransaction(self,acc_no):
        if not BankAccount.acc_transaction:
            print("NO transactions yet.")
        elif acc_no in BankAccount.acc_transaction:
            print("===== Transactions =====")
            lst=BankAccount.acc_transaction[acc_no]
            for val in lst:
                print(val)
        else:
            print("No transactions for this account no.")

    def pinChange(self,old,new):
        orgpin=BankAccount.dict_pin[self.accountNumber]
        if(orgpin==old):
            if not(new.isdigit() and len(new)==4):
                print("Invalid Key! Pin must be of 4 digits")
            elif (new==old):
                print("New pin cannot be same as last pin.!")
            else:
                BankAccount.dict_pin[self.accountNumber]=new
                print("Pin changed successfully.")
        else:
            print("Incorrect old pin!")



accounts={}
while(True):
    print("\n=== Bank System ===")
    print("Enter 1 to Create Account.")
    print("Enter 2 to Access Account")
    print("Enter 3 to show accounts")
    print("Enter 4 to Exit!.")
    
    choice=input("Enter choice: ")

    if(choice=="1"):
        name=input("Enter Name: ")
        balance=float(input("Enter initial balance: "))
        acc=BankAccount(name,balance)
        accounts[acc.accountNumber]=acc
    elif(choice=="2"):
        acc_no=int(input("Enter Account no: "))
        if acc_no in accounts:
            acc=accounts[acc_no]

            while(True):
                print(f"\n --- Welcome {acc.name} ---")
                print("1. Deposit ")
                print("2. Withdraw ")
                print("3. Check Balance ")
                print("4. Show Transactions")
                print("5. Change Pin")
                print("6. Back")

                sub_choice=input("Enter choice: ")

                if(sub_choice=="1"):
                    amt=float(input("Enter Amount to Deposit: "))
                    acc.deposit(amt)
                elif(sub_choice=="2"):
                    amt=float(input("Enter Amount to withdraw: "))
                    acc.withdraw(amt)
                elif(sub_choice=="3"):
                    acc.getBalance()
                elif(sub_choice=="4"):
                    acc.showTransaction(acc_no)
                elif(sub_choice=="5"):
                    old=input("Enter Old Pin: ")
                    new=input("Enter new Pin: ")
                    acc.pinChange(old,new)
                elif(sub_choice=="6"):
                    break
                else:
                    print("Invalid choice!")
            
        else:
            print("Account not found!")

    elif(choice=="3"):
        if not accounts:
            print("NO accounts to show.")
        else:
            for acc in accounts.values():
                print(f"Acc no: {acc.accountNumber}, Name: {acc.name}, Balance: {acc.balance}")


    elif(choice=="4"):
        print("Thanks for using Banking system...")
        break

    else:
        print("Invaid choice!")





