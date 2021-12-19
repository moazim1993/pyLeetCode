# import packages
import itertools
from itertools import permutations
import random


class DeckOfCards:
    def __init__(self):
        self.ranks =["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
        self.shapes = ["heart","dimond","Spade","cloves"]
        self.deck = self.generateDeck(self.ranks, self.shapes)
        

    def generateDeck(self, rank, shape):
        deck = []
        for r in rank:
            for s in shape:
                deck.append((r,s))
        return deck

    def deal(self, n):
        """
        given an int n, deal that many cards from the deck
        """
        hand = random.choices(self.deck, k=n)
        self.deck = [i for i in self.deck if i not in hand]
        return hand


myDeck = DeckOfCards()
#print(deck.generateDeck(["1","2","3","4"],["heart","dimond","Spade","cloves"]))
print(len(myDeck.deck))
print(myDeck.deal(5))
print(len(myDeck.deck))

"""
# initialize lists
list_1 = ["a", "b", "c","d"]
list_2 = [1,4,9]

# create empty list to store the
# combinations
unique_combinations = []

# Getting all permutations of list_1
# with length of list_2

# zip() is called to pair each permutation
# and shorter list element into combination
for comb in permut:
	zipped = zip(comb, list_2)
	unique_combinations.append(list(zipped))

# printing unique_combination list
print(unique_combinations)
"""