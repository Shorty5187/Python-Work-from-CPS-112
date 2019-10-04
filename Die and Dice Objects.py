from random import randint

class Die:
    """Single Die"""

    def __init__(self):
        self.held = False
        self.roll()

    def roll(self):
        if not self.held:
            self.value = randint(1, 6)

    def __str__(self):
        if self.held:
            return "[{}]".format(self.value)
        else:
            return " {} ".format(self.value)

class Dice:
    """Collection of Die"""

    def __init__(self, how_many):
        self.dice = []
        for i in range(how_many):
            self.dice.append(Die())

    def __str__(self):
        tmp = ""
        for die in self.dice:
            tmp += str(die)
        return tmp

    def __roll__(self):
        for die in self.dice:#because you have it already defined above, you can just call itself from above
            die.roll()

    def sum(self):
        total = 0
        for die in self.dice:
            total += die.value
        return total

    def hold(self, hold_value, release_other=True):
        for die in self.dice:
            if die.value == hold_value:
                die.held = True
            elif release_other:
                die.held = False

    def count(self, count_value):
        """Method returns # of dice having specified value"""
        n = 0
        for die in self.dice:
            if die.value == count_value:
                n += 1
        return n

    def count_all(self):
        """return a cont of all values"""
        count = [0]
        for value in range(1, 6+1):
            count.append(self.count(value))
        return count

    def most(self):
        count = self.count_all()
        most_count = 0
        most_list = []

        for value in range(1, 6+1):
            if count[value] > most_count:
                most_count = count[value]
                most_list = [value]
            elif count[value] == most_count:
                most_list.append(value)

        return (most_count, most_list)

    def release_all(self):
        if d.held == True:
            d.held = False
        else:
            d.held = False
count = 0
#Test Dice Object
print("Testing Dice object")
for i in range(100000):
    d = Dice(5)
    for i in range (3):
        d.__roll__()
        most_often, most_list = d.most()
        #print(most_often)
        d.hold(most_list[0])
        if most_often == 5: #figures out if you have 5 of a kind#
            count = count + 1
        else:
            count = count
        print( '{}: {}: {}'.format(i, d, d.most()))
        print(count)

print('This number ', (count / 100000 * 100), '% is the probability of rolling a YAHTZEE per 100,000 rolls.')

#Print the Initial Values
#print(d)

#Test the Die Object
# print()
# print("Testing Die object")
# #Create Two Die Objects
# d1 = Die()
# d2 = Die()
#
# #Roll Each 10 times
# for i in range (0, 10+1):
#     d1.roll()
#     d2.roll()
#
#     print("{0}: {1} {2}".format(i, d1, d2))
#
#     #hold the first if it is a 6
#     if d1.value == 6:
#         d1.held = True
#     #Release the first if the second is a 1
#     if d2.value == 6:
#         d2.held = True
