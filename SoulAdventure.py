
class SoulAdventure:
    def __init__(self):
        self.enemies_slain = 0
        self.inventory = []
        self.health = 10
        self.invalid_choice = "Invalid choice. Try again."
        self.sedated = False

        if self.health <= 0:
            self.game_over()

    def start_game(self):
        print("--------------------------")
        print("Welcome to Soul Adventure! Let's get started:")
        print("You find yourself lying on the ground in a dim, musty cellar.")
        print("You don't remember how you got here or where you are.")
        print("You stand up and look around. Straight ahead of you is a locked door. To your left is a dark room. To your right is a hallway that leads further into this strange place.")
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
        print("He moves closer, 'I have been here a long time... I don't know if there is a way out... They like to hurt people...'")
        print("He pauses, 'Wait... You're one of them, aren't you?'. The stranger pulls out an object that reflects what little light there is. A sword!")
        ## You're one of them aren't you?
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
        print("You search his body and find a lockpick. Too bad you don't know how to use it :(")
        self.enemies_slain = self.enemies_slain + 1
        self.inventory.append("sword")
        print(f"You take the sword. You now have {self.inventory} in your inventory.")
        print("No where else to go but the hallway now.")
        print("--------------------------")
        choice = input("Enter 'move on': ").lower()
        if choice == "move on":
            self.hallway()
        else:
            print(self.invalid_choice)
            self.fight_back()
        
    def hallway(self):
        if "sword" in self.inventory:
            print("--------------------------")
            print("You make your way down the long hallway.")
            print("Torches line the walls sparingly.")
            print("What is this place? How did I get here?")
            print("Near one of the torches, you see a crack in the wall.")
            print("Hit wall crack with sword or move on?")
            print("--------------------------")

            choice = input("Enter 'hit wall' or 'move on': ").lower()

            if choice == "hit wall":
                self.secret_room()
            elif choice == "move on":
                self.sacrificial_chamber()
            else:
                print(self.invalid_choice)
        else:
            print("--------------------------")
            print("You make your way down the long hallway.")
            print("Torches line the walls sparingly.")
            print("What is this place? How did I get here?")
            print("Near one of the torches, you see a crack in the wall.")
            print("You see an opening up ahead which leads to a large chamber.")
            print("--------------------------")
            self.sacrificial_chamber()
            ## sneak or walk in

    def secret_room(self):
        print("--------------------------")
        print("A section of the wall crumbles and you step through.")
        print("You find yourself in a storage room with a locked door on the other end.")
        print("You see shelves with restraining equipment, transportation tools, and... potions.")
        print("You walk to shelf with potions. They seem to be health potions but have a greenish tint to them.")

        choice = input("Enter 'drink one' or 'go back': ").lower()

        if choice == 'drink one':
            self.sedated = True
            self.health += 2
            print(f"You feel better. Your health is now: {self.health}.")
            print("However, you start to feel a little groggy and it becomes hard to walk.")
            print(f"You have been sedated! Your sedated status is {self.sedated}")
            
            choice = input("Enter 'hallway':").lower()
            if choice == "hallway":
                print("You return to the hallway and continue.")
                self.sacrificial_chamber()
            else: 
                print("You return to the hallway and continue.")
                self.sacrificial_chamber()
        elif choice == "move on":
            print("You return to the hallway and continue.")
            self.sacrificial_chamber()
        else:
            print(self.invalid_choice)
            self.secret_room()

    def sacrificial_chamber(self):
        print("--------------------------")
        print("The hallway opens up to a large dim chamber with torches placed about.")
        print("You stand at the hallway entrance to the room looking in.")
        print("You see tables by the torches with various pieces of equipment nearby.")
        print("It is too dim to tell what is on them from here.")
        print("You think to yourself: 'Should I walk in and see what is in here or stick to the walls of the chamber and stay in the shadows.")

        choice = input("Type 'investigate chamber' or 'stay in the shadows': ").lower()

        if choice == "investigate chamber": 
            self.investgate_chamber()

    def investgate_chamber(self):
        print("You walk boldly into the middle of the chamber.")
        print("You walk up to one of the tables to investigate.")
        print("As you get closer, you see... human body parts!")
        print("You stumble backwards and bump into another table.")
        print("You turn around to see a man with his scalp cut open and his brain exposed.")
        print("A strange machine is attached to his brain...")
        print("'Hello', you hear a soft voice say behind you.")
        print("You turn around to see an attractive woman standing in front of you.")
        print("'What are YOU doing here?', she asks.")

        choice = input("Enter 'question her' or 'attack her': ").lower()

    def game_over(self):
        print("--------------------------")
        print("You died! You slayed", self.enemies_slain, "enemies.")
        print("Thanks for playing!")
        print("--------------------------")


def main():
    game = SoulAdventure()
    game.start_game()

if __name__ == "__main__":
    main()