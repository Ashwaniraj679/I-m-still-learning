class customers:
    def __init__(self,name, phone, bill):
        self.name = name 
        self.phone = phone 
        self.bill = bill 
    
    def add_amount(self,amount):
        self.bill += amount
        print(self.bill)
    def get_bill(self):
        return self.bill
d  = customers("Ravi","12",453)
print(customers.get_bill(d))