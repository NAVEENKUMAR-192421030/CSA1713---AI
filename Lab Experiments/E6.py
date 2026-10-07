def vacuum_cleaner():
    room = {
        'A': 'Dirty',
        'B': 'Dirty'
    }

    current_room = 'A'

    print("Initial State:")
    print("Room A:", room['A'])
    print("Room B:", room['B'])
    print()

    while True:
        print("Current Room:", current_room)

        if room[current_room] == 'Dirty':
            print("Action: Suck")
            room[current_room] = 'Clean'
        else:
            print("Action: Move")

            if current_room == 'A':
                current_room = 'B'
            else:
                current_room = 'A'

        print("Room A:", room['A'])
        print("Room B:", room['B'])
        print()

        if room['A'] == 'Clean' and room['B'] == 'Clean':
            print("Both rooms are clean.")
            print("Goal State Reached!")
            break


vacuum_cleaner()
