class Change:

    def __init__(self, dollars=0, quarters=0, dimes=0, nickels=0, pennies=0):
        self.dollars = dollars
        self.quarters = quarters
        self.dimes = dimes
        self.nickels = nickels
        self.pennies = pennies

    def __str__(self):
        return "Dollars:{}; Quarters:{}; Dimes:{}; Nickels:{}; Pennies:{}".format(self.dollars,self.quarters,self.dimes,self.nickels,self.pennies)

    def amount(self):
        amount = self.dollars+self.quarters+self.dimes+self.nickels+self.pennies
        return amount

    def add_change(self, change):
        if change.dollars <= 1:
            change.dollars += self.dollars
        if change.quarters <= 1:
            change.quarters += self.quarters
        if change.dimes <= 1:
            change.dimes += self.dimes
        if change.nickels <= 1:
            change.nickels += self.nickels
        if change.pennies <=1:
            change.pennies += self.pennies

    def remove_change(self, change):
        if self.dollars < change.dollars:
            raise Exception ("Insufficient Dollars")
        if self.quarters < change.quarters:
            raise Exception ("Insufficient Quarters")
        if self.dimes < change.dimes:
            raise Exception ("Insufficient Dimes")
        if self.nickels < change.nickels:
            raise Exception ("Insufficient Nickels")
        if self.pennies < change.pennies:
            raise Exception ("Insufficient Pennies")

        self.dollars -= change.dollars
        self.quarters -= change.quarters
        self.dimes -= change.dimes
        self.nickels -= change.nickels
        self.pennies -= change.pennies

    def remove_amount(self, amount):



        pass

    def payment_on(self, amount_due, paid_change):
        if amount_due > paid_change.amount():
            raise Exception("Insufficient Payment")

        self.add_change(paid_change)

        try:
            return self.remove_amount(paid_change.amount()-amount_due)

        except Exception as e:
            self.remove_change(paid_change)
            raise e

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
