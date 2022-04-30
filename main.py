# Trent Ricks
# commonly used phrase in functions
phrase = "You can't go that way."

# items
sword = 'sword'
key = 'key'
compass = 'compass'
boots = 'boots'
map1 = 'map'
boat = 'boat'
treasure = 'treasure'

# empty list for user to add items to
inventory = []

# function to exit the game
def game_over():
    print('You have been defeated')

# functions to move between rooms
def kitchen():
    print('You are in the Kitchen')
    if sword not in inventory:
        print('you see a sword on the counter, type grab to pick it up')
    answer = input('Enter direction: ').lower().strip()
    item = sword
    if answer == 'east':
        bathroom()
    elif answer == 'south':
        great_hall()
    elif answer == 'exit':
        game_over()
    elif answer == 'grab':
        inventory.append(item)
        print('the {} has been grabbed'.format(item))
        print('you have', inventory,'in your inventory')
        kitchen()
    else:
        print(phrase)
        kitchen()

def great_hall():
    print('You are in the Great Hall')
    answer = input('Enter direction: ').lower().strip()
    if answer == 'north':
        kitchen()
    elif answer == 'south':
        lake()
    elif answer == 'east':
        master_bedroom()
    elif answer == 'west':
        study()
    elif answer == 'exit':
        game_over()
    else:
        great_hall()

def bathroom():
    print('you are in the Bathroom')
    if key not in inventory:
        print('you see a key, type grab to pick it up')
    answer = input('Enter direction: ').lower().strip()
    item = key
    if answer == 'west':
        kitchen()
    elif answer == 'exit':
        game_over()
    elif answer == 'grab':
        inventory.append(item)
        print('the {} has been grabbed'.format(item))
        print('you have', inventory,'in your inventory')
        bathroom()

    else:
        print(phrase)
        bathroom()

def study():
    print('You are in the Study')
    if map1 not in inventory:
        print('you see a map, type grab to pick it up.')
    answer = input('Enter direction: ').lower().strip()
    item = map1
    if answer == 'east':
        great_hall()
    elif answer == 'exit':
        game_over()
    elif answer == 'grab':
        inventory.append(item)
        print('the {} has been grabbed'.format(item))
        print('you have', inventory,'in your inventory')
        study()
    else:
        print(phrase)
        study()

def master_bedroom():
    print('You are in the Master Bedroom')
    if boots not in inventory:
        print('There are muddy boots in the corner, type grab to pick them up')
    item = boots
    answer = input('Enter directions: ').lower().strip()
    if answer == 'north':
        walk_in_closet()
    elif answer == 'west':
        great_hall()
    elif answer == 'exit':
        game_over()
    elif answer == 'grab':
        inventory.append(item)
        print('the {} has been grabbed'.format(item))
        print('you have', inventory,'in your inventory')
        master_bedroom()
    else:
        print(phrase)
        master_bedroom()

def walk_in_closet():
    print('You are in the Walk In Closet')
    if compass not in inventory:
        print('You see a compass on the shelf, type grab to pick it up')
    answer = input('Enter directions: ').lower().strip()
    item = compass
    if answer == 'south':
        master_bedroom()
    elif answer == 'exit':
        game_over()
    elif answer == 'grab':
        inventory.append(item)
        print('the {} has been grabbed'.format(item))
        print('you have', inventory,'in your inventory')
        walk_in_closet()
    else:
        print(phrase)
        walk_in_closet()

def lake():
    print('You are by the Lake')
    if boat not in inventory:
        print('you see a boat tied up to the dock, type enter to get in')
    answer = input('Enter direction: ').lower().strip()
    item = boat
    if answer == 'north':
        great_hall()
    elif answer == 'east':
        island()
    elif answer == 'exit':
        game_over()
    elif answer == 'enter':
        inventory.append(item)
        print('the {} has been grabbed'.format(item))
        print('you have', inventory,'in your inventory')
        lake()
    else:
        print(phrase)
        lake()

def island():
    print('You have entered the Island')
    if len(inventory) >= 6:
        print('You have defeated the pirate! Type grab to save the treasure')
        answer = input('Enter direction: ').lower().strip()
        if answer == 'grab':
            print('You have saved the treasure!')
            print('The game is now over')
        elif answer == 'exit':
                game_over()
        else:
            island()
    else:
        print('You did not have all the items needed to defeat the pirate')
        game_over()

# function to start the game
def start():
    print('Welcome to the pirate adventure game.')
    print('Acceptable directions are north, south, east, and west')
    print('Enter exit to quit')
    print('You will need to gather six items before entering the island or you will lose')
    print('Good luck!')
    great_hall()


start()
