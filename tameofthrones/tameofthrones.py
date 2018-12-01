import universe
import kingdom
from config import kingdom_dict, universe_name


def find_kingdom(king_name):
    for key, value in kingdom_dict.items():
        if value[0].lower() == king_name.lower():
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
        to_be_ruler = str(raw_input("\n Who wants to be the ruler of " +
                                    universe_name +
                                    " (Options are " + kings + "?\n"))
        print("Input Messages to kingdoms from " + to_be_ruler +
              "(Linux - Ctrl-D or Windows - Ctrl-Z to save it):\n")
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
                # emblem_char_count = kingdomObj.get_emblem_char_count()

                # send the message for validation
                if kingdomObj.validate_message(message, to_be_ruler):
                    allies.append(message_to_kingdom)

        # check if the ally count is atleast 3
        # if so, we set the new ruler for the universe
        if len(allies) >= 3:
            uniObj.ruler = to_be_ruler
            uniObj.allies = allies

        # display the information regarding the universe
        uniObj.get_info()


if __name__ == '__main__':
    main()
