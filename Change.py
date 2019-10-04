class Change:

    def __init__(self, dollars = 0, quarters = 0, dimes = 0, nickels = 0, pennies = 0):
       self.dollars = dollars
       self.quarters = quarters
       self.dimes = dimes
       self.nickels = nickels
       self.pennies = pennies

    def __str__(self):
        return 'Dollars: {}, Quarters: {} Dimes: {} Nickels: {} Pennies: {}'.format(self.dollars,self.quarters,self.dimes,self.nickels,self.pennies)

    #return total amount of $
    def amount(self):
        self.amount = (self.dollars * 1) + (self.quarters * .25) + (self.dimes * .10) + (self.nickels * .05) + (self.pennies * .01)
        return self.amount

    #add in the provided change
    def add_change(self, change):
        if change.dollars <= 1:
            self.dollars += change.dollars
        elif change.quarters <= .25:
            self.quarters += change.quarters
        elif change.dimes <= .10:
            self.dimes += change.dimes
        elif change.nickels <=.05:
            self.nickels += change.nickels
        elif change.pennies <= .01:
            self.pennies += change.pennies

    def remove(self, change):#needs an exceptions
        if self.dollars < change.dollars:
            raise Exception("Insufficient Dollars")
        elif self.quarters < change.quarters:
            raise Exception("Insufficient Quarters")
        elif self.dimes < change.dimes:
            raise Exception("Insufficient Dimes")
        elif self.nickels < change.nickels:
            raise Exception("Insufficient Nickels")
        elif self.pennies < change.pennies:
            raise Exception("Insufficient Pennies")

        self.dollars = self.dollars - change.dollars
        self.quarters = self.quarters - change.quarters
        self.dimes = self.dimes - change.dimes
        self.nickels = self.nickels - change.nickels
        self.pennies = self.pennies - change.pennies

    def remove_amount(self, amount):
        if amount.dollars >= 1:
            self.dollars -= amount.dollars
        elif amount.quarters >= .25:
            self.quarters = self.quarters - amount.quarters
        elif amount.dimes >= .10:
            self.dimes = self.dimes - amount.dimes
        elif amount.nickels >=.05:
            self.nickels = self.nickels - amount.nickels
        elif amount.pennies >= .01:
            self.pennies = self.pennies - amount.pennies

    #return change after paying 'paid_change' on 'amount_due'
    def payment_on(self, amount_due, paid_change):
        if amount_due > paid_change.amount():
            raise Exception("Insufficient Payment")

        self.add_change(paid_change)

        try:
            return self.remove_amount(paid_change.amount() - amount_due)
        except Exception as e:
            #self.remove_change(paid_change)
            raise e


#test code
register = Change(dollars=10, quarters=2, dimes=3, nickels=4, pennies=3)

due = 3.67
paid = Change(dollars=4)

# due = 3.66
# paid = Change(dollars=4)

# due = 3.24
# paid = Change(dollars=4)

# due = 3.67
# paid = Change(dollars=4, dimes=1, nickels=1, pennies=2)

try:
    print('Register:', register)
    print()
    print('Due:', due)
    print('Paid:', paid)
    print()

    back = register.payment_on(due, paid)

    print('Back:', back)
    print('Register:', register)

except Exception as e:
    print()
    print( 'Error:', str(e) )
    print('Register:', register)
# I am not sure why I keep getting a 'float' error message. It says the object is not callable, but I have no red lines and no exit code error...
