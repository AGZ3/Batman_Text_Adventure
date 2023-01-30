### CREATE PLAYER AND NPC CLASSES
class Player():
    def __init__(self, a=10, c=0):
        self.attackpotency = a
        self.clues = c

    def stats(self):
        return("Health: " + str(self.health) + '\n' + "Attack: " + str(self.attack) + '\n' + "Clues: " + str(self.clues))

class Henchmen():
    def __init__(self, h=15, a=5):
        self.health = h
        self.attackpotency = a

class Boss1():
    def __init__(self, h=20, a=5):
        self.health = h
        self.attackpotency = a

### DEFINE INTRODUCTION AND FAIL

def StartGame():
    print(" ")
    print(" /(_M_)\ ")
    print("|       |")
    print(" \/~V~\/ ")
    print("Batman")
    print("-------------------")
    print("A Sick Joke")
    print("-------------------")
    print("1. Start Game")
    print("2. Quit Game")



def Introduction():
    print(" ")
    print("It's a dark night in Gotham City and you, Bruce Wayne, find yourself sitting in the darkness of the Batcave... thinking...")
    print("You pick up the case file of Harley Quinn. It's been almost a year since the disappearance of the Joker.")
    print("Harley still has a slew of Joker's henchman on payroll. She's planning something... but what? Maybe she's...")
    print("The phone rings. It's Comissioner Gordon.")

def Fail():
    print(" ")
    print("The next day arrives in the blink of an eye. Another dreamless night. You turn on the television and see the headline:")
    print("Gotham City citizens found dead in their homes bearing eerie smiles on their faces. How could this be? It seems you made the wrong decision.")


def main():

### CREATE ROOM MAP
    location = {
        'Batcave': {'name': 'The Batcave', 'items': '1'},
        'Gotham City': {'name': 'Gotham City', 'items': '1'},
        'Ace Chemicals': {'name': 'Ace Chemicals', 'items': '1'},
        'Clocktower': {'name': 'The Clocktower', 'items': '0'}
        }

### ASSETS

    inventory = ['***', '***', '***']
    p = Player()
    h = Henchmen()
    b = Boss1()

