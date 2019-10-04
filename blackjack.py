import random

class PlayingCard:

    ACE = 1
    JACK = 11
    QUEEN = 12
    KING = 13

    VALUE_NAMES = [None, 'A','2','3','4','5','6','7','8','9','X','J','Q','K']

    HEARTS = '\u2665'
    DIAMONDS = '\u2666'
    CLUBS = '\u2663'
    SPADES = '\u2660'

    SUITS = (HEARTS, DIAMONDS, CLUBS, SPADES)

    RED = "RED"
    BLACK = "BLACK"

    UP = True
    DOWN = False

    def __init__(self, value, suit, face_up=UP):
        self.value = value
        self.suit = suit.lower()
        self.face_up = face_up

    def __str__(self):
        if not self.face_up:
            return "[--]"
        else:
            return "[{}{}]".format(PlayingCard.VALUE_NAMES[self.value], self.suit)

    @property
    def is_royal(self):
        return self.value >= PlayingCard.JACK

    @property
    def color(self):
        return PlayingCard.RED if self.suit == PlayingCard.HEARTS or self.suit == PlayingCard.DIAMONDS else PlayingCard.BLACK

    @property
    def points(self):
        return self.value

    def flip(self):
        # if self.face_up == PlayingCard.UP:
        #     self.face_up = PlayingCard.DOWN
        # else:
        #     self.face_up = PlayingCard.UP

        self.face_up = not self.face_up

    @classmethod
    def full_deck(cls, face_up=True, shuffle=True):
        deck = CardStack()
        for suit in PlayingCard.SUITS:
            for value in range(PlayingCard.ACE,PlayingCard.KING+1):
                deck.add(cls(value,suit,face_up))

        if shuffle:
            deck.shuffle()

        return deck



class AceHighPlayingCard(PlayingCard):

    @property
    def points(self):
        if self.value == PlayingCard.ACE:
            return PlayingCard.KING+1
        else:
            return self.value



class CardStack:

    TOP = -1
    BOTTOM = 0

    LEFT = 0
    RIGHT = -1

    def __init__(self, force_up_down=None):
        self.cards = []
        self.force_up_down = force_up_down

    def __str__(self):
#        return "".join(str(card) for card in self.cards)
        tmp = ""
        for card in self.cards:
            # tmp = tmp + str(card)
            tmp += str(card)

        return tmp

    def add(self, card, pos=TOP):
        if pos== CardStack.TOP:
            self.cards.append(card)
        else:
            self.cards.insert(pos, card)

        if not self.force_up_down is None:
            card.face_up = self.force_up_down

    def take(self, pos=TOP):
        return self.cards.pop(pos)

    def pick(self):
        pos = random.randrange(len(self))
        return self.take(pos)

    @property
    def count(self):
        return len(self.cards)

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

        # for n in range(len(self.cards)*10):
        #     i = random.randrange(len(self.cards))
        #     j = random.randrange(len(self.cards))
        #
        #     self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def deal(self, other, n_cards=1):
        for i in range(n_cards):
            other.add(self.take())

#deck = PlayingCard.full_deck()
deck = AceHighPlayingCard.full_deck(face_up=True)

print(deck)
print( deck.cards[0] )
print( deck.cards[0].points )

hand = CardStack()

deck.deal(hand,5)
print( hand )

exit()

card1 = PlayingCard(PlayingCard.ACE, PlayingCard.SPADES, face_up=PlayingCard.DOWN)
card1.flip()

#card = AceHighPlayingCard(PlayingCard.ACE, PlayingCard.DIAMONDS, face_up=PlayingCard.UP)
card2 = PlayingCard(5, PlayingCard.DIAMONDS)
card2.flip()

# print( "card:  ", card )
# print( "color: ", card.color )
# print( "royal: ", card.is_royal )
# print( "points:", card.points )

hand = CardStack()

#hand.add(card1)
#hand.add(card2)

for value in range(PlayingCard.ACE, PlayingCard.KING+1):
    hand.add( PlayingCard(value, PlayingCard.DIAMONDS))

print( "Hand:", hand )
print( "# Cards:", len(hand) )

for i in range(5):
    card = hand.pick()
    print( card )

print( "Hand:", hand )
print( "# Cards:", len(hand) )
