import random
import time


# create cards for the game
class GameCard:
    def __init__(self, CarName, TopSpeed, Power, Gear, Torque, Cylinders, WheelBase):
        self.CarName = CarName
        self.TopSpeed = TopSpeed
        self.Power = Power
        self.Gear = Gear
        self.Torque = Torque
        self.Cylinders = Cylinders
        self.WheelBase = WheelBase


CardDeck = []
CardDeck.append(GameCard("BMW_M3", 280, 460, 7, 600, 6, 2812))
CardDeck.append(GameCard("Audi_A8", 250, 340, 8, 500, 4, 2998))
CardDeck.append(GameCard("Jaguar_XJ", 300, 575, 8, 700, 4, 3157))
CardDeck.append(GameCard("Tesla_ModelS", 255, 539, 1, 967, 0, 2959))
CardDeck.append(GameCard("Volkswagen_Passat", 234, 240, 7, 500, 4, 2789))
CardDeck.append(GameCard("Mercedes_Benz_SLC", 250, 367, 9, 520, 6, 2778))

random.shuffle(CardDeck)

PlayerCardDeck = []
ComputerCardDeck = []
OutdatedCardDeck = []

# Deal the cards
while len(CardDeck) > 0:
    PlayerCardDeck.append(CardDeck.pop(0))
    ComputerCardDeck.append(CardDeck.pop(0))
# rolling dices
print("Card game Player1 vs Player2!")
game_start = input("Do you want to roll the dice? ")

def dice_roll():
    Dice1 = random.randint(1, 6)
    Dice2 = random.randint(1, 6)
    global playerTurn
    print("Player1 dice is: " + str(Dice1))
    print("Player2 dice is: " + str(Dice2))
    if Dice1 > Dice2:
        print("Player1 first!")
        playerTurn = True
    elif Dice1 < Dice2:
        print("Player2 first!")
        playerTurn = False
    else:
        print("It's a tie. Need to roll again!")
        dice_roll()


if game_start == "yes":
    dice_roll()
elif game_start == "no":
    print("Please input yes to proceed")
else:
    print("Please enter proper input")

playerTurn = True
KeyInput = ["a", "b", "c", "d", "e", "f"]
GodSpellCountPlayer = 0
GodSpellCountCom = 0
ResurrectSpellCountPlayer = 0
ResurrectSpellCountComputer = 0
Player_1 = 0
Player_2 = 0
ResurrectSpell = "no"
ResurrectSpell1 = "no"

