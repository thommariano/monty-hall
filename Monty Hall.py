import numpy as np

data = {'Winner':{'Change Door':0,'Kept Door':0,'Total Runs':0}}

count = 0
while True:
    count += 1
    doors = [0, 0, 0]
    chosen_doors = [0, 0, 0]
    prize_door = np.random.randint(0,3)
    doors[prize_door] = 1
    print('There are three doors in front of you.\nInside of each door is either a goat or your prize.')
    print('In total there are two goats and one prize. \nWhich door do you choose?\n')
    # Try/except logic to ensure user inputs a 1,2 or 3.
    try:
        n = int(input('Choose a door: [1] [2] [3]: '))
        print('')
        if n > 3:
            raise Exception('Your input is a number greater three. \n')
            break
    except ValueError:
        print('You did not enter a valid number. \n')
        break
    chosen_doors[n-1] = 1
    # Logic for showing user a door with goat behind it
    goat_door = np.random.randint(0,3)
    while (goat_door == prize_door or goat_door+1 == n):
        goat_door = np.random.randint(0,3)
    print('There is a goat in door number: {}'.format(goat_door+1))
    # Logic for user input yes or no if they want to switch door
    last_door = [1,2,3]
    last_door.remove(n)
    last_door.remove(goat_door+1)
    last_door = last_door[0]
    switch = input('Do you wish to switch your door to door [{}]? (yes/no):'.format(last_door)).lower()
    while (switch != 'yes' and switch != 'no'):
        print('Your input was not yes or no. \n')
        switch = input('Do you wish to switch your door to door [{}]? (yes/no):'.format(last_door)).lower()
    if switch == 'yes':
        chosen_doors = [0, 0, 0]
        chosen_doors[last_door-1] = 1
    # Winner/Loser
    print(chosen_doors)
    print(doors)
    if chosen_doors == doors:
        print('')
        print('You win $1M, congratulations! \n')
        if switch == 'yes':
            data['Winner']['Change Door'] += 1
        else:
            data['Winner']['Kept Door'] += 1
    else:
        print('')
        print('You have chosen the goat door. \n')
    # Logic for user input yes or no if they want to continue playing
    end = input('Do you wish to end the Monty Hall problem? (yes/no):').lower()
    while (end != 'yes' and end != 'no'):
        print('Your input was not yes or no. \n')
        end = input('Do you wish to end the Monty Hall problem? (yes/no):').lower()
    if end == 'yes':
        data['Winner']['Total Runs'] = count
        break
    print('')
        
