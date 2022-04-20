# Jacob Sullivan Module 6 Milestone

rooms = {
    'S\'wallow Valley Town Square': {
        'South': 'Channel 5 News Station',
        'West': 'Steve Mahanahan\'s Child Clown Outlet',
        'North': 'Jan\'s Castle',
        'East': 'Wayne\'s Castle'},
    'Channel 5 News Station': {'North': 'S\'wallow Valley Town Square'},
    'Steve Mahanahan\'s Child Clown Outlet': {"South": "S\'wallow Valley Mall",
                                              'East': 'S\'wallow Valley Town Square'},
    'S\'wallow Valley Mall': {'North': 'Steve Mahanahan\'s Child Clown Outlet'},
    'Jan\'s Castle': {'South': 'S\'wallow Valley Town Square',
                      'East': 'House of Doris Pringle Brule'},
    'House of Doris Pringle Brule': {'West': 'Jan\'s Castle',
                                     'North': 'S\'wallow Valley Lake'},
    'S\'wallow Valley Lake': {'South': 'House of Doris Pringle Brule'},
    'Wayne\'s Castle': {'West': 'S\'wallow Valley Town Square'}
}


def player_status():  # sets up info returned to give player context about location
    print('-------------------')
    print(' You are in the {}'.format(current_room))
    print('-------------------')


current_room = 'S\'wallow Valley Town Square'  # sets start location

while current_room == 'S\'wallow Valley Town Square':
    player_status()
    player_move = input('Choose a way you would like to go:\n')
    if player_move == 'exit':
        current_room = 'exit'
        print('Thanks for playing!')
    elif player_move == 'South' or player_move == 'south':
        current_room = 'Channel 5 News Station'
        player_status()
        print('Choose a way you would like to go:\n')
    elif player_move == 'East' or player_move == 'east':
        current_room = 'Wayne\'s Castle'
        print('You lose')
        break
    elif player_move == 'West' or player_move == 'west':
        current_room = 'Steve Mahanahan\'s Child Clown Outlet'
        player_status()
        print('Choose a way you would like to go:\n')
    elif player_move == 'North' or player_move == 'north':
        current_room = 'Jan\'s Castle'
        player_status()
        print('Choose a way you would like to go:\n')
    else:
        print('Invalid move')

while current_room == 'Channel 5 News Station':
    player_status()
    player_move = input('Choose a way you would like to go:\n')
    if player_move == 'exit':
        current_room = 'exit'
        print('Thanks for playing!')
    elif player_move == 'North':
        current_room = 'S\'wallow Valley Town Square'
        player_status()
        print('Choose a way you would like to go:\n')
    elif player_move != 'exit' or player_move != 'North' or player_move != 'north':
        print('Invalid move')
    else:
        player_status()

while current_room == 'Steve Mahanahan\'s Child Clown Outlet':
    player_status()
    player_move = input('Choose a way you would like to go:\n')
    if player_move == 'exit':
        current_room = 'exit'
        print('Thanks for playing!')
    elif player_move == 'East' or player_move == 'east':
        current_room = 'S\'wallow Valley Town Square'
        player_status()
        print('Choose a way you would like to go:\n')
    elif player_move == 'South' or player_move == 'south':
        current_room = 'S\'wallow Valley Mall'
        player_status()
        print('Choose a way you would like to go:\n')
    elif player_move != 'exit' or player_move != 'East' or player_move != 'east' \
            or player_move != 'South' or player_move != 'south':
        print('Invalid move')
    else:
        player_status()

while current_room == 'S\'wallow Valley Mall':
    player_status()
    player_move = input('Choose a way you would like to go:\n')
    if player_move == 'exit':
        current_room = 'exit'
        print('Thanks for playing!')
    elif player_move == 'North' or player_move == 'north':
        current_room = 'Steve Mahanahan\'s Child Clown Outlet'
        player_status()
        print('Choose a way you would like to go:\n')
    elif player_move != 'exit' or player_move != 'North' or player_move != 'north':
        print('Invalid Move')
    else:
        player_status()

while current_room == 'Jan\'s Castle':
    player_status()
    player_move = input('Choose a way you would like to go:\n')
    if player_move == 'exit':
        current_room = 'exit'
        print('Thanks for playing!')
    elif player_move == 'South' or player_move == 'south':
        current_room = 'S\'wallow Valley Town Square'
        player_status()
        print('Choose a way you would like to go:\n')
    elif player_move == 'East' or player_move == 'east':
        current_room = 'House of Doris Pringle Brule'
        player_status()
    elif player_move != 'exit' or player_move != 'East' or player_move != 'east' \
            or player_move != 'South' or player_move != 'south':
        print('Invalid move')
    else:
        player_status()

while current_room == 'House of Doris Pringle Brule':
    player_status()
    player_move = input('Choose a way you would like to go:\n')
    if player_move == 'exit':
        current_room = 'exit'
        print('Thanks for playing!')
    elif player_move == 'West' or player_move == 'west':
        current_room = 'Jan\'s Castle'
        player_status()
        print('Choose a way you would like to go:\n')
    elif player_move == 'North' or player_move == 'north':
        current_room = 'S\'wallow Valley Lake'
        player_status()
        print('Choose a way you would like to go:\n')
    elif player_move != 'exit' or player_move != 'West' or player_move != 'west' \
            or player_move != 'North' or player_move != 'north':
        print('Invalid move')
    else:
        player_status()

while current_room == 'S\'wallow Valley Lake':
    player_status()
    player_move = input('Choose a way you would like to go:\n')
    if player_move == 'exit':
        current_room = 'exit'
        print('Thanks for playing!')
    elif player_move == 'South' or player_move == 'south':
        current_room = 'S\'wallow Valley Town Square'
        player_status()
        print('Choose a way you would like to go:\n')
    elif player_move != 'exit' or player_move != 'South' or player_move != 'south':
        print('Invalid move')
    else:
        player_status()
