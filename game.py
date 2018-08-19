print("""you
do you go through door #1 or door #2?"""
door = input("> ")

if door == "1":
    print("there are savages gathered around to eat meat.")
    print("what do you do?")
    print("1. attack savages with a pistol.")
    print("2. run in the opposite direction.")
    print("3. ")

    savages = input("> ")

    if savages == "1":
        print("they grabbed you and ate you.")
        print("prefect!")
    elif savages == "2":
        print("they froze for a moment and then grabbed you.")
        print("good job!")

elif door == "2":
    print("you stare into the endless abyss at cthuluhu's retina.")
    print("1. blueberries.")
    print("2. yellow jacket clothespins.")
    print("3. understanding revolvers yelling melodies.")
    
    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("your body survives powered by a mind of jello.")
        print("good job!")
    else:
        print("the insanity rots your eyes into a pool of muck.")
        print("good job!")

else:
    print("you stumble around and fall on a knife and die.  good job!")