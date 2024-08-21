import time
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
        print("You find yourself lying on the ground in a dim, musty cellar. You are in a cell but the door has been unlocked and left open.")
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
        print("He moves closer, 'I have been here a while... hiding... I don't know if there is a way out... They hurt people...'")
        print("He pauses, 'Wait... This was a trap, wasn't it?!', he shouts. The stranger pulls out an object that reflects what little light there is. A sword!")
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
        print("--------------------------")

        choice = input("Enter 'drink one' or 'go back': ").lower()

        if choice == 'drink one':
            self.sedated = True
            self.health += 2
            print("--------------------------")
            print(f"You feel better. Your health is now: {self.health}.")
            print("However, you start to feel a little groggy and it becomes hard to walk.")
            print(f"You have been sedated! Your sedated status is {self.sedated}")
            print("--------------------------")
            
            choice = input("Enter 'hallway':").lower()
            
            if choice == "hallway":
                print("You return to the hallway and continue down the corridor.")
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
        print("--------------------------")

        choice = input("Type 'investigate chamber': ").lower()

        if choice == "investigate chamber": 
            self.investgate_chamber()

    def investgate_chamber(self):
        print("--------------------------")
        print("You walk boldly into the middle of the chamber.")
        print("You walk up to one of the tables to investigate.")
        print("As you get closer, you see... human body parts!")
        print("You stumble backwards and bump into another table.")
        print("You turn around to see a man with his scalp cut open and his brain exposed.")
        print("A strange machine is attached to his brain...")
        print("'Hello', you hear a soft voice say behind you.")
        print("You turn around to see an attractive woman standing in front of you.")
        print("'What are YOU doing out here?', she asks.")
        print("--------------------------")

        choice = input("Enter 'question her' or 'attack her': ").lower()

        if choice == "question her":
            self.question_her()
        elif choice == "attack her":
            self.attack_her()
        else:
            print(self.invalid_choice)
            self.investgate_chamber()

    def question_her(self):
        print("--------------------------")
        print("Who are you?, you ask wearily.")
        print("'Who am I?', she says with a smile. She steps closer to you.")
        print("'I'm here to help you', she says and takes another stop closer.")
        print("You are unsure who this lady is and she keeps moving closer.")
        print("--------------------------")

        choice = input("Enter 'let her approach' or 'attack her': ").lower()

        if choice == "let her approach":
            self.let_her_approach()
        elif choice == "attack her":
            self.attack_her()
        else:
            print(self.invalid_choice)
            self.question_her()

    def let_her_approach(self):
        print("--------------------------")
        print("You are in a strange place and you decide to trust the woman.")
        print("She is now standing right in front of you with a soft smile on her face.")
        print("Suddenly, she swings her arm accross your neck. Blood spurts onto her.")
        print("You look at her but she is no longer the woman you saw earlier.")
        print("A horrendous muscular monster stands in front of you with claws and fangs.")
        print("It lets out a menacing laugh as you fall to the ground.")

        time.sleep(3)

        self.game_over()

    def attack_her(self):
        if "sword" in self.inventory:
            print("--------------------------")
            print("You attack her with your sword.")
            print("The woman looks at you and lets out a frustrated cry.")
            print("Suddenly there is no longer a woman standing in front of you.")
            print("A horrid beast with fangs and claws has replaced her with a slice accross its chest from your sword.")
            print("'You will regret that,' the beast says in a menacing voice.")
            print("It lunges at you with its claws.")
            print("--------------------------")

            choice = input("Enter 'parry' or 'dodge': ").lower()

            if choice == "parry":
                self.parry()
            elif choice == "dodge":
                self.dodge()
            else:
                print(self.invalid_choice)
                self.attack_her()
        else:
            print("--------------------------")
            print("You punch the woman in the face.")
            print("The woman barely budges. She smiles at you.")
            print("Suddenly, she swings her arm accross your neck. Blood spurts onto her.")
            print("You look at her but she is no longer the woman you saw earlier.")
            print("A horrendous monster stands in front of you with claws and fangs.")
            print("It lets out a menacing laugh as you fall to the ground.")

            time.sleep(3)

            self.game_over()

    def parry(self):
        if self.sedated:
            print("--------------------------")
            print("You try to parry the monster but the sedative affects your reflexes.")
            print("You miss the parry and the monsters claws slash accross your chest.")

            time.sleep(3)

            self.game_over()
        else:
            print("--------------------------")
            print("You parry the monster's attack deflecting it and knocking it off balance.")
            print("It knicked you arm during the parry and you lose 4 health.")
            self.health = self.health - 4
            print("Your health is now:", self.health)
            print("--------------------------")

            choice = input("Enter 'press the attack' or 'try to escape': ").lower()

            if choice == "press the attack":
                self.press_the_attack()
            elif choice == "try to escape":
                self.try_to_escape()
            else:
                print(self.invalid_choice)
                self.parry()

    def dodge(self):
        if self.sedated:
            print("--------------------------")
            print("You try to dodge the monster but the sedative affects your reflexes.")
            print("You sloppily dodge the monsters attack and it grazes your side.")
            print("It stumbles as it tries to regain its composure.")
            self.health = self.health - 3
            print("You lose 3 health. Your health is now:", self.health, ".")

            choice = input("Enter 'press the attack' or 'try to escape': ").lower()

            if choice == "press the attack":
                self.press_the_attack()
            elif choice == "try to escape":
                self.try_to_escape()
            else:
                print(self.invalid_choice)
                self.dodge()
        else:
            print("--------------------------")
            print("You dodge the monster's attack and it barely misses you.")
            print("It stumbles as it tries to regain its composure.")

            choice = input("Enter 'press the attack' or 'try to escape': ").lower()

            if choice == "press the attack":
                self.press_the_attack()
            elif choice == "try to escape":
                self.try_to_escape()
            else:
                print(self.invalid_choice)
                self.dodge()

    def press_the_attack(self):
        if self.sedated:
            print("--------------------------")
            print("You press the attack but the sedative affects your reflexes.")
            print("You miss the attack and the monsters claws slash accross your chest.")

            time.sleep(3)

            self.game_over()
        else:
            print("--------------------------")
            print("With your opening, you press the attack and drive your sword through the monsters torso.")
            print("It cries as it starts to burn. A vampire! And this must be a silver sword.")
            print("It falls to the floor and slowly disintegrates into ash.")
            print("You look around to see a door at one end of the chamber.")
            print("You walk up to the door and open it.")
            print("It leads outside to a grove. You have escaped.")

            self.enemies_slain = self.enemies_slain + 1

            self.victory()
    
    def try_to_escape(self):
        if self.sedated:
            print("--------------------------")
            print("While the monster recovers, you search for an exit.")
            print("You see one on the other side of the chamber.")
            print("You make a run for it but the sedative slows you down.")

            choice = input("Enter 'keep running' or 'try to slow monster': ").lower()

            if choice == "keep running":
                self.keep_running()
            elif choice == "try to slow monster":
                self.try_to_slow_monster()
            else:
                print(self.invalid_choice)
                self.try_to_escape()
        else:
            print("--------------------------")
            print("While the monster recovers, you search for an exit.")
            print("You see one on the other side of the chamber.")
            print("You make a run for it.")
            print("You make it the door, open it and run through. It leads to a sunlit grove.")
            print("You look behind you to see the monster standing at the chamber entrance.")
            print("A vampire! It cannot come out into the sunlight. You have escaped!")

            self.victory()
 

    def keep_running(self):
        print("--------------------------")
        print("You try to run for the exit but you are too sedated to make it.")
        print("The monster catches you and ends you.")

        self.game_over()

    def try_to_slow_monster(self):
        print("--------------------------")
        print("You sloppily knock over one of the tables as the monster recovers.")
        print("The table falls to the floor and body parts strew accross the floor.")
        print("You run for the door hearing the monster struggle behind you.")
        print("You make it the door, open it and run through. It leads to a sunlit grove.")
        print("You look behind you to see the monster standing at the chamber entrance.")
        print("A vampire! It cannot come out into the sunlight. You have escaped!")

        self.victory()

    def game_over(self):
        print("--------------------------")
        print("You died! You slayed", self.enemies_slain, "enemies.")
        print("Thanks for playing!")
        print("--------------------------")

    def victory(self):
        print("--------------------------")
        print("You won! You slayed", self.enemies_slain, "enemies.")
        print("Thanks for playing!")
        print("--------------------------")


def main():
    game = SoulAdventure()
    game.start_game()

if __name__ == "__main__":
    main()