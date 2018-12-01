from kingdom import Kingdom


class Universe:
    """
    Class containing basic attributes and methods
    of Universe class
    Attributes:
        name: name of the Universe
        ruler: name of the current Universe Ruler
    """
    def __init__(self, name=None, kingdom_dict={}, ruler=None, allies=None):
        self.name = name
        self.ruler = ruler

        # need to check if this needed?
        self.allies = allies
        self.kingdoms = []
        self.king_list = []
        self.kingdom_list = []
        self.kingdom_dict = kingdom_dict

        for k, v in self.kingdom_dict.items():
            kingdom = Kingdom(k, v[0], v[1])
            self.king_list.append(v[0])
            self.kingdom_list.append(k)
            self.kingdoms.append(kingdom)

    def get_info(self):
        """
        Function to dispaly the basic info regarding the Universe
        Args
            None
        Returns:
            Return the ruler name and list of Kings
        """
        print("\nWho is the ruler of " + self.name + "?")
        print(str(self.get_ruler()))
        if self.get_ruler():
            print("\nAllies of " + self.ruler + "?")
        else:
            print("\nAllies of Ruler?")
        print(str(self.get_allies()))
        return self.get_ruler(), self.king_list

    def get_kingdoms(self):
        """
        Function to get the kingdoms present in Universe
        Args
            None
        Returns:
            Returns a list of Kingdom objects
        """
        if self.kingdoms:
            return self.kingdoms
        else:
            return None

    def get_ruler(self):
        """
        Function to fetch the name of the current ruler of Universe
        Args
            None
        Returns:
            (str) Name of the ruler
        """
        return self.ruler

    def get_allies(self):
        """
        Function to get the allies for the current ruler
        Args:
            None
        Returns:
            Returns a string of allies if any ally
            is present else return None
        """
        # check if any allies are present
        if self.allies:
            # convert list of allies to a string
            return ", ".join(self.allies)
        else:
            return None

    def get_kings(self):
        """
        Function to get a string of all Kings present
        in the Universe
        Args
            None
        Returns:
            Return a string of King names if any
            King is present else return None
        """
        if self.king_list:
            # convert list of Kings to a string
            return ', '.join(self.king_list)
        else:
            return None

    def __del__(self):
        '''
        Destructor
        '''
        pass
