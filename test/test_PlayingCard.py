import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'src')))
from PlayingCard import *

class TestPlayingCard(unittest.TestCase):
    def test_create_card(self):
        card = PlayingCard("H", 1)
        self.assertEqual(card.suit, "H")
        self.assertEqual(card.face, 1)
        #self.assertEqual(card.rank, 1)

    def test_card_str(self):
        card = PlayingCard("S", 10)
        self.assertEqual(card.get_as_string(), "S10")
    

if __name__ == "__main__":
    unittest.main()
