from functions.menu import menu
from functions.room1 import room1
from functions.score import score

def room2():
    room2_loop = 0

    room3_key = 0
    room4_key = 0
    hidden_gem = 0
    bone = 0

    while room2_loop < 1:
        hidden_gem_loop = 0
        room4_key_loop = 0
        room3_key_loop = 0
        bone_loop = 0

        if room3_key == 0 and room4_key == 0:
            print("You enter the next room right as your torch burns out.",
            "The matches are wet and unusable, but they were valuable for",
            "your final score. In the darkness, you can feel that the room",
            "is much smaller than the last, but there are many rocks laying",
            "on the ground. A large rock, a small rock, a wet rock, and a",
            "broken rock. What do you decide to do?")
            room2talk = input("")
        elif room3_key == 1 and room4_key == 0:
            print("Now that you have a key, maybe you should scour the floor some more.")
            room2talk = input("")
        elif room4_key == 1 and room3_key == 0:
            print("This golden key feels as if it could open anything... like a ceiling.")
            room2talk = input("")


        if "large" in room2talk:
            if room4_key == 0:
                while room3_key_loop == 0:
                    if room3_key == 0:
                        print("You found the key to the third room! Where could it be?")
                        room3_key += 1
                        room3_key_loop += 1
                        score(500)
                    else:
                        print("You already have the key to the third room, but where could it be?")
                        room3_key_loop += 1
            else:
                print("You already have a golden key and can't carry more.")
                continue
        elif "wet" in room2talk:
            if room3_key == 0:
                while room4_key_loop == 0:
                    if room4_key == 0:
                        print("You found a golden key! This could probably get you pretty far.")
                        room4_key += 1
                        room4_key_loop += 1
                        score(1000)
                    else:
                        print("You already picked up the golden key.")
                        room4_key_loop += 1
            else:
                print("You already have a key and can't carry more.")
                continue
        elif "small" in room2talk:
            while bone_loop == 0:
                if bone == 0:
                    print("You found an old bone... that's not promising.")
                    bone += 1
                    bone_loop += 1
                    score(2)
                else:
                    print("You've already picked up the bone for whatever reason.")
                    bone_loop += 1
        elif "broken" in room2talk:
            while hidden_gem_loop == 0:
                if hidden_gem == 0:
                    print("You found a hidden gem!")
                    hidden_gem += 1
                    hidden_gem_loop += 1
                    score(5000)
                else:
                    print("You're too greedy. You have the gem in your bag.")
                    hidden_gem_loop += 1
        elif "ceiling" in room2talk:
            if room4_key == 1:
                print("You open the grate above you and manage to crawl through a series of tunnels to safety! Congratulations!")
                score(1000)
                break
            else:
                print("You have nothing to open it, but you feel a grate above you.")
                continue
        elif "floor" in room2talk:
            if room3_key == 1:
                print("You find a keyhole in the floor and continue to a secret treasure room.")
                score(500)
                #room3()
                break
            else:
                print("You feel around and find a keyhole, but you have nothing to open it.")
                continue
        elif room2talk == "m":
            menu()
        else:
            print("You cannot do that.")
            continue
            
        
        

        
            
