import random
class Customer:
    def _init_(self,name,address,contact_no):
        self.name=name
        self.address=address
        self.contact_no=contact_no
        self.accounts=[]

    def create_account(self,account_type,initial_balance):
        account_no=Bank.generate_account_no()
        account=BankAccount(account_type,initial_balance,self,account_no)
        self.account.append(account)
        return account
    def display_customer_info(self):
        print(f"Customer Name:{self.name}")
        print(f"Address:{self.address}")
        print(f"Contact Number:{self.contact_no}")
        print("Account:")
        for account in self.accounts:
            print(f" -{account}")
class BankAccount:
    def _init_(self,account_type,balance,owner,account_no):
        self.account_type=account_type
        self.balance=balance
        self.account_no=account_no
    def deposit(self,amount):
        self.balance+=amount
        print(f"Deposited INR {amount}.New balance:INR{self.balance}")
    def withdraw(self,amount):
        if amount<=self.amount:
            self.balance-=amount
            print(f"Withdrew INR {amount}.New balance:INR{self.balance}")
        else:
            print("Insufficient funds!")
    def _str_(self):
        return f"{self.account_type}Account - Account Number:{self.account_no},Balance:INR{self.balance}"
class Bank:
    def _init_(self,name):
        self.name=name
        self.customers=[]
    def add_customers(self,customer):
        self.customers.append(customer)
        @staticmethod
        def dispaly_bank_info(self):
            print(f"Bank name:{self.name}")
            print("Customers:")
            for customer in self.customers:
                customer.display_customer_info()
                print()
        def find_account_by_no(self,account_no):
            for customer in self.customers:
                for account in customer.accounts:
                    if account_no==account_no:
                        return account_no
                return None
    #Example usage
    if _name=="main_":
        #create a bank
        my_bank=Bank("My Bank")
        customer_list=[]
        while True:
            print("1.New Customer 2.Existing Customer 3.Find customers info4.Exit")
            try:
                choice=int(input())
                if choice==1:
                    print("Customer Registration: \n")
                    #create a customer
                    name=input("Enter cutomer name:")
                    address=input("Enter address:")
                    contact_no=input("Enter contact_no:")
                    customer_obj=Customer(name,address,contact_no)
                    customer_list.append(customer_obj)
                    my_bank.add_customer(customer_obj)
                    while True:
                        acc_type=int(input("Enter 1. To create saving account 2.To create checking account 3.Exit \n"))
                        if acc_type==1:
                            new_account=customer_obj.create_account("Savings",1000)
                            print(f"Savings account created with account_no:{new_account.account_no}\n")
                            break
                        elif acc_type==2:
                            new_account=customer_obj.create_account("Current",1000)
                            print(f"Current account created with account number:{new_account.account_number}\n")
                            break
                        elif acc_type==3:
                            break
                        else:
                            print("Invalid option... Try again")
                    if choice==2:
                        #User input for trasactions
                        account_number_input=input("Enter your account no:")
                        account_to_transact=my_bank.find_account_by_number(account_number_input)
                        if account_to_transact:
                            print(f"\nWelcome,{account_to_transact.owner.name}!")
                            print(account_to_transact)
                            while True:
                                print("1.Enter 1 to deposit\n2.Enter 2 to withdrawl\n3.Enter 3 to check the balance\n4 .Exit")
                                option=int(input("Enter your opinion:\n"))
                                if option==1:
                                    print("Welcome to deposit section\n")
                                    #Deposit
                                    deposit_amount=int(input("\nEnter the amount to deposit:INR"))
                                    account_to_transact.deposit(deposit_amount)
                                elif option==2:
                                    print("Welcome to withdrawl section:\n")
                                    #withdrawl
                                    withdrawl_amount=int(input("\n Enter the amount to withdraw:INR"))
                                    account_to_transact.withdraw(withdrawl_amount)
                                elif option==3:
                                    #Display updated account information
                                    print("\n Updated Account information:")
                                elif option==4:
                                    break
                                else:
                                    print("Invalid option")
                        else:
                            print("Account not found.")
                        if choice==3:
                            my_bank.display_bank_info()
                        elif choice==4:
                            break
                        else:
                            pass
            except ValueError:
                print("Invalid input.Please enter a valid option.")
                continue
