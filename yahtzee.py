import random

dice = { 1 : "⚀",
         2 : "⚁",
         3 : "⚂",
         4 : "⚃",
         5 : "⚄",
         6 : "⚅"
         }

cup = [0,0,0,0,0]
held = [False,False,False,False,False]
aTurn = True # This is just a way of saying if it's A players turn then it's True if it's B players turn it's False
scoreAmount = 0 # Increments every time a player scores. If it reaches 26 that means the player B has done the last turn
rolls = 0 # After it reaches 3 it's going to prevent the player from rolling
sheetA = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1] # Player A sheet values. -1 means empty
sheetB = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1] # Player B sheet values. -1 means empty

# rolling the dice
def rollDice():
    flag = False
    if not all(held):
        for index in range(5):
            if held[index] == False:
                cup[index] = random.randint(1,6)
        displayDice()
        flag = True
    return flag

# Displaying the dice
def displayDice():
    for index in range (5):
        if held[index] == False:
            print('{0}:{1} '.format(index+1, dice.get(cup[index])), end="")
        else:
            print('{0}>{1} '.format(index+1, dice.get(cup[index])), end="")
    print()

# Holds the die
def holdDie(index):
    flag = False
    if index > 0 and index < 6:
        held[index - 1] = True
        flag = True
        displayDice()
    return flag

# Releases the die
def releaseDie(index):
    flag = False
    if index > 0 and index < 6:
        held[index - 1] = False
        flag = True
        displayDice()
    return flag

def help():
    print("Sheet - displaying a player's full score sheet\nScore (1-13) - selecting a spot to score the current dice\nRoll - rolling all free dice\nHold (1-5) - a method of holding / keeping dice not to be rolled\nRelease (1-5) - a method of releasing dice so they can be rolled")

def totalScore(playerA):
    scoreSum = 0
    if playerA:
        for value in sheetA:
            scoreSum += value
    else:
        for value in sheetB:
            scoreSum += value
    return scoreSum
    
def displaySheet():
    if aTurn:
        print("Player A\nOnes: {}\nTwos: {}\nThrees: {}\nFours: {}\nFives: {}\nSixes: {}\nThree of a kind: {}\nFour of a kind: {}\nFull house: {}\nSmall straight: {}\nLarge straight: {}\nChance: {}\nYAHTZEE: {}\nTOTAL SCORE: ".format(sheetA[0] if sheetA[0] > -1 else "", sheetA[1] if sheetA[1] > -1 else "", sheetA[2] if sheetA[2] > -1 else "", sheetA[3] if sheetA[3] > -1 else "", sheetA[4] if sheetA[4] > -1 else "", sheetA[5] if sheetA[5] > -1 else "", sheetA[6] if sheetA[6] > -1 else "", sheetA[7] if sheetA[7] > -1 else "", sheetA[8] if sheetA[8] > -1 else "", sheetA[9] if sheetA[9] > -1 else "", sheetA[10] if sheetA[10] > -1 else "", sheetA[11] if sheetA[11] > -1 else "", sheetA[12] if sheetA[12] > -1 else ""))
    else:
        print("Player B\nOnes: {}\nTwos: {}\nThrees: {}\nFours: {}\nFives: {}\nSixes: {}\nThree of a kind: {}\nFour of a kind: {}\nFull house: {}\nSmall straight: {}\nLarge straight: {}\nChance: {}\nYAHTZEE: {}\nTOTAL SCORE: ".format(sheetB[0] if sheetB[0] > -1 else "", sheetB[1] if sheetB[1] > -1 else "", sheetB[2] if sheetB[2] > -1 else "", sheetB[3] if sheetB[3] > -1 else "", sheetB[4] if sheetB[4] > -1 else "", sheetB[5] if sheetB[5] > -1 else "", sheetB[6] if sheetB[6] > -1 else "", sheetB[7] if sheetB[7] > -1 else "", sheetB[8] if sheetB[8] > -1 else "", sheetB[9] if sheetB[9] > -1 else "", sheetB[10] if sheetB[10] > -1 else "", sheetB[11] if sheetB[11] > -1 else "", sheetB[12] if sheetB[12] > -1 else ""))
    

