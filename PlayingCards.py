import random

#dealer and player
Player_cards = []
Dealer_cards = []

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

    def __init__(self, value, suit, face_up = UP):
        self.value = value
        self.suit = suit.lower()
        self.face_up = face_up

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
    def full_deck(cls, face_up=True, shuffle=True):
        deck = CardStack()
        for suit in PlayingCard.SUITS:
            for value in range(PlayingCard.ACE, PlayingCard.KING+1):
                deck.add(cls(value, suit, face_up) )
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

class BlackJackCard(PlayingCard):
#creates a blackjack playing card
    @property
    def points(self):
        if self.value == PlayingCard.ACE:
            return 11
        elif self.value >= PlayingCard.JACK:
            return 10
        else:
            return self.value

class BlackJackStack(CardStack):
#takes the score of the cards in your hand
    def score(self):
        if self.cards >= 21:
            BlackJackCard.ACE = 1
            return self.cards + BlackJackCard.value
        else:
            return self.cards + BlackJackCard.value
            # loop through self.cards[] and total points
            # if > 21 and there are aces, make them worth 1 pt

class BlackJackGame:
    #where the game is actually played out

    def __init__(self, Deck, Dealer, Player):
        self.Deck = BlackJackCard.full_deck(face_up = False, shuffle = True)
        self.Dealer = BlackJackStack()
        self.Player = BlackJackStack()

        self.Deck.deal(other=self.Dealer, n_cards=2)
        self.Dealer.cards[0].flip()#flips one card over in the dealer's hand

        self.Deck.deal(other=self.Player, n_cards=2)
        self.Player.cards[0].flip()#flips both cards over in the player's hand
        self.Player.cards[1].flip()#flips both cards over in the player's hand

    def __str__(self):
        self.score = score
        return self.Player.score() + "/n" + self.Dealer.score()
        #returns the points of the player and the dealer on seperate lines

while Player_cards.self.score <= 21:
    print("Would you like to draw a card?")
    add_card = input("Type 'hit' to draw, type 'stay' to end.")
    print('')
    # if hit
    if add_card == "hit":
      Player_cards.append(BlackJackGame.self.Deck.deal(CardStack))
      score = Dealer_cards.hand()
      if Player_cards.self.score > 21:
        print("Player 1 Hand: " + Dealer_cards.hand())
        print("Player 1 Busted")
    elif Player_cards.self.score > Dealer_cards.self.score:
        print("Player 1 wins!")
    elif Player_cards.self.score < Dealer_cards.self.score:
        print("Dealer wins")
    elif sum(Dealer_cards) == 21:
        print("Dealer has 21 and wins!")
    elif sum(Dealer_cards) > 21:
        print("Dealer has busted!")

exit()

#Test code for work done in class and failed trials
#dealer = BlackJackCard.full_deck(face_up=True)
#hand = BlackJackStack()
#dealer.deal(hand, 2)
#print("Dealer hand".format(hand))

#player = PlayingCard.full_deck(face_up=True)
#hand = CardStack
#player.deal(hand, 2)
#print("Player hand".format(hand))

# dealer = PlayingCardACEHigh.full_deck(face_up=True)
# hand = CardStack()
# dealer.deal(hand, 2)
# print(hand)
# exit()

#deck = PlayingCard.full_deck()
# deck = PlayingCardACEHigh.full_deck(face_up=True)
#
# print(deck)
# print(deck.cards[0] )
# print(deck.cards[0].points)
#
# hand = CardStack()
# deck.deal(hand, 5)
# print(hand)
#
# exit()
#
# card1 = PlayingCardACEHigh(PlayingCard.ACE, PlayingCard.SPADES, face_up = PlayingCard.DOWN)
#
# card1.flip()
# card2 = PlayingCard(5, PlayingCard.DIAMONDS)
# card2.flip()

# print("Card:   ", card)
# print("Color:  ", card.color)
# print("Royal:  ", card.is_royal)
# print("Points: ", card.points)
# print()

# hand = CardStack()

# hand.add(card1, CardStack.LEFT)
# hand.add(card2, 0)
#
# for value in range(PlayingCard.ACE, PlayingCard.KING+1):
#     hand.add(PlayingCard(value, PlayingCard.DIAMONDS))
#
# print("Hand:    ", hand) #prints given hand of cards
# print("# Cards:", len(hand) )
#
# for i in range(5):
#     card = hand.pick()#dictates where you take the card from
#     print(card)
# print(hand)
