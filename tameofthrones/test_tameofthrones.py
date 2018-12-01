import unittest
from message import Message
from universe import Universe
from kingdom import Kingdom
from config import kingdom_dict
from collections import Counter


class TestUniverse(unittest.TestCase):
    """
    Class containing methods for unit testing
    """
    def setUp(self):
        """
        Function to set the required values for testing
        Args

        Returns:
            Initialize a set of variables and objects for testing
        """
        self.message = "Ice, Ahoy! Fight for me with men & money"
        self.emblem = 'mammoth'
        self.king_name = 'King Shan'
        self.receiver = 'fire'
        self.sender = 'space'
        self.msgObj = Message(self.message, self.sender, self.receiver)
        self.kingObj = Kingdom('space', 'King Shan', 'gorilla')
        self.fireObj1 = Kingdom('fire', 'Dragon King', 'dragon')
        self.allies = ['fire', 'water', 'ice']
        self.kingObj.allies = self.allies
        self.universe_name = 'Southeros'
        self.uniObj = Universe(self.universe_name, kingdom_dict)
        self.uniObj.ruler = 'King Shan'
        self.uniObj.allies = self.allies

    def test_message_get_char_count(self):
        """
        Function to test the get_char_count method
        Args
            None
        Returns:
            Success, if character counts are correct
        """
        message_get_char_count = self.msgObj.get_char_count(self.message)
        expected_output = Counter(self.message)
        self.assertEqual(message_get_char_count, expected_output)

    def test_get_emblem_char_count(self):
        """
        Function to test the get_emblem_char_count method
        Args
            None
        Returns:
            Success, if character counts are correct
        """
        space_emblem = 'gorilla'
        expected_output = Counter(space_emblem)
        orig_output = self.kingObj.get_emblem_char_count()
        self.assertEqual(orig_output, expected_output)

    def test_get_emblem_char_count_failure(self):
        """
        Function to test the failure condition of
        get_emblem_char_count method
        Args
            None
        Returns:
            Success, if character counts are in-correct
        """
        expected_output = Counter(self.emblem)
        orig_output = self.kingObj.get_emblem_char_count()
        self.assertNotEqual(orig_output, expected_output)

    def test_get_kingdom_allies(self):
        """
        Function to test the get_kingdom_allies method
        Args
            None
        Returns:
            Success, if kingdom allies are correctly displayed
        """
        expected_output = ['fire', 'water', 'ice']
        orig_outut = self.kingObj.get_allies()
        self.assertEqual(expected_output, orig_outut)

    def test_get_allies_list_type(self):
        """
        Function to test the output type from the
        get_kingdom allies method
        Args
            None
        Returns:
            Success, if character counts are in-correct
        """
        orig_outut = self.kingObj.get_allies()
        self.assertIsInstance(orig_outut, list)

    def test_get_universe_ruler(self):
        """
        Function to test the get_universe_ruler method
        Args
            None
        Returns:
            Success, if ruler name is correct
        """
        expected_output = 'King Shan'
        orig_output = self.uniObj.get_ruler()
        self.assertEqual(orig_output, expected_output)

    def test_get_universe_king_allies(self):
        """
        Function to test the get_allies method to
        fetch the allies of King in Universe
        Args
            None
        Returns:
            Success, if allies are displayed correctly
        """
        expected_output = ', '.join(self.allies)
        orig_output = self.uniObj.get_allies()
        self.assertEqual(orig_output, expected_output)

    def test_get_allies_type(self):
        """
        Function to test the get_allies_type method
        Args
            None
        Returns:
            Success, if the allies type is correct
        """
        # expected_output = ', '.join(self.allies)
        orig_output = self.uniObj.get_allies()
        self.assertIsInstance(orig_output, str)

    def test_get_universe_kings(self):
        """
        Function to test the get_kings method
        Args
            None
        Returns:
            Success, if Kings are displayed correctly
        """
        expected_output = 'Land King, King Shan,'\
                          ' Dragon King, Ice King,'\
                          ' Air King, Water King'
        orig_output = self.uniObj.get_kings()
        self.assertEqual(orig_output, expected_output)

    def test_verify_king_in_universe_kings(self):
        """
        Function to test the get_kings method's
        output for the presence of a king
        Args
            None
        Returns:
            Success, if King is present
        """
        orig_output = self.uniObj.get_kings()
        self.assertIn(self.king_name, orig_output)

    def test_no_king_in_universe(self):
        """
        Function to test the get_kings method
        when no kings are present in universe
        Args
            None
        Returns:
            Success, if output is None
        """
        self.uniObj.king_list = []
        orig_output = self.uniObj.get_kings()
        self.assertIsNone(orig_output)

    def test_get_universe_kingdoms_type(self):
        """
        Function to test the get_kingdoms method
        to check the output type
        Args
            None
        Returns:
            Success, if output is of type 'list'
        """
        orig_output = self.uniObj.get_kingdoms()
        self.assertIsInstance(orig_output, list)

    def test_no_kingdoms_in_universe(self):
        """
        Function to test the get_kingdoms method
        when no kings are present
        Args
            None
        Returns:
            Success, if output is None
        """
        self.uniObj.kingdoms = []
        self.assertIsNone(self.uniObj.get_kingdoms())

    def test_validate_message(self):
        """
        Function to test the validate_message method
        Args
            None
        Returns:
            Success, if validation passes
        """
        message_to_fire = 'Fire, "Drag on Martin!"'
        orig_output = self.fireObj1.validate_message(
                      message_to_fire, self.sender)
        self.assertTrue(orig_output)

    def test_validate_message_failure(self):
        """
        Function to test the validate_message method
        for failure
        Args
            None
        Returns:
            Success, if message validation fails
        """
        message_to_fire = 'Fire, "Drag on Martin!"'
        orig_output = self.kingObj.validate_message(
                      message_to_fire, self.sender)
        self.assertFalse(orig_output)

    def test_debug_incorrect_message(self):
        """
        Function to test the decode_message method
        for incorrect message
        Args
            None
        Returns:
            Success, if message decoding fails
        """
        orig_output = self.msgObj.decode_message('dragon')
        self.assertFalse(orig_output)

    def test_debug_correct_message(self):
        """
        Function to test the decode_message method
        Args
            None
        Returns:
            Success, if message decoding works
        """
        self.msgObj.message = 'Fire, "Drag on Martin!"'
        orig_output = self.msgObj.decode_message('dragon')
        self.assertTrue(orig_output)

    def tearDown(self):
        """
        Function to specify the cleanup steps afte test execution
        """
        del self.msgObj
        del self.kingObj
        del self.fireObj1
        del self.uniObj


if __name__ == '__main__':
    unittest.main()
