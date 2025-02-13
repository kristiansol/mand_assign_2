import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '..', 'src')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from HandOfCards import *
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
        
    def test_is_flush(self):
        hand = HandOfCards()
        hand.add_card(PlayingCard("H",1))
        hand.add_card(PlayingCard("H", 2))
        hand.add_card(PlayingCard("H",3))
        hand.add_card(PlayingCard("H",4))
        hand.add_card(PlayingCard("H",5))
        self.assertEqual(hand.is_flush(), True)
        
    
        
        
        
        
        
    

if __name__ == "__main__":
    unittest.main()
