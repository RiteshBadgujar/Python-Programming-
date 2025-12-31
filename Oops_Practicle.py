#Create account class with 2 attribute - balance &account no.
#create method for debit, credit &printing  the balance

class Bank:

    def __init__(self,balance,acoount_no):
        self.balance=balance
        self.account_no=acoount_no
        
    def debit_money(self,amount):
        self.balance-=amount
        print("Rs.",amount,"wasDebited")
        print("Total balance =",self.get_balance())
        
    def credit_money(self,amount):
        self.balance+=amount
        print("Rs.",amount,"wae credited")
        print("total balance =",self.get_balance())
    
    def get_balance(self):
        return self.balance
    
        
acc1 = Bank(10000,2345)   
acc1.debit_money(5000)

acc1.credit_money(30000)

acc1.get_balance()