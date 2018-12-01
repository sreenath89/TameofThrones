import universe
import kingdom
from config import kingdom_dict, universe_name


def find_kingdom(king_name):
    """
    Function to fetch the name of Kingdom based on the King
    Args:
        king_name: name of the king
    Return:
        (str) kname: name of the kingdom, if king is
                     present in the dictionary, else
                     return None
    """

    # loop through eachitem in the kingdom dictionary
    for key, value in kingdom_dict.items():
        # compare the name of king
        if value[0].lower() == king_name.lower():
            # fetch the kingdom name
            kname = key
            break
        else:
            kname = None
    return kname


def main():
    '''
    '''
    # universe_name = 'Southeros'
    uniObj = universe.Universe(universe_name, kingdom_dict)
    universe_ruler, king_list = uniObj.get_info()
    kings = ', '.join(king_list)

    # Enter only if there isn't any ruler for the Universe
    if not universe_ruler:
        to_be_ruler = ''

        # ensure that only valid king names are entered
        while to_be_ruler not in king_list:
            to_be_ruler = str(raw_input("\nWho wants to "
                                        "be the ruler of "
                                        + universe_name +
                                        " (Options are "
                                        + kings + "?\n"))
            to_be_ruler = to_be_ruler.title()
        print("\nInput Messages to kingdoms from "
              + to_be_ruler +
              "(One line for each unique message | "
              "Ex- <Kingdom Name>, <Message> | "
              "Enter - to move to next line, "
              "Linux - Ctrl-D or Windows - Ctrl-Z "
              "to stop inout save it):\n")
        allies = []
        messages = []

        '''
        Since we don't know the exact number of inputs
        that will be given by the user. By default
        '''
        while True:
            try:
                line = str(raw_input())
            except EOFError:
                break
            messages.append(line)

        '''
        loop through each message and find the kingdom name
        and message to kingdom
        '''
        for message in messages:
            try:
                message_to_kingdom = message.split(',')[0].lower().strip()
                message = message.split(",")[1].lower().strip()
            except IndexError:
                message_to_kingdom = ''
                message = ''

            # validate the Kindom name present in the user input
            if message_to_kingdom in kingdom_dict.keys() and \
                    message_to_kingdom != find_kingdom(
                    to_be_ruler):
                kingdomObj = kingdom.Kingdom(
                        message_to_kingdom,
                        kingdom_dict.get(
                            message_to_kingdom
                        )[0],
                        kingdom_dict.get(
                            message_to_kingdom
                        )[1])

                # send the message for validation
                if kingdomObj.validate_message(message, to_be_ruler):
                    allies.append(message_to_kingdom.title())

        # ensure that one kingdom has only one entry
        # even if multiple messages have been sent
        unique_allies = set(allies)

        # check if the ally count is atleast 3
        # if so, we set the new ruler for the universe
        if len(unique_allies) >= 3:
            uniObj.ruler = to_be_ruler

            # convert set to list and pass it
            uniObj.allies = list(unique_allies)

        # display the information regarding the universe
        uniObj.get_info()


if __name__ == '__main__':
    main()