def displayEndSheet(playerA):
    if playerA:
        print("Player A\nOnes: {}\nTwos: {}\nThrees: {}\nFours: {}\nFives: {}\nSixes: {}\nThree of a kind: {}\nFour of a kind: {}\nFull house: {}\nSmall straight: {}\nLarge straight: {}\nChance: {}\nYAHTZEE: {}\nTOTAL SCORE: {}".format(sheetA[0], sheetA[1], sheetA[2], sheetA[3], sheetA[4], sheetA[5], sheetA[6], sheetA[7], sheetA[8], sheetA[9], sheetA[10], sheetA[11], sheetA[12], totalScore(playerA)))
    else:
        print("Player B\nOnes: {}\nTwos: {}\nThrees: {}\nFours: {}\nFives: {}\nSixes: {}\nThree of a kind: {}\nFour of a kind: {}\nFull house: {}\nSmall straight: {}\nLarge straight: {}\nChance: {}\nYAHTZEE: {}\nTOTAL SCORE: {}".format(sheetB[0], sheetB[1], sheetB[2], sheetB[3], sheetB[4], sheetB[5], sheetB[6], sheetB[7], sheetB[8], sheetB[9], sheetB[10], sheetB[11], sheetB[12], totalScore(playerA)))

def scoreCalculator(index):
    total = 0
    foundOption = False

    repeatingCount = [0, 0, 0, 0, 0, 0] # 6 faces of a die. The amount of times 1 face was repeated from in the cup
    for die in cup:
        repeatingCount[die - 1] += 1

    if index < 6: # Ones, Twos, Threes, Fours, Fives, Sixes
        for die in cup:
            if die == index + 1:
                total += die
                foundOption = True
        if foundOption:
            return total
        else:
            return -1
    elif index == 6: # Three of a kind
        for face in repeatingCount:
            if face >= 3:
                return sum(cup)
        return -1
    elif index == 7: # Four of a kind
        for face in repeatingCount:
            if face >= 4:
                return sum(cup)
        return -1
    elif index == 8: # Full house
        threeRepeating = False
        twoRepeating = False
        for face in repeatingCount:
            if face == 2:
                twoRepeating = True
            elif face == 3:
                threeRepeating = True
        if threeRepeating and twoRepeating:
            return 25
        else:
            return -1
    elif index == 9: # Small straight
        straightCounter = 0
        for face in repeatingCount:
            if face > 0:
                straightCounter += 1
            else:
                straightCounter = 0

            if straightCounter >= 4:
                return 30
        return -1
    elif index == 10: # Large straight
        straightCounter = 0
        for face in repeatingCount:
            if face > 0:
                straightCounter += 1
            else:
                straightCounter = 0

            if straightCounter == 5:
                return 40
        return -1
    elif index == 11: # Chance
        return sum(cup)
    elif index == 12: # YAHTZEE
        for face in repeatingCount:
            if face == 5:
                return 50
        return -1

def score(index):
    index -= 1
    flag = False

    if aTurn:
        if sheetA[index] == -1:
            calculatedScore = scoreCalculator(index)
            if not calculatedScore == -1:
                sheetA[index] = calculatedScore
                flag = True
            else:
                if all(sheetA[i] != -1 or scoreCalculator(i) == -1 for i in range(13)):
                    sheetA[index] = 0
                    flag = True
                else:
                    print("You can't score there!")
        else:
            print("Location already scored! Choose another!")
    else:
        if sheetB[index] == -1:
            calculatedScore = scoreCalculator(index)
            if not calculatedScore == -1:
                sheetB[index] = calculatedScore
                flag = True
            else:
                if all(sheetB[i] != -1 or scoreCalculator(i) == -1 for i in range(13)):
                    sheetB[index] = 0
                    flag = True
                else:
                    print("You can't score there!")
        else:
            print("Location already scored! Choose another!")
            
    return flag

