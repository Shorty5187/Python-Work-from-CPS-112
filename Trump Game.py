import random
class PlayingCard:

    ACE = 1
    JACK = 11
    QUEEN = 12
    KING = 13

    VALUE_NAMES = [None, 'A', '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K']

    HEARTS = '\u2665'
    DIAMONDS = '\u2666'
    CLUBS = '\u2663'
    SPADES = '\u2660'

    SUITS =(HEARTS, DIAMONDS, CLUBS, SPADES)

    RED = 0
    BLACK = 1

    UP = True
    DOWN = False

    def __init__(self, value, suit, face_up = UP, game=None):
        self.value = value
        self.suit = suit.lower()
        self.face_up = face_up
        self.game = game

    def __str__(self):
        if not self.face_up:
            return '[--]'
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
        # if self.face_up == True:
        #     self.face_up = False
        # else:
        #     self.face_up = True
        self.face_up = not self.face_up

    @classmethod
    def full_deck(cls, face_up=True, shuffle=True, game=None):
        deck = CardStack()
        for suit in PlayingCard.SUITS:
            for value in range(PlayingCard.ACE, PlayingCard.KING+1):
                deck.add(cls(value, suit, face_up, game = game) )
        if shuffle:
            deck.shuffle()

        return deck

class PlayingCardACEHigh(PlayingCard): #child of playing card

    @property
    def points(self):
        if self.value == PlayingCard.ACE:
            return PlayingCard.KING + 1
        else:
            return self.value


class TrumpPlalyingCard(PlayingCardACEHigh):
    @property
    def is_trump(self):
        return self.suit == self.game.trump

    @property
    def points(self):
        if self.is_trump:
            multiplier = 10
        else:
            multiplier = 1
        return super(TrumpPlalyingCard, self).points * multiplier

class EuchrePlayingCard(PlayingCardACEHigh):
    pass

class CardStack:

    TOP = -1
    BOTTOM = 0

    LEFT = 0
    RIGHT = -1

    def __init__(self, force_up_down=None):
        self.cards = []
        self.force_up_down = force_up_down


    def __str__(self):
        return "-".join(str(card) for card in self.cards)

    def add(self, card, pos=TOP):
        if pos == CardStack.TOP:
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
            other.add(self.take() )
