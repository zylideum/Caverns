def menu():
    start_game_loop = 0
    name_loop = 0
    while start_game_loop < 1:
        while name_loop < 1:
            print("Welcome to Caverns")

            print("What is your name?")
            name = input("")

            if name == 0:
                print("Please enter a valid name")
            else:
                name_loop += 1
        

        print("Are you prepared for Caverns", name + "? (y/n)")
        start_game = input("")

        if start_game == 'y':
            print("Good, get ready.")
            start_game_loop += 1
        else:
            print("Come back when you're ready")
            print(format('-','-<25'))
