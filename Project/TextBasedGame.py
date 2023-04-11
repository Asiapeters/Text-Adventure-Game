# Asia Peters
def instructions():
    """ print a main menu and the commands """
    print("School Supplies Text Adventure Game")
    print("Collect 7 items to win the game, or get caught by security.")
    print("Move commands: go South, go North, go East, go West\nAdd to Inventory: get 'item name'")


def rooms_dict():
    """ Creates a dictionary for rooms and directions"""
    rooms = {'Entrance': {'east': 'Parking Lot', 'south': 'Main Hallway'},
             'Parking Lot': {'west': 'Entrance', 'item': 'backpack'},
             'Main Hallway': {
                 'north': 'Entrance',
                 'east': 'East Locker Corridor',
                 'south': 'South Locker Corridor',
                 'west': 'Office',
                 'item': 'pencil'},
             'Office': {'east': 'Main Hallway', 'item': 'Security'},
             'East Locker Corridor': {
                 'east': 'Gym',
                 'south': 'Library',
                 'west': 'Main Hallway',
                 'item': 'calculator'},
             'Gym': {'west': 'East Locker Corridor', 'item': 'binder'},
             'South Locker Corridor': {
                 'north': 'Main Hallway',
                 'east': 'Library',
                 'south': 'Auditorium',
                 'west': 'Cafeteria',
                 'item': 'flash drive'
             },
             'Cafeteria': {'east': 'South Locker Corridor', 'item': 'lunch box'},
             'Library': {
                 'north': 'East Locker Corridor',
                 'west': 'South Locker Corridor',
                 'item': 'computer science book'
             },
             'Auditorium': {'north': 'South Locker Corridor', 'item': 'notebook'}
             }
    return rooms


def status(room_dict, location, inventory):
    """Shows current status of location and inventory
        Arguments:
        room_dict -- dictionary for all available rooms
        location -- string representing current location user is in
        inventory -- list of items user has
    """
    if location == 'Entrance':
        print('\nYou are at the', location)
        print('Inventory:', inventory)
        print('-' * 30)
    else:
        for room in room_dict:
            if location == room:
                print('\nYou are in the', room)
                print('Inventory:', inventory)
                if 'item' in room_dict[room]:
                    print('You see a', room_dict[room]['item'])
                print('-' * 30)
                break
        else:
            print('Error')


def move_rooms(rooms, room, command):
    """Moves user to another room based on direction
        Arguments:
        rooms -- dictionary of all rooms and directions available
        room -- string of currrent room user is in
        command -- string of direction user wants to go to
    """
    new_room = room
    if command == 'north' or command == 'east' or command == 'south' or command == 'west':
        for direction in rooms[room]:
            if command == direction:
                new_room = rooms[room][command]
        else:
            if room == new_room:
                print('You can\'t go that way!')
            else:
                room = new_room
    else:
        print('Invalid Input!')
    return room


def add_item(inventory, rooms, room, command):
    """Adds item to users inventory
        Arguments:
        inventory -- list of items that user has
        rooms -- dictionary of rooms with correlated directions
        room -- string representing room user is in
        command -- string representing action to get item
    """
    if 'item' in rooms[room]:
        if command == rooms[room]['item']:
            item = rooms[room]['item']
            inventory.append(item)
            del rooms[room]['item']
        else:
            print('Can\'t get {}!'.format(command))
    else:
        print('Can\'t get {}!'.format(command))


def gane_result(inventory, requirement):
    """Result after ggame is finished
        Arguments:
        inventory -- list of items that user has
        requirement -- int required for inventory after game ends
    """
    # calculates if number of items in inventory matches requirement to win gaame
    if len(inventory) >= requirement:
        print('You have collected all of the school supplies')
    else:
        print('\nYou were caught by security!')
        print('GAME OVER')
    print('Thanks for plauing!')


def action_input():
    """Requests user to enter action command"""
    direction = ''
    command = input('Enter your move:\n').lower().split()

    # calculates length of command list
    if 1 < len(command) <= 2:
        direction = command[1]
    elif len(command) > 2:
        # adds extra words to direction string
        for index, word in enumerate(command[:-1]):
            if index == 0:
                continue
            direction += command[index] + ' '
        direction += command[-1]
    action = command[0]
    return action, direction


def main():
    """Starts game"""
    num_items = 7
    rooms = rooms_dict()
    inventory = []
    location = 'Entrance'
    instructions()
    # Determines if rooms has villain to end game
    while len(inventory) < num_items:
        if 'item' in rooms[location]:
            if rooms[location]['item'] == 'Security':
                break
        status(rooms, location, inventory)
        action, direction = action_input()
        # Determines if action word is 'go' or 'get'
        if action == 'go':
            location = move_rooms(rooms, location, direction)
            continue
        elif action == 'get':
            add_item(inventory, rooms, location, direction)
        else:
            print('Invalid Inpot!')
    gane_result(inventory, num_items)


if __name__ == '__main__':
    main()
