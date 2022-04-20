def introduction():
    print('Welcome to Wizard Knights! You are Sir Steven Brule, knight of S’wallow Valley. \n'
          'You must travel to 6 exotic locations to gather items needed to save Princess Jan \n'
          'from the evil wizard, and her ex-husband, Wayne Skylar!!\n')
    print('Move Commands: North, north, South, south, East, east, West, west, Exit, exit\n')
    print('To collect an item, use the command \'get item\'\n')
    print('You awaken in S\'wallow Valley Town Square, your ears ringing from the battle \n'
          'you\'ve just been through. Princess Jan is nowhere to be seen, and you can hear \n'
          'the evil Wizard, and Jan\'s ex-husband, Wayne Skylar cackling in the distance.\n'
          '\"She\'s mine forever Steven! You\'ll never save her!\"\n'
          'You stand up, preparing for the journey before you. Save Princess Jan!')


rooms = {
    'S\'wallow Valley Town Square': {
        'South': 'Channel 5 News Station',
        'West': 'Steve Mahanahan\'s Child Clown Outlet',
        'North': 'Jan\'s Castle',
        'East': 'Wayne\'s Castle'},
    'Channel 5 News Station': {'North': 'S\'wallow Valley Town Square',
                               'item': 'Glasses of the Learned Doctor'},
    'Steve Mahanahan\'s Child Clown Outlet': {"South": "S\'wallow Valley Mall",
                                              'East': 'S\'wallow Valley Town Square',
                                              'item': 'Child Clown Bard'},
    'S\'wallow Valley Mall': {'North': 'Steve Mahanahan\'s Child Clown Outlet',
                              'item': 'The Great Sword of Alan Bishopman'},
    'Jan\'s Castle': {'South': 'S\'wallow Valley Town Square',
                      'East': 'House of Doris Pringle Brule',
                      'item': 'Jan\'s Vest of Protection'},
    'House of Doris Pringle Brule': {'West': 'Jan\'s Castle',
                                     'North': 'S\'wallow Valley Lake',
                                     'item': 'Pant Suit of Might'},
    'S\'wallow Valley Lake': {'South': 'House of Doris Pringle Brule',
                              'item': 'Hunk Shield'},
    'Wayne\'s Castle': {'West': 'S\'wallow Valley Town Square', 'item': 'Wayne Skylar'}
}

inventory = []

introduction()
def player_status():  # sets up info returned to give player context about location
    print('-------------------')
    print('You are in the {}'.format(current_room))
    print('Items {}'.format(inventory))
    print('What would you like to do?')
    print('-------------------')


current_room = 'S\'wallow Valley Town Square'  # sets start location
is_win = False

while True:
    player_status()

    if current_room == 'Wayne\'s Castle':
        if len(inventory) < 6:
            print('You stumble into Wayne\'s Castle, unprepared for \n'
                  'the battle ahead. As the evil wizard Wayne Skylar \n'
                  'towers over you, you fall to your knees in defeat. \n'
                  'If only you had collected all the items!')
            print('Thanks for playing, try again soon!')
            break
    player_command = input()
    input_words = player_command.split(' ')

    if len(input_words) > 2 or len(input_words) < 1:
        print('Invalid command. Please try again.')

    first_word = input_words[0].capitalize()

    if first_word == 'Exit' and len(input_words) == 1:
        break
    elif first_word == 'Go':
        second_word = input_words[1].capitalize()

        possible_directions = rooms[current_room]
        if second_word not in possible_directions:
            print('Invalid Direction')
            continue
        current_room = possible_directions[second_word]

    elif first_word == 'Get':
        second_word = input_words[1].lower()

        if second_word != 'item':
            print('Invalid command. Please try again.')
            continue
        item_in_current_room = rooms[current_room]['item']

        if item_in_current_room in inventory:
            print('You already have this item, ya turkey!')
        inventory.append(item_in_current_room)
        if len(inventory) == 6:
            is_win = True
            break
    else:
        print('Invalid command ya dang dingus! Please try again')

if is_win:
    print('As you collect the last of the items you need to \n'
          'battle the evil wizard Wayne Skylar, you look to \n'
          'the sky and shout \"I\'m coming Princess Janny! \n'
          'You storm Wayne\'s Castle and slay the Wayne where \n'
          'he stands. Congratulations! You\'ve saved Princess Jan!')
else:
    print('loss')

print('Thanks for playing')