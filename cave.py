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
room1talk = input("")
room1_loop = 0
torch_loop = 0
match_loop = 0

torch = 0
match = 0

while room1_loop < 1:
        if "torch" in room1talk:
            while torch_loop == 0:
                print("You grab the torch")
                if match == 0:
                    print("You're in a dark room with just a match, what's next?")
                torch += 1
                torch_loop += 1
                continue
            if torch == 2:
                print("You have the torch already.")
                torch_loop += 1
        elif "match" in room1talk:
            while match_loop == 0:
                print("You grab the match")
                if torch == 0:
                    print("You're in a dark room with just a torch, what's next?")
                match += 1
                match_loop += 1
                continue
            if match == 1:
                print("You have the match already.")
