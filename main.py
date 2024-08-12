def start_game():
    print("Welcome to the Python Adventure!")
    print("You find yourself at a crossroad.")
    print("Do you want to go left or right?")
    
    choice = input("Enter 'left' or 'right': ").lower()
    
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("Invalid choice. Game over!")

def left_path():
    print("You've chosen the left path.")
    print("You see a dark cave ahead.")
    print("Do you want to enter the cave or turn back?")
    
    choice = input("Enter 'enter' or 'back': ").lower()
    
    if choice == "enter":
        print("You enter the cave and find a treasure chest!")
        print("Congratulations, you win!")
    elif choice == "back":
        print("You turn back and return to the crossroad.")
        start_game()
    else:
        print("Invalid choice. Game over!")

def right_path():
    print("You've chosen the right path.")
    print("You come across a river.")
    print("Do you want to swim across or look for a bridge?")
    
    choice = input("Enter 'swim' or 'bridge': ").lower()
    
    if choice == "swim":
        print("You attempt to swim but the current is too strong.")
        print("Game over!")
    elif choice == "bridge":
        print("You find a bridge and safely cross the river.")
        print("You see a castle in the distance. You win!")
    else:
        print("Invalid choice. Game over!")

# Start the game
start_game()