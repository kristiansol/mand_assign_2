import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '..', 'src')))
from PlayingCard import PlayingCard

class TestPlayingCard(unittest.TestCase):
    def test_create_card(self):
        card = PlayingCard("Hearts", "Ace")
        self.assertEqual(card.suit, "Hearts")
        self.assertEqual(card.rank, "Ace")

    def test_card_str(self):
        card = PlayingCard("Spades", "10")
        self.assertEqual(str(card), "10 of Spades")

if __name__ == "__main__":
    unittest.main()
