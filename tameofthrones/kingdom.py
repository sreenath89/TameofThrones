from collections import Counter
from message import Message


class Kingdom:
    """
    Class containing basic attributes and methods
    of Kingdom class
    Attributes:
        name: name of the Kingdom
        king: name of the King
        allies: list of allies for the Kingdom
        emblem: unique emblem of the Kingdom
    """

    def __init__(self, name=None, king=None, emblem=None):
        self.name = name
        self.king = king
        self.allies = []
        self.emblem = emblem

    def validate_message(self, message_to_kingdom, sender):
        """
        Validate the message that has been received from another Kingdom
        Args
            message_to_kingdom:
            sender:
        Returns:
            Returns True if message has been validated successfully
        """
        message = Message(message_to_kingdom, sender, self.name)
        if message.decode_message(self.emblem):
            return True
        else:
            return False

    def add_allies(self, allie_name):
        """
        Add allies for current kingdom
        Args
            allie_name: name of ally kingdom
        Returns:
            Returns list of allies
        """
        return self.allies.append(allie_name)

    def get_allies(self):
        """
        Get the list of allies for current kingdom
        Args
            None
        Returns:
            Returns list of allies
        """
        return self.allies

    def remove_allies(self):
        pass

    def get_emblem_char_count(self):
        """
        Get the character wise count of emblem
        Args
            None
        Returns:
            Counter class containing key value pair showing
            each character and their count
        """
        return Counter(self.emblem)

    def __del__(self):
        '''
        Destructor
        '''
        pass
