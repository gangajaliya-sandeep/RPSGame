# Import random module for random selection for computer
import random

print("\033[1;36mWelcome to Rock Paper Scissor Game\033[0m")

# These objects will hold winning, lose and tie count
winCount = loseCount = tieCount = 0.0


# Take User's choice as input
def playerChoice():

    try:
        # Take choice from user as input
        userChoice = int(
            input("Select your choice => 0: Rock, 1: Paper, 2: Scissor, 5: Exit => "))

        # Validate User's choice
        if (validateUserInput(userChoice)):
            return userChoice
        else:
            playerChoice()

    except ValueError:
        # Throw error if selected wrong option
        print("Please enter an number \n")


# Validate User's choice
def validateUserInput(userChoice):

    # Compare User's choice
    if ((userChoice <= 2 and userChoice >= 0) or userChoice == 5):
        return True
    else:
        # Wrong choice from user, try again
        print(
            "\nPlease enter an integer less than 3 and greater than or equalt to 0 or 5 to exit. \n")
        return False


# Function to play game
def playGame():

    # Choices is a static array
    choices = ["Rock", "Paper", "Scissor"]

    # This object will decide to play again or exit from game
    playContinue = True

    # Play continue
    while (playContinue):

        # User choice
        userChoice = playerChoice()

        # Computer choice with random between 0 to 2
        computerChoice = random.randint(0, 2)

        # Check user choice if valid or not
        if (userChoice <= 2 and userChoice >= 0):

            result = checkResult(userChoice, computerChoice)
            print("Your choice is %s" % choices[userChoice])
            print("The computer choose %s" % choices[computerChoice])
            print("You %s" % result)

        elif (userChoice == 5):
            # User choose to exit from game
            playContinue = False


# Compare choice and decide result
def checkResult(user, computer):
    win = False
    tie = False
    if (user == 0):
        if (computer == 0):
            tie = True
        elif (computer == 1):
            win = False
            tie = False
        elif (computer == 2):
            win = True
            tie = False

    elif (user == 1):
        if (computer == 0):
            win = True
            tie = False
        elif (computer == 1):
            tie = True
        elif (computer == 2):
            win = False
            tie = False

    else:
        if (computer == 0):
            win = False
            tie = False
        elif (computer == 1):
            win = True
            tie = False
        elif (computer == 2):
            tie = True

    if (tie == True):
        countStats(2)
        return "Tied!"
    elif (win):
        countStats(0)
        return "Win!"
    else:
        countStats(1)
        return "Lose!"


# Caluculate and set win, lose and tie count
def countStats(result):
    global winCount
    global loseCount
    global tieCount

    if (result == 0):
        winCount += 1
    elif (result == 1):
        loseCount += 1
    else:
        tieCount += 1


# Announce results
def finaliseResult():

    # Get global object
    global winCount, loseCount, tieCount
    print("These are your final result: ")

    # Calculate winning percentage
    if (winCount+loseCount+tieCount != 0):
        winningPercentage = "{percent:.2%}".format(
            percent=(winCount / (winCount+loseCount)))
    else:
        winningPercentage = "{percent:.2%}".format(percent=0)

    # Pring final result
    print("You won %d game(s), you lose %d game(s) and %d tied game(s)!" %
          (winCount, loseCount, tieCount))
    print("You have a %s winning percentage" % winningPercentage)


# This function will call at very first time
def main():

    # playGameAgain will be used to play game again
    playGameAgain = True

    # quitGameYesOrNo will be used to exit from game
    quitGameYesOrNo = True

    while (playGameAgain):

        quitGameYesOrNo = True
        playGameAgain = False
        playGame()

        while (quitGameYesOrNo):

            # Take input from user to exit from game
            continueGame = input(
                "Would you like to play again? Type Yes or No \n")

            if (continueGame.lower() == "yes"):

                # Continue to play game
                print("Starting Rock Paper Scissor game again \n")
                quitGameYesOrNo = False
                playGameAgain = True

            elif (continueGame.lower() == "no"):

                # Exit from game and display final result
                finaliseResult()
                quitGameYesOrNo = False
                playGameAgain = False

            else:

                # Wrong input from user
                print("Please type Yes or No")
                quitGameYesOrNo = True


main()
