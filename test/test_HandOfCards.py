import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '..', 'src')))


import unittest
from HandOfCards import HandOfCards
from PlayingCard import PlayingCard

class TestHandOfCards(unittest.TestCase):
    def test_add_card(self):
        hand = HandOfCards()
        card = PlayingCard("H", 2)
        hand.add_card(card)
        self.assertIn(card, hand.cards)

    def test_remove_card(self):
        hand = HandOfCards()
        card = PlayingCard("D", 13)
        hand.add_card(card)
        hand.remove_card(card)
        self.assertNotIn(card, hand.cards)

    def test_hand_size(self):
        hand = HandOfCards()
        self.assertEqual(len(hand.cards), 0)
        hand.add_card(PlayingCard("C", 7))
        self.assertEqual(len(hand.cards), 1)
        
    

if __name__ == "__main__":
    unittest.main()