while len(PlayerCardDeck) > 0 and len(ComputerCardDeck) > 0:
    time.sleep(1)

    if playerTurn == True:
        # player1 resurrect spell
        ra = 0
        if (ResurrectSpellCountPlayer == 0 and len(OutdatedCardDeck) > 1 and ra == 0):
            ResurrectSpell = input("Player1, do you want to use Resurrect Spell? yes or no: ")
            if (ResurrectSpell == "yes" and ResurrectSpellCountPlayer == 0):
                z1 = random.randint(1, len(OutdatedCardDeck))
                playerCard = OutdatedCardDeck.pop(int(z1) - 1)
                OutdatedCardDeck.append(playerCard)
                ResurrectSpellCountPlayer = 1
                ra = 1
            else:
                playerCard = PlayerCardDeck.pop(0)
                OutdatedCardDeck.append(playerCard)
        else:
            playerCard = PlayerCardDeck.pop(0)
            OutdatedCardDeck.append(playerCard)

        print("PLAYER1 CARD")
        print("Car Name:", playerCard.CarName)
        print("a. Top Speed:", playerCard.TopSpeed)
        print("b. Power:", playerCard.Power)
        print("c. Gear:", playerCard.Gear)
        print("d. Torque:", playerCard.Torque)
        print("e. Cylinders:", playerCard.Cylinders)
        print("f. Wheel Base:", playerCard.WheelBase)
        answer = input("Player1, which specification do you choose? ")

        while KeyInput.count(answer) == 0:
            answer = input("Invalid, please try again: ")
        # player1 god spell
        if (GodSpellCountPlayer == 0 and len(ComputerCardDeck) > 1 and ra == 0):
            gspell = input("Player1, do you want to use God Spell? yes or no: ")
            if (gspell == "yes" and GodSpellCountPlayer == 0):
                GodSpellCountPlayer = 1
                lec = len(ComputerCardDeck)
                print("No of cards in Player2 deck:", lec)
                cardno = input("Which card number from Player2 deck? ")
                if (ResurrectSpellCountComputer == 0 and len(OutdatedCardDeck) > 1):
                    ResurrectSpell1 = input("Player2, do you want to use Resurrect Spell? yes or no: ")
                    if (ResurrectSpell1 == "yes" and ResurrectSpellCountComputer == 0):
                        z2 = random.randint(1, len(OutdatedCardDeck))
                        mn = OutdatedCardDeck.pop(int(z2) - 1)
                        ComputerCardDeck.insert(0, mn)
                        choice = input("Player1: a. Use resurrected card or b. Select Previous choice ")
                        if (choice == "a"):
                            computerCard = ComputerCardDeck.pop(0)
                            OutdatedCardDeck.append(computerCard)
                            ResurrectSpellCountComputer = 1
                        else:
                            computerCard = ComputerCardDeck.pop(int(cardno) - 1)
                            OutdatedCardDeck.append(computerCard)
                            ResurrectSpellCountComputer = 1
                    else:
                        computerCard = ComputerCardDeck.pop(int(cardno) - 1)
                        OutdatedCardDeck.append(computerCard)
                else:
                    computerCard = ComputerCardDeck.pop(int(cardno) - 1)
                    OutdatedCardDeck.append(computerCard)

            else:
                computerCard = ComputerCardDeck.pop(0)
                OutdatedCardDeck.append(computerCard)


        else:
            computerCard = ComputerCardDeck.pop(0)
            OutdatedCardDeck.append(computerCard)

        print("PLAYER2 CARD")
        print("Car Name:", computerCard.CarName)
        print("a. Top Speed:", computerCard.TopSpeed)
        print("b. Power:", computerCard.Power)
        print("c. Gear:", computerCard.Gear)
        print("d. Torque:", computerCard.Torque)
        print("e. Cylinders:", computerCard.Cylinders)
        print("f. Wheel Base:", computerCard.WheelBase)


    else:
        # player2 resurrect spell
        rb = 0
        if (ResurrectSpellCountComputer == 0 and len(OutdatedCardDeck) > 1 and rb == 0):
            ResurrectSpell1 = input("Player2, do you want to use Resurrect Spell? yes or no: ")
            if (ResurrectSpell1 == "yes" and ResurrectSpellCountComputer == 0):
                z2 = random.randint(1, len(OutdatedCardDeck))
                computerCard = OutdatedCardDeck.pop(int(z2) - 1)
                OutdatedCardDeck.append(computerCard)
                ResurrectSpellCountComputer = 1
                rb = 1
            else:
                computerCard = ComputerCardDeck.pop(0)
                OutdatedCardDeck.append(computerCard)

        else:
            computerCard = ComputerCardDeck.pop(0)
            OutdatedCardDeck.append(computerCard)

        print("PLAYER2 CARD")
        print("Car Name:", computerCard.CarName)
        print("a. Top Speed:", computerCard.TopSpeed)
        print("b. Power:", computerCard.Power)
        print("c. Gear:", computerCard.Gear)
        print("d. Torque:", computerCard.Torque)
        print("e. Cylinders:", computerCard.Cylinders)
        print("f. Wheel Base:", computerCard.WheelBase)

        answer = input("Player2, which specification do you choose? ")
        print("Player2 chooses", answer)

        # Player2 god spell
        if (GodSpellCountCom == 0 and len(PlayerCardDeck) > 1 and rb == 0):
            gspell1 = input("Player2, do you want to use God Spell? yes or no: ")
            if (gspell1 == "yes" and GodSpellCountCom == 0):
                GodSpellCountCom = 1
                lep = len(PlayerCardDeck)
                print("No of cards in Player1 deck:", lep)
                cardno1 = input("Which card number from Player1 deck? ")
                if (ResurrectSpellCountPlayer == 0 and len(OutdatedCardDeck) > 1):
                    ResurrectSpell = input("Player1, do you want to play Resurrect Spell? yes or no: ")
                    if (ResurrectSpell == "yes" and ResurrectSpellCountPlayer == 0):
                        z1 = random.randint(1, len(OutdatedCardDeck))
                        nm = OutdatedCardDeck.pop(int(z1) - 1)
                        PlayerCardDeck.insert(0, nm)
                        choice1 = input("Player2: a. Force resurrected card or b. Force earlier choice ")
                        if (choice1 == "a"):
                            playerCard = PlayerCardDeck.pop(0)
                            OutdatedCardDeck.append(playerCard)
                            ResurrectSpellCountPlayer = 1
                        else:
                            playerCard = PlayerCardDeck.pop(int(cardno1) - 1)
                            OutdatedCardDeck.append(playerCard)
                            ResurrectSpellCountPlayer = 1
                    else:
                        playerCard = PlayerCardDeck.pop(int(cardno1) - 1)
                        OutdatedCardDeck.append(playerCard)
                else:
                    playerCard = PlayerCardDeck.pop(int(cardno1) - 1)
                    OutdatedCardDeck.append(playerCard)
            else:
                playerCard = PlayerCardDeck.pop(0)
                OutdatedCardDeck.append(playerCard)


        else:
            playerCard = PlayerCardDeck.pop(0)
            OutdatedCardDeck.append(playerCard)

        print("PLAYER1 CARD")
        print("Car Name:", playerCard.CarName)
        print("a. Top Speed:", playerCard.TopSpeed)
        print("b. Power:", playerCard.Power)
        print("c. Gear:", playerCard.Gear)
        print("d. Torque:", playerCard.Torque)
        print("e. Cylinders:", playerCard.Cylinders)
        print("f. Wheel Base:", playerCard.WheelBase)

    playerWins = False
    # comparing cards of player1 and player2
    if answer == "a":
        playerWins = (playerCard.TopSpeed > computerCard.TopSpeed)
    elif answer == "b":
        playerWins = (playerCard.Power > computerCard.Power)
    elif answer == "c":
        playerWins = (playerCard.Gear > computerCard.Gear)
    elif answer == "d":
        playerWins = (playerCard.Torque > computerCard.Torque)
    elif answer == "e":
        playerWins = (playerCard.Cylinders > computerCard.Cylinders)
    elif answer == "f":
        playerWins = (playerCard.WheelBase < computerCard.WheelBase)

    time.sleep(1)

    # who wins the hand?
    if playerWins:
        print("Player1 wins this hand!")
        Player_1 = Player_1 + 1
        playerTurn = True
    else:
        print("Player2 wins this hand!")
        Player_2 = Player_2 + 1
        playerTurn = False

time.sleep(2)

# who wins the match?
if Player_1 < Player_2:
    print("PLAYER2 WINS THE MATCH!")
elif Player_1 > Player_2:
    print("PLAYER1 WINS THE MATCH!")
else:
    print("IT'S A TIE!")

time.sleep(2)

# total points of player1 and player2 in the match
print("Player1 total points: ", Player_1)
print("Player2 total points: ", Player_2)
print("Total cards in Outdated Deck: ", len(OutdatedCardDeck))