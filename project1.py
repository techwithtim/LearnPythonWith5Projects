name = input("Hey type your name: ")
print("Hello " + name + " welcome to my game!")

should_we_play = input("Do you want to play? ").lower()

if should_we_play == "y" or should_we_play == "yes":
    print("We are gonna play!")

    direction = input("Do you want to go left or right? (left/right) ").lower()
    if direction == "left":
        print("You went left and fell of a cliff, game over, try again.")
    elif direction == "right":
        choice = input(
            "Okay, you now see a bridge, do you want to swim under it or cross it? (swim/cross) "
        )
        if choice == "swim":
            print("You got eaten by an alligator, you die, the end!")
        else:
            print("You found the gold and won!")
    else:
        print("Sorry not a valid reply, you die!")

else:
    print("We are NOT playing...")
