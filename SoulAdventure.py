
class SoulAdventure:
    def __init__(self):
        self.enemies_slain = 0
        self.inventory = []
        self.health = 10
        self.invalid_choice = "Invalid choice. Try again."

        if self.health <= 0:
            self.game_over()

    def start_game(self):
        print("--------------------------")
        print("Welcome to Soul Adventure! Let's get started:")
        print("You find yourself lying on the ground in a dim, musty cellar.")
        print("You don't remember how you got here or where you are.")
        print("You stand up and look around. To your left is a dark room. To your right is a hallway that leads further into this strange place.")
        print("Do you want to go into the dark room or go down the hallway?")
        print("--------------------------")

        choice = input("Enter 'dark room' or 'hallway': ").lower()

        if choice == "dark room":
            self.dark_room()
        elif choice == "hallway":
            self.hallway()
        else:
            print(self.invalid_choice)
            self.start_game()

    def dark_room(self):
        print("--------------------------")
        print("You enter the dark room. You hear a voice calling to you.")
        print("Do you want to talk to the voice or run away?")
        print("--------------------------")

        choice = input("Enter 'talk' or 'run': ").lower()

        if choice == "talk":
            self.demented_stranger()
        elif choice == "run":
            print("--------------------------")
            print("You run back into the cellar and close the door to the dark room. No where else to go but the hallway now.")
            print("--------------------------")
            self.hallway()
        else:
            print(self.invalid_choice)
            self.dark_room()

    def demented_stranger(self):
        print("--------------------------")
        print("You see a shadowy figure in the corner of the room.")
        print("He speaks, 'Another visitor to this place I see...'")
        print("He moves closer, 'I have been here a long time... I don't know if there is a way out...'")
        print("'But exploring this place, I did find this...'. The stranger pulls out an object that reflects what little light there is. A sword!")
        print("The stranger lunges at you. You try to dodge it but he grazes your upper arm. You lose 3 health.")
        self.health = self.health - 3
        print("Your health is now:", self.health)
        print("--------------------------")

        choice = input("Enter 'fight back' or 'run away': ").lower()

        if choice == "fight back":
            self.fight_back()
        elif choice == "run away":
            print("--------------------------")
            print("The man stumbles after swinging at you. You see your chance to escape.")
            print("You run back into the cellar and close the door to the dark room. No where else to go but the hallway now.")
            print("--------------------------")
            self.hallway()
        else:
            print(self.invalid_choice)
            self.demented_stranger()

    def fight_back(self):
        print("--------------------------")
        self.health = self.health - 1
        print("After swinging at you, the stranger loses his balance in the dark and stumbles around.")
        print("You see your chance. You tackle the stranger to the ground and wrestle the sword from him.")
        print(f"However, when you obtain the sword. The stranger bites you and draws blood. You lose 1 health. Your health is now: {self.health}.")
        print("You take the sword and drive it into the stranger's torso. He gasps as he bleeds out on the floor and dies.")
        print("What the hell was that guys problem? He must have gone insane in this place.")
        self.enemies_slain = self.enemies_slain + 1
        self.inventory.append("sword")
        print(f"You take the sword. You now have {self.inventory} in your inventory.")
        print("No where else to go but the hallway now.")
        print("--------------------------")
        self.hallway()
        
    def hallway(self):
        print("--------------------------")
        print("TBC")
        print("--------------------------")

    def game_over(self):
        print("You died! You slayed", self.enemies_slain, "enemies.")
        print("Thanks for playing!")
        print("--------------------------")


def main():
    game = SoulAdventure()
    game.start_game()

if __name__ == "__main__":
    main()