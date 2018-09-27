from functions.reset import reset
reset()
def menu():
    start_game_loop = 0
    name_loop = 0
    while start_game_loop < 1:
        while name_loop < 1:
            print("Welcome to Caverns, poor soul.")
            print("Press m to return to the menu at any time.")
            print("This will not reset your progress, and you will start where you left off.")
            print("What is your name?")
            name = input("")

            if name == 0:
                print("Please enter a valid name.")
            else:
                name_loop += 1
        

        print("Are you prepared for Caverns", name + "? (y/n)")
        start_game = input("")

        if "yes" in start_game or start_game == "y":
            print("Good, be prepared.")
            start_game_loop += 1
        else:
            print("Come back when you're ready")
            print(format('-','-<25'))
