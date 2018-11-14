from functions.menu import menu
from functions.score import score

def room1():
    room1_loop = 0
    
    torch = 0
    match = 0

    
    while room1_loop < 1:
        torch_loop = 0
        match_loop = 0
        
        if torch == 0 and match == 0:
            print("You're in a dark room with a torch and a match, what's next?")
            room1talk = input("")
        elif torch == 0 and match == 1:
            print("The dark room contains only a torch now. What's next?")
            room1talk = input("")
        elif torch == 1 and match == 0:
            print("The room is now completely lit by the torch, but a match still remains. What's next?")
            room1talk = input("")
        elif torch == 1 and match == 1:
            print("You should probably search for a door, since you have the items in the room.")
            room1talk = input("")
            
        if "torch" in room1talk:
            while torch_loop == 0:
                if torch == 0:
                    print("You grab the torch")
                    torch += 1
                    torch_loop += 1
                    score(100)
                else:
                    print("You have the torch already.")
                    torch_loop += 1
        elif "match" in room1talk:
            while match_loop == 0:
                if match == 0:
                    print("You grab the match")
                    match += 1
                    match_loop += 1
                    score(400)
                else:
                    print("You have the match already.")
                    match_loop += 1
        elif "search" in room1talk:
            if torch == 1:
                print("You use the torch to scour the walls and find a small stone button. What will you do? Keep in mind you will probably not be able to return. ")
                room1button = input("")
                if "push" in room1button:
                    print("You push the button, revealing a door on the opposite side of the room. You continue through the next passage.")
                    score(500)
                    break
                else:
                    print("You turn back, without pushing the button.")
                    continue
            else:
                print("You need a light source to search the room.")
        elif room1talk == "m":
            menu()
        else:
            print("You cannot do that.")
            continue

