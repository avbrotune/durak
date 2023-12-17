from random import shuffle, randint

RANDOM_NAMES = ['Loren H. Warden', 'Khadijah Lynch', 'Chase Davenport', 'Joel K. Laney',
    'Jorden L. Linton', 'Quinlan Feldman', 'Emiliano Moe', 'Johnny J. Alley',
    'Josephine Vinson', 'Gabriel Corona', 'Ramon Cooney', 'Edna K. Benavides',
    'Kaya S. Workman', 'Travion E. Blount', 'Melany L. Connell', 'Kalli Dubose',
    'Alia A. Weiner', 'Victor Q. Perea', 'Tyrone J. Conway', 'Rashawn Menendez',
    'Alvaro Hathaway', 'Valentin T. Otto', 'Jarett K. Young', 'Angel B. Hinson',
    'Omari Z. Cable', 'Dana Herron', 'Jalynn M. Cyr', 'Sebastian S. Wheeler',
    'Lyric Maki', 'Jayna Bull', 'Hector K. Templeton', 'Alora Tom',
    'Zariah A. Sheets', 'Hayley McLain', 'Devon D. McMullen',
    'Alayna M. Rosenberg', 'Yosef Wylie', 'Kaia Mast', 'Ignacio Hinton',
    'Alysha Mcneely', 'Ammon Polk', 'Kirsten Garrison', 'Crystal Witherspoon',
    'Tyrell E. Fuentes', 'Emmanuel Keating', 'Riley E. Robins',
    'Susannah White', 'Loren M. Steen', 'Milton J. Mcvey', 'Baby B. Wright']

CARD_VALUES = {
    '6': 1,
    '7': 2,
    '8': 3,
    '9': 4,
    '10': 5,
    'J': 6,
    'Q': 7,
    'K': 8,
    'A': 9
}
CARD_RANKS = {
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
    '10': 'Ten',
    'J': 'Jack',
    'Q': 'Queen',
    'K': 'King',
    'A': 'Ace'
}
SUITS = ('Diamonds', 'Hearts', 'Spades', 'Clubs')

class Card():
    def __init__(self, suit, rank):
        self.rank = rank
        self.is_trump = False
        self.suit = suit

    def __repr__(self):
        return f'{CARD_RANKS[self.rank]} of {self.suit}'

class Player():
    def __init__(self, name):
        self.hand = []
        self.name = name

    def add_card(self, card):
        self.hand.append(card)

    def play_card(self, index):
        self.hand.pop(index-1)

    def __repr__(self):
        return self.name

class Game():
    def __init__(self):
        self.players = []
        self.turn = None
        self.deck = []
        self.trump_suit = None

    def set_players(self):
        while True:
            try:
                players_number = int(input('Enter number of players from 2 to 6: '))
                if players_number not in range(2, 7):
                    print('Game only allows from 2 to 6 players')
                    pass
            except ValueError:
                print('You should write a whole number')
            else:
                for _ in range(players_number):
                    self.players.append(Player(name=RANDOM_NAMES[randint(0,50)]))
                break

    def create_deck(self):
        for suit in SUITS:
            for rank in CARD_VALUES.keys():
                self.deck.append(Card(suit, rank))
                shuffle(self.deck)

    def deal_cards(self, players, first=False, cards_needed=6):
        if first:
            self.trump_suit = self.deck[0].suit
            for _ in range(cards_needed):
                for player in players:
                    player.add_card(self.deck.pop())
        else:
            for player in players:
                for _ in range(cards_needed):
                    try:
                        player.add_card(self.deck.pop())
                    except IndexError:
                        return

    def define_first_turn(self):
        """Defines who's first turn"""
        compare = []
        for player in self.players:
            player_trump_cards = [CARD_VALUES[card.rank] for card in player.hand if card.suit == self.trump_suit]
            compare.append(min(player_trump_cards)) if player_trump_cards else compare.append(100000)
        self.turn = compare.index(min(compare))




game = Game()
game.set_players()
print(game.players)
game.create_deck()
print(game.deck)
game.deal_cards(game.players, first=True)
for player in game.players:
    print(player.hand)
print(game.trump_suit)
game.define_first_turn()
print(game.players[game.turn])
