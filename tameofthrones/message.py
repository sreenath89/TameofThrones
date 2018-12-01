from collections import Counter
import re


class Message:
    """
    Class containing basic attributes and methods
    of Message class
    Attributes:
        message: message which is to be decoded
        sender: Kingdom who sends the message
        receiver: Kingdom for whom the message is sent
    """
    def __init__(self, message, sender, receiver):
        self.message = message
        self.sender = sender
        self.receiver = receiver

    def cleanup_message(self):
        '''
        Fetch only alphabets
        '''
        return ''.join(re.findall("[a-zA-Z]+", self.message.lower()))

    def get_char_count(self, message_to_check):
        """
        Function to get the character wise count of a string
        Args
            message_to_check: string whose character wise count is
            to be obtained
        Returns:
            Returns a Counter class containing dict with
            charcters as key and their count as value
        """
        return Counter(message_to_check)

    def decode_message(self, secret_key):
        """
        Function to decode the message send by one kingdom
        to another kingdom
        Args
            secret_key: corresponds to the emblem of
                        kingdom that receives the message
        Returns:
            Returns True, if decoding was successful
        """
        cleaned_up_message = self.cleanup_message()
        message_count = self.get_char_count(cleaned_up_message)
        secret_key_char_count = self.get_char_count(secret_key)
        for char in secret_key:
            if char not in message_count.keys():
                return False
            else:
                secret_char_value = secret_key_char_count.get(char, 0)
                message_char_value = message_count.get(char, 0)
                if message_char_value < secret_char_value:
                    return False
        return True

    def __del__(self):
        pass
