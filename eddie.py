#rn i have little to no coding for the actual running of a game due to not being able to get the deal_to function to
#work under the cardstack() class

import random
class playingcard:

    ACE = 1
    JACK = 11
    KING = 13
    QUEEN = 12
    HEARTS = '\u2665'
    SPADES = '\u2666'
    CLUBS = '\u2663'
    DIAMONDS = '\u2660'
    SUITS = [HEARTS,DIAMONDS,CLUBS,SPADES]

    VALUE_NAMES = [None, 'A', '2', '3', '4', '5', '6', '7', '8', '9', 'x', 'J', 'Q', 'K']

    RED="red"
    BLACK="black"

    def __init__(self, value,suit,face_up=True):
        self.value = value
        self.suit=suit
        self.face_up=face_up

    def __str__(self):
        if self.face_up:
            return "[{}{}]".format(playingcard.VALUE_NAMES[self.value] ,self.suit)
        else:
            return "[--]"

    def color(self):
        if not self.face_up:
            return "-"
        if self.suit==playingcard.HEARTS or self.suit == playingcard.DIAMONDS:
            return playingcard.RED
        else:
            return playingcard.BLACK

    def is_royal(self):
        return self.value in [playingcard.JACK,playingcard.QUEEN, playingcard.KING]


class playingcardacehigh(playingcard):  #playing card ace high new class child of parent class playing card


    #new class overriding parent's points method
    @property
    def points(self):
        if self.value ==playingcard.ACE:
            return playingcard.KING + 1
        else:
            return self.value

    def flip(self):
        self.face_up=not self.face_up

    @classmethod
    def deck(cls):
        stack = cardstack()
        for suit in playingcard.SUITS:
            for value in range(playingcard.ACE, playingcard.KING+1):
                card = cls(value, suit)
                stack.add(card)

        stack.shuffle()
        return stack


class cardstack:

    def __init__(self):
        self.cards = []
    def add(self, card):
        self.cards.append(card)
    def __str__(self):
        tmp=""
        for card in self.cards:
            tmp += str(card)
        return tmp

    # def shuffle(self):
    #     # random.shuffle(self.cards)
    def shuffle(self):
        for i in range(len(self.cards) -1,0,- 1):
            pos = random.randrange(len(self.cards) - i)
            self.cards[pos], self.cards[-i - 1] = self.cards[-i - 1], self.cards[pos]

    @property
    def is_empty(self):
        return len(self.cards) == 0
    def deal_to(self,other):                             #this is the deal fucnction that i cant get to properly work
        for player in range(4):
        # deal cards here using deck.pop()               #You may also want to get rid of the property function unless it is essential. Try commenting it out for now.
            print(self.deck.pop(cardstack).num)          #Try something like the following and see where that gets you.   print(self.deck.pop(cardstack).num)

    def take(self,card):
        return self.cards.pop()

    @property
    def count(self):
        return len(self.cards)

    def transfer_all_to(self, other):
        while not self.is_empty:
            self.deal_to(other)

class blackjack:
    def __init__(self):
        self.playing = cardstack()

    def options(cardstack):
        print("(1=Hit)(2=Done)(3=Bust)")
        x=input("Hit?")
        if x == 1:
            deck.deal_to(player1.playing)
            deck.deal_to(player2.playing)
        elif x == 2:
            pass
        else:
            pass

deck = playingcardacehigh.deck()
player1=blackjack()
player2=blackjack()

hand1 = cardstack()
hand2 = cardstack()
print(hand1)
print(hand2)
while not deck.is_empty:
    deck.deal_to(hand1)
    # deck.deal_to(hand2)

print(hand1)
print(hand2)
