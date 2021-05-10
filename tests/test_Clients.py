import unittest
from Client.utils.fonctions import countCards

class ClientTest(unittest.TestCase):
    def test_CountCards(self):
        cards1 = [{'code': '7S', 'image': 'https://deckofcardsapi.com/static/img/7S.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/7S.svg', 'png': 'https://deckofcardsapi.com/static/img/7S.png'}, 'value': '7', 'suit': 'SPADES'}, 
        {'code': 'KC', 'image': 'https://deckofcardsapi.com/static/img/KC.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/KC.svg', 'png': 'https://deckofcardsapi.com/static/img/KC.png'}, 'value': 'KING', 'suit': 'CLUBS'}, 
        {'code': '0D', 'image': 'https://deckofcardsapi.com/static/img/0D.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/0D.svg', 'png': 'https://deckofcardsapi.com/static/img/0D.png'}, 'value': '10', 'suit': 'DIAMONDS'}, 
        {'code': '3C', 'image': 'https://deckofcardsapi.com/static/img/3C.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/3C.svg', 'png': 'https://deckofcardsapi.com/static/img/3C.png'}, 'value': '3', 'suit': 'CLUBS'}, 
        {'code': '9H', 'image': 'https://deckofcardsapi.com/static/img/9H.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/9H.svg', 'png': 'https://deckofcardsapi.com/static/img/9H.png'}, 'value': '9', 'suit': 'HEARTS'}]

        card2 = [{'code': 'QC', 'image': 'https://deckofcardsapi.com/static/img/QC.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/QC.svg', 'png': 'https://deckofcardsapi.com/static/img/QC.png'}, 'value': 'QUEEN', 'suit': 'CLUBS'}, 
        {'code': '3D', 'image': 'https://deckofcardsapi.com/static/img/3D.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/3D.svg', 'png': 'https://deckofcardsapi.com/static/img/3D.png'}, 'value': '3', 'suit': 'DIAMONDS'}, 
        {'code': '7C', 'image': 'https://deckofcardsapi.com/static/img/7C.png', 'images': {'svg': 'https://deckofcardsapi.com/static/img/7C.svg', 'png': 'https://deckofcardsapi.com/static/img/7C.png'}, 'value': '7', 'suit': 'CLUBS'}]

        self.assertEqual({'SPADES': 1, 'DIAMONDS': 1, 'CLUBS': 2, 'HEARTS': 1}, countCards(cards1))
        self.assertEqual({'SPADES': 0, 'DIAMONDS': 1, 'CLUBS': 2, 'HEARTS': 0}, countCards(card2))