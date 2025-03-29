class Category:
    1# different budget : 
    #a-food
    #b-clothing
    #c-entertainment

    #instantiate  objects based on different budget categories
    def __init__(self, category):
        self.ledger = []
        self.category = category
      
    def data_ledger(self):    
        return self.ledger

    2# instance variavble - ledger - list
      
    3# method deposit - param : amount , description
    #no descrition default - emty string
    #append object to ledger list
    def deposit(self,amount,description=''):        
        data_deposit ={            
            'amount' : amount,
            'description' : description
        } 
        self.ledger.append(data_deposit)         
        return self.ledger
    4# method withdraw = deposit
    #amount passed in ledger as a negative number
    #not enough fund no added in ledger
    #return True if withdrawal, False otherwise
    def withdraw(self,amount,description=''):       
        if self.check_funds(amount):           
            #enough fund ,added in ledger 
            data_withdraw ={
                'amount' : -amount,
                'description' : description
            } 
            self.ledger.append(data_withdraw)  

            return True
        else:
            return False

    5# method get_balance
    #returns current balance - deposit + withdrawal
    def get_balance(self):
        total = sum(amt['amount'] for amt in self.ledger)
        return total


    6# method transfer - accepts amount + budjet category as arguments
    #-add withdrawal with the amount + description
    #if not enough funds, no added to ledgers
    #return True if transfer, False otherwise
    def transfer(self,amount,category):  
        if self.check_funds(amount):                
            if self.withdraw(amount,'Transfer to '+category.category):
                
                category.deposit(amount,'Transfer from '+self.category)
                return True
            else:
                return False
        return False


    #7 method check_funds - accept amount
    #-return false if amount > balance budget,categorty, 
    #-return True otherwise
    #this method can be used both withdraw and transfer
    def check_funds(self,amount):
        total = self.get_balance()
        if amount > total:
           return False
        else:
           return True

    #8 printed display
    # 30 character title- food is in the middle

    #list of item ledger-> description and amount
    
    #first 23 character of descriptin should be display , then amount right aline and 2 decimal places and max display 7 caracther
    def __str__(self):
        output_display=''
        len_category = len(self.category)
        title ='*' * (30-len_category)
        mid_title = (30-len_category) // 2
        output_display = title[:mid_title] +self.category+title[mid_title:]+'\n'
        for i in self.ledger:
            output_display += i['description'][:23] + str(format(i['amount'],'.2f').rjust(30-len(i['description'][:23]))) +'\n'
        output_display+='Total: '+str(self.get_balance())
        return output_display

    #total withdraw
    def total_withdraw_only(self):
        total = sum(amt['amount'] for amt in self.ledger if amt['amount'] < 0)
        return total 
    #total deposit
    def total_deposit_only(self):
        total = sum(amt['amount'] for amt in self.ledger if amt['amount'] > 0)
        return total         


def create_spend_chart(categories):
    #1 return string that is a bar chart
    chart=''
    chart='Percentage spent by category\n'
    left_percentage=''
    range_data = 11
    max_val= str(max(range(range_data))*10)
   
    
    data_categories = [i.category for i in categories]
      
    #2 the chart show the percentage spent in each category
    
    
    max_length = max(len(category) for category in data_categories)

    padded_categories = [category.ljust(max_length) for category in data_categories]

   
   
    #3 the percentage spent calculated for withdrawal and no deposit
   # Calculate total spending in each category
    total_spent = [abs(category.total_withdraw_only()) for category in categories]
    print(total_spent)
    total_funds = sum(total_spent)
    
    
    percentages = [(spending / total_funds * 100 // 10) * 10 for spending in total_spent] if total_funds > 0 else [0] * len(categories)
    
    

    for i in reversed(range(range_data)):
        chart+=str(i*10).rjust(len(str(max_val)))+"| "
        for percent in percentages:            
            chart += "o"+" "*2 if float(percent) >= i*10 else "   "
        chart += "\n"

    chart +=left_percentage +'-'.rjust(len(max_val)+2) + '-'*len(percentages)*3 
       
    chart+=''
    
    for i in range(max_length):
        chart+="\n"
        chart += " "*(len(max_val)+2)
        for category in padded_categories:            
            chart +=category[i] + " "*2
        #chart += "\n"

    return chart.rstrip("\n")  # Remove the last unnecessary newline
    #percentages = [math.ceil(p / 10) * 10 for p in percentages]  # Round up to nearest 10
    
    #4 0-100, bar show 'o'
    
    #5 the height of each bar rounded down to the nearest 10

    #6 horizontal between space bar is 2

    #7 each category name show vertically below bar

    #8 show title 'Percentage spent by category'

    #9 This function will be tested with up to four categories.


food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
Auto = Category('Auto')
Auto.deposit(1000, 'deposit')
Auto.withdraw(15)
print(food)
print(clothing)
print(Auto)
categories = [food,clothing,Auto]
print(create_spend_chart(categories))