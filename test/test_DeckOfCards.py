import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


import unittest
from DeckOfCards import DeckOfCards

class TestDeckOfCards(unittest.TestCase):
    def test_deck_size(self):
        deck = DeckOfCards()
        self.assertEqual(len(deck.cards), 52)  # Antar en standard 52-korts kortstokk

    def test_draw_card(self):
        deck = DeckOfCards()
        card = deck.draw_card()
        self.assertIsNotNone(card)
        self.assertEqual(len(deck.cards), 51)  # Ett kort trukket

    def test_shuffle(self):
        deck = DeckOfCards()
        before_shuffle = deck.cards[:]
        deck.shuffle()
        self.assertNotEqual(before_shuffle, deck.cards)  # Kortene skal stokkes

if __name__ == "__main__":
    unittest.main()