print("Welcome to Yahtzee. Use the command 'help' to show a list of commands.")

while scoreAmount < 26:
    if aTurn:
        print()
        command = input("Player A turn: ").lower()

        if command == "sheet":
            displaySheet()
        elif command == "score":
            if rolls > 0:
                displaySheet()
                location = input("Enter the location you want to score (1-13): ")
                if location.isdigit():
                    index = int(location)
                    if index > 0 and index < 14:
                        if score(index):
                            rolls = 0
                            scoreAmount += 1
                            aTurn = False
                            held = [False,False,False,False,False]
                    else:
                        print("Invalid input! Enter a number between 1-13! Try again!")
                else:
                    print("Invalid input! Enter a number between 1-13! Try again!")
            else:
                print("You can't score before rolling for the first time!")
        elif command == "roll":
            if rolls < 3:
                if rollDice():
                    rolls += 1
                else:
                    print("All dies are held!")
            else:
                print("You've rolled 3 times already. Choose a spot you want to score!")
        elif command == "hold":
            if rolls > 0:
                displayDice()
                die = input("Choose the die you want to hold: ")
                if die.isdigit():
                    index = int(die)
                    if holdDie(index):
                        print("Die {} is held".format(index))
                    else:
                        print("Invalid input! Enter a number between 1-5! Try again!")
                else:
                    print("Invalid input! Enter a number between 1-5! Try again!")
            else:
                print("You can't hold before rolling for the first time!")
        elif command == "release":
            if rolls > 0:
                displayDice()
                die = input("Choose the die you want to release: ")
                if die.isdigit():
                    index = int(die)
                    if releaseDie(index):
                        print("Die {} is released".format(index))
                    else:
                        print("Invalid input! Enter a number between 1-5! Try again!")
                else:
                    print("Invalid input! Enter a number between 1-5! Try again!")
            else:
                print("You can't release before rolling for the first time!")
        elif command == "help":
            help()
        else:
            print("Invalid command! Type 'help' for a list of commands!")
    else:
        print()
        command = input("Player B turn: ").lower()

        if command == "sheet":
            displaySheet()
        elif command == "score":
            if rolls > 0:
                displaySheet()
                location = input("Enter the location you want to score (1-13): ")
                if location.isdigit():
                    index = int(location)
                    if index > 0 and index < 14:
                        if score(index):
                            rolls = 0
                            scoreAmount += 1
                            aTurn = True
                            held = [False,False,False,False,False]
                    else:
                        print("Invalid input! Enter a number between 1-13! Try again!")
                else:
                    print("Invalid input! Enter a number between 1-13! Try again!")
            else:
                print("You can't score before rolling for the first time!")
        elif command == "roll":
            if rolls < 3:
                if rollDice():
                    rolls += 1
                else:
                    print("All dies are held!")
            else:
                print("You've rolled 3 times already. Choose a spot you want to score!")
        elif command == "hold":
            if rolls > 0:
                displayDice()
                die = input("Choose the die you want to hold: ")
                if die.isdigit():
                    index = int(die)
                    if holdDie(index):
                        print("Die {} is held".format(index))
                    else:
                        print("Invalid input! Enter a number between 1-5! Try again!")
                else:
                    print("Invalid input! Enter a number between 1-5! Try again!")
            else:
                print("You can't hold before rolling for the first time!")
        elif command == "release":
            if rolls > 0:
                displayDice()
                die = input("Choose the die you want to release: ")
                if die.isdigit():
                    index = int(die)
                    if releaseDie(index):
                        print("Die {} is released".format(index))
                    else:
                        print("Invalid input! Enter a number between 1-5! Try again!")
                else:
                    print("Invalid input! Enter a number between 1-5! Try again!")
            else:
                print("You can't release before rolling for the first time!")
        elif command == "help":
            help()
        else:
            print("Invalid command! Type 'help' for a list of commands!")

displayEndSheet(True)
displayEndSheet(False)
print("Thanks for playing!")