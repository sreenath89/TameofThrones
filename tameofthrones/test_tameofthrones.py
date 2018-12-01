import unittest
from message import Message
from universe import Universe
from kingdom import Kingdom
from config import kingdom_dict
from collections import Counter


class TestUniverse(unittest.TestCase):
    def setUp(self):
        self.message = "Ice, Ahoy! Fight for me with men & money"
        self.emblem = 'mammoth'
        self.king_name = 'King Shan'
        self.receiver = 'fire'
        self.sender = 'space'
        self.msgObj = Message(self.message, self.sender, self.receiver)
        self.kingObj = Kingdom('space', 'King Shan', 'gorilla')
        self.kingObj1 = Kingdom('fire', 'Dragon King', 'dragon')
        self.allies = ['fire', 'water', 'ice']
        self.kingObj.allies = self.allies
        self.universe_name = 'Southeros'
        self.uniObj = Universe(self.universe_name, kingdom_dict)
        self.uniObj.ruler = 'King Shan'
        self.uniObj.allies = self.allies

    def test_message_get_char_count(self):
        message_get_char_count = self.msgObj.get_char_count(self.message)
        expected_output = Counter(self.message)
        self.assertEqual(message_get_char_count, expected_output)

    def test_get_emblem_char_count(self):
        space_emblem = 'gorilla'
        expected_output = Counter(space_emblem)
        orig_output = self.kingObj.get_emblem_char_count()
        self.assertEqual(orig_output, expected_output)

    def test_get_emblem_char_count_failure(self):
        expected_output = Counter(self.emblem)
        orig_output = self.kingObj.get_emblem_char_count()
        self.assertNotEqual(orig_output, expected_output)

    def test_get_kingdom_allies(self):
        expected_output = ['fire', 'water', 'ice']
        orig_outut = self.kingObj.get_allies()
        self.assertEqual(expected_output, orig_outut)

    def test_get_allies_list_type(self):
        orig_outut = self.kingObj.get_allies()
        self.assertIsInstance(orig_outut, list)

    def test_get_universe_ruler(self):
        expected_output = 'King Shan'
        orig_output = self.uniObj.get_ruler()
        self.assertEqual(orig_output, expected_output)

    def test_get_universe_king_allies(self):
        expected_output = ', '.join(self.allies)
        orig_output = self.uniObj.get_allies()
        self.assertEqual(orig_output, expected_output)

    def test_get_allies_type(self):
        # expected_output = ', '.join(self.allies)
        orig_output = self.uniObj.get_allies()
        self.assertIsInstance(orig_output, str)

    def test_get_universe_kings(self):
        expected_output = 'Land King, King Shan,'\
                          'Dragon King, Ice King,'\
                          'Air King, Water King'
        orig_output = self.uniObj.get_kings()
        self.assertEqual(orig_output, expected_output)

    def test_verify_king_in_universe_kings(self):
        orig_output = self.uniObj.get_kings()
        self.assertIn(self.king_name, orig_output)

    def test_no_king_in_universe(self):
        self.uniObj.king_list = []
        orig_output = self.uniObj.get_kings()
        self.assertIsNone(orig_output)

    def test_get_universe_kingdoms_type(self):
        orig_output = self.uniObj.get_kingdoms()
        self.assertIsInstance(orig_output, list)

    def test_no_kingdoms_in_universe(self):
        self.uniObj.kingdoms = []
        self.assertIsNone(self.uniObj.get_kingdoms())

    def test_validate_message(self):
        message_to_fire = 'Fire, "Drag on Martin!"'
        orig_output = self.kingObj1.validate_message(
                      message_to_fire, self.sender)
        self.assertTrue(orig_output)

    def test_validate_message_failure(self):
        message_to_fire = 'Fire, "Drag on Martin!"'
        orig_output = self.kingObj.validate_message(
                      message_to_fire, self.sender)
        self.assertFalse(orig_output)

    def test_debug_incorrect_message(self):
        orig_output = self.msgObj.decode_message('dragon')
        self.assertFalse(orig_output)

    def test_debug_correct_message(self):
        self.msgObj.message = 'Fire, "Drag on Martin!"'
        orig_output = self.msgObj.decode_message('dragon')
        self.assertTrue(orig_output)

    def tearDown(self):
        del self.msgObj
        del self.kingObj
        del self.kingObj1
        del self.uniObj


if __name__ == '__main__':
    unittest.main()
