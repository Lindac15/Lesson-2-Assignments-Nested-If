# Task 1: Code Correction

place = input("Choose a place: forest or cave? ")

# if place = "forest":
if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    # else action = "cross a river":
    elif action == "cross a river":
        print("You found a boat!")
#elif place = "cave":
elif place == "cave":
    print("You find a hidden treasure!")


# Task 2: Setting the Scene

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    action = input("Do you want to light a torch or proceed in the dark?")
    if action == "light a torch":
        print("You found a comfy place to rest!")
    elif action == "proceed in the dark":
        print("You tripped over a rock!")

# Task 3: Default Path

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else: pass
        
elif place == "cave":
    action = input("Do you want to light a torch or proceed in the dark?")
    if action == "light a torch":
        print("You found a comfy place to rest!")
    elif action == "proceed in the dark":
        print("You tripped over a rock!")
    else: pass
else: pass

