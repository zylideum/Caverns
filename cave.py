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

##End Menu Loop

##Start Room 1 Loop

print("You're in a dark room with a torch and a match, what's next?")
room1torch = input("")
room1torch = room1torch.split()
room1torch = list(room1torch)
room1_loop = 0

torch = 0
match = 0

while room1_loop < 1:
    for i in range(0, len(room1torch)):
        if room1torch[i] == "torch" and torch == 0:
            print("You grab the torch")
            torch += 1
        elif torch == 1:
            print("You have the torch already.")
        elif room1torch[i] == "match" and match == 0:
            print("You grab the match")
        elif match == 1:
            print("You have the match already.")
