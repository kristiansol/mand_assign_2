import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '..', 'src')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from PlayingCard import *

class TestPlayingCard(unittest.TestCase):
    def test_create_card(self):
        card = PlayingCard("H", 1)
        self.assertEqual(card.suit, "H")
        self.assertEqual(card.face, 1)
      

    def test_card_str(self):
        card = PlayingCard("S", 10)
        self.assertEqual(card.get_as_string(), "S10")
    
    def test_hash(self):
        card = PlayingCard("D", 5)
        self.assertEqual(hash(card), hash(("D", 5)))
        
    def test__eq__(self):
        card1 = PlayingCard("H", 2)
        card2 = PlayingCard("H", 1)
        self.assertEqual(card1 == card2,False)  
        self.assertEqual((card1).__eq__(card2),False)   
        
    def test_get_suit_get_face(self):
        card = PlayingCard("H", 2)
        self.assertEqual(card.get_suit(), "H")
        self.assertEqual(card.get_face(), 2)
           
        
if __name__ == "__main__":
    unittest.main()