### GAME LOOP

    while True:

        StartGame()
        STARTGAME = input("Select an option (1/2): ")

        if STARTGAME == '1':

            ### CHAPTER 1: BATCAVE ###

            current_location = location['Batcave']

            Introduction()

            print(" ")
            d1 = input("Do you pick up the phone? (y/n): ")
            print(" ")

            if d1 =='y':
                print("Gordon: Batman... This is serious. We stumbled upon a crime scene I think you should take a look at. The victims look... well... like the joker? I'm not sure what's going on but im pinging the location.")
                print(" ")
                print("You hang up the phone. They look like the joker? What could that mean?")

                print(" ")
                d2 = input("Do you suit up and pursue the investigation? (y/n): ")
                print(" ")

                if d2 =="y":
                    print("You suit up. It's time to head over to Gordon's location. You look over and see the new utility belt you created. ")

                    print(" ")
                    d3 = input("Do you equip it instead of the one you have now? (y/n): ")
                    print(" ")

                    if d3 =="y":
                        inventory[0] = "Smoke Bomb"
                        p.attackpotency += 5
                    elif d3 =="n":
                        print("You proceed without your new utility belt.")

                    ### CHAPTER 2: GOTHAM CITY ###

                    current_location = location['Gotham City']
                    print("You are now in " + (current_location['name']))
                    print("You have reached the scene of the crime. In front of you lies two bodies. As you inspect the bodies you notice that the victims are pale white, with a crooked smile on their face reminiscent of the Joker. ")
                    print("You get chills down your spine at the sight. It's time to investigate further.")

                    completion = False

                    while completion == False:

                        print(" ")
                        d4 = input("What do you want to investigate? (jacket/shoes): ")
                        print(" ")

                        if d4 =="jacket":
                            print("You notice the tip of a playing card poking out of one of the victim's suit pockets. Typical. The Joker card... but this one seems to have a small hole in it. ")
                            print("It appears to have been burned by a drop of acid? This must mean one thing... You take the card.")
                            p.clues += 1
                            inventory[1] = "Joker Playing Card"

                            print(" ")
                            d5 = input("Do you wish to return to the crime scene? (y/n): ")
                            print(" ")

                        elif d4 =="shoes":
                            print("You notice small pieces of shattered glass on the shoes of the victims. Upon closer inspection you see green residue. Could this be from smoke or coloring? Maybe you should gather some more information.")
                            print(" ")
                            d5 = input("Do you wish to return to the crime scene? (y/n): ")
                            print(" ")
                        else:
                            continue

                        if d5 == "n" and p.clues >= 1:
                            break
                        elif d5 == "y":
                            continue
                        elif d5 == "n" and p.clues < 1:
                            print("You do not have what you need to find the attackers.")
                            continue
                        else:
                            continue

                    ### CHAPTER 3: ACE CHEMICALS ###

                    current_location = location['Ace Chemicals']
                    print("You are now in " + (current_location['name']))
                    print("There's only one place in Gotham where these goons could have come from. Ace Chemicals.")
                    print ("Not only is it the only acidic plant in the city, but it's where Harley and Joker first dedicated their lives to crime. It only makes sense that she would hold her base of operations here.")
                    print('"Hey! Is that Batman? Get him!"')
                    print("You turn around and see three henchman running at you.")
                    print(" ")

                    completion2 = False

                    while completion2 == False:
                        d6 = input("What do you do? (attack/run): ")

                        if d6 == "attack" and p.attackpotency >= h.health:
                            print(" ")
                            print("BAM! POW! BOOM!")
                            print("Just like that, you took out all three! Good thing you brought your new utility belt. It really gave you the upper hand here.")
                            print('"Tell me where Harley is or I will break every bone in your body one by one." you say to the only conscious henchman.')
                            print('"WAIT WAIT WAIT. I WILL TELL YOU" he pleads. "All I know is that they keep the joker toxin at the clocktower! I swear!"')
                            break
                        elif d6 == "attack" and p.attackpotency < h.health:
                            print("You weren't strong enough. If only you had the gear needed to beat them. You barely escaped with your life and had to retreat to the Batcave.")
                            Fail()
                            main()
                        elif d6 == "run":
                            print("You were able to run, however running won't help you stop Harley. You hide in the shadows, confusing the henchmen. While they are lost in their confusion you have an opening to strike from the shadows.")
                            continue

                    print("That should be all of the information you need. You could knock him out and chase down Harley or see if there's anything else he may know.")

                    print(" ")
                    d7 = input("What will you do? (knockout/interrogate): ")
                    print(" ")

                    if d7 == "knockout":
                        print("You knock the henchman out and throw him to the floor. It's time to face Harley.")
                    if d7 == "interrogate":
                        print('You interrogate him one last time and out of fear he reveals that this "joker toxin" has an antitode. You take it from his pocket and go off to face Harley.')
                        inventory[2] = "Antidote"
                        p.attackpotency += 5

                    ### CHAPTER 4: CLOCKTOWER ###

                    current_location = location['Clocktower']
                    print("You are now in " + (current_location['name']))

                    print("After sneaking your way into the tower you see Harley Quinn standing on a stage talking to a large group of henchmen...")
                    print('"The time has come boys! Mr. Js toxin is finished! Sadly two poor bozos had to give it a taste before we finished it, but now Gotham will pay for what they did to Mr. J!"')
                    print("This doesn't look good. Harley has managed to perfect Joker's toxin. You had been following a lead on this toxin back before the disappearance of the Joker.")
                    print(" ")
                    print('"Hey! Is that Batman???"')
                    print (" ")
                    print("You've been detected! You turn around a see a henchman watching the ceiling and pointing. They knew you were coming... They must have had someone watching the crime scene from a distance.")
                    print("You can't just outrun this one...")
                    print(" ")
                    print("Inventory")
                    print("----------------------")
                    for i in inventory:
                        print(i)

                    print(" ")
                    d8 = input("Quick! Which item can you use to get out of this situation? ")
                    if d8 == "Smoke Bomb":
                        del inventory[0]
                        print(" ")
                        print("You used the smoke bomb to conceal your next move and grappled across the clocktower.")
                        print("In the heat of the moment you activated your infrared vision and took out the henchmen.")
                        print("Suddenly, the smoke clears. You begin to see Harley on stage with a man... wait... is that the Joker??? But you thought he was dead???")
                        print("In your confusion a green gas starts to emerge from the vents on the floor.")

                        print("*** Harley and the Joker appear with gas masks on ***")
                        print('"Hey Bats! Let me know how the J toxin tastes! Well, I give ya 60 seconds before you lose the ability to talk... permanently!"')
                        print(" ")
                        print("Inventory")
                        print("----------------------")
                        for i in inventory:
                            print(i)
                        d9 = input("Quick! Which item can you use to get out of this situation? ")
                        if d9 == "Antidote":
                            del inventory[1]
                            print("You use the antidote and inject it quickly. The pain fades away and you look up to see the blurry outline of the Joker starting to... change shape?")
                            print("You suddenly realize that this whole time... it wasn't the Joker... it was... CLAYFACE!")
                            print("As Clayface begins to take his form you realize that you have an opening to strike while they think you're down.")

                            print(" ")
                            d10 = input("What will you do? (attack/run): ")

                            if d10 == "attack" and p.attackpotency >= b.health:
                                print("You were able to defeat Clayface and knock out Harley Quinn")
                                print("After taking Harley back to Arkham Asylum you return to the Batcave. It's finally time to close the case.")
                                print("With the Joker toxin being disposed of by the GCPD and Harley and Clayface back at Arkham Asylum, the only mystery remains... Is the joker really dead?")
                                print("Inventory")
                                print("----------------------")
                                for i in inventory:
                                    print(i)
                                    print(" ")

                                d11 = input("Select an item to use: ")
                                print(" ")

                                if d11 == "Joker Playing Card":
                                    print(" ")
                                    print("You put the card in the Joker's Case file. It's closed... for now...")
                                    print(" - The End - ")
                                    print("Gotham is safe for another night.")
                                    print(" ")
                                    main()
                                else:
                                    print(" ")
                                    print(" - The End - ")
                                    print(" ")
                                    main()

                            elif d10 == "run":
                                print("You ran, barely escaping with your life. You retreat to the batcave and start to drift away...")
                                Fail()
                                main()

                        else:
                            print("You failed to stop the fear toxin from spreading through your body. You lie down out of weakness and look up at the cieling...")
                            print("A smile on your face... You laugh. What's so funny? You failed. There's nothing funny about that, but you can't stop yourself")
                            print("as the world fades to black")
                            print(" - The End - ")
                            print("Try again to reach a much more heroic ending!")
                            main()

                    elif d8 == "Joker Playing Card":
                        print("The Joker Playing Card had no use. You tried to fight off the henchmen but barely escaped with your life.")
                        Fail()
                        main()
                    elif d8 == "Antidote":
                        print("The Antitode had no use. You tried to fight off the henchmen but barely escaped with your life.")
                        Fail()
                        main()

                elif d2 =="n":
                        print("You decide to handle this situation later.")
                        Fail()
                        main()

            elif d1 == 'n':
                print("You continue to review the case file... Studying... What could she be planning? Your eyes slowly begin to close.")
                Fail()
                main()

        elif STARTGAME == '2':
            print('Gotham is waiting for the Dark Knight.')
            break

        else:
            print('Please enter a valid response!')

if __name__ == "__main__":
    main()