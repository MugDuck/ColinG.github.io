import random

from sqlalchemy import false

#beginning structure function

def main(): 

    #coin flip function

    coinLibrary = {1:"Heads",
    2 : "Tails"}
    print(f"This is a game of Tic Tac Toe.")
    turnChance = input(f"Heads or Tails? ")
    numChance = random.randint(1,2)
    turnRand = coinLibrary[numChance]

   # print(f"{numChance}")

    if turnChance == turnRand:
        print(f"It was {turnRand}! You go first!")
        playerTurn = "first"
        TicTacToe(playerTurn)
    elif turnChance != turnRand:
        print(f"Too bad! It was {turnRand} you go second.")
        playerTurn = "last"
        TicTacToe(playerTurn)
    else:
        print(f"Please type 'Heads' or 'Tails', please!")

#game function

def TicTacToe(firsecTurn):
 #the main problem is that each turn can choose over one another
    #player function
    def playerTurn(definition, turn):
        print("It is your turn!")
        playerTarget = int(input("Your number please: "))
        definition[playerTarget] = turn
        if definition[playerTarget] != "O" or "X":
            definition[playerTarget] = turn
            printGrid(definition)
        else:
            print("Pick a number that has not been chosen")
            playerTurn(definition, turn)

        #enemy function

    def enemyTurn(definition, turn):
        def randFunction():
            randAttack = int(random.randint(1,9))
            attack = randAttack
            return attack
        newNum = randFunction()
        definition[newNum] = turn
        if definition[newNum] != "O" or "X":
            print(f"Enemy has chosen {newNum}")
            definition[newNum] = turn
            printGrid(definition)
        else:
            print("facepalm")
            enemyTurn(definition, turn)
        
    #grid print system

    def printGrid(definition):
        print(f"{definition[1]}  /  {definition[2]}  /  {definition[3]}")
        print(f"{definition[4]}  /  {definition[5]}  /  {definition[6]}")
        print(f"{definition[7]}  /  {definition[8]}  /  {definition[9]}")

    #function to store values from game

    def TicTacToeGameplay(type):
        gameRounds = [1, 2, 3, 4]
        tictacGrid = {1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9"}
        if type == "first":
            playerValue = "X"
            enemyValue = "O"
            playerTurns = {0:playerValue, 1:playerValue, 2:playerValue, 3:playerValue, 4:playerValue}
            enemyTurns = {1:enemyValue, 2:enemyValue, 3:enemyValue, 4:enemyValue}
            printGrid(tictacGrid)
            playerTarget = int(input("Type the number you want to cross off: "))
            tictacGrid[playerTarget] = playerTurns[1]
            printGrid(tictacGrid)
            for i in gameRounds:
                turnCount =+ 1
                turnCountE =+ 1
                enemyTurn(tictacGrid, enemyTurns[turnCountE])
                playerTurn(tictacGrid,  playerTurns[turnCount])
                tictacWin(tictacGrid)
            
        else:
            playerValue = "O"
            enemyValue = "X"
            playerTurns = {1:playerValue, 2:playerValue, 3:playerValue, 4:playerValue}
            enemyTurns = {0:enemyValue, 1:enemyValue, 2:enemyValue, 3:enemyValue, 4:enemyValue, 5:enemyValue}
            randAttack = int(random.randint(1,9))
            print(f"Enemy chose {randAttack}!")
            tictacGrid[randAttack] = enemyTurns[1]
            printGrid(tictacGrid)
            for i in gameRounds:
                turnCount =+ 1
                turnCountE =+ 1
                playerTurn(tictacGrid,  playerTurns[turnCount])
                enemyTurn(tictacGrid, enemyTurns[turnCountE])
                tictacWin(tictacGrid)
            
        
    

#endgame function
    def tryAgain():
        choice = input("Again? y / n    ")
        if choice == "y":
            main()
        elif choice == "n":
            print("Have a nice day!")
            exit()
        else:
            print("please type y or n")
            tryAgain()
#basic winners code but no draw option
    def tictacWin(definition):            
        while definition[1] == "X" and definition[2] == "X" and definition[3] == "X":
            print("X's WIN!")
            tryAgain()
        while definition[1] == "O" and definition[2] == "O" and definition[3] == "O":  
            print("O's WIN!")
            tryAgain()
        while definition[4] == "X" and definition[5] == "X" and definition[6] == "X":
            print("X's WIN!")
            tryAgain()
        while definition[4] == "O" and definition[5] =="O" and definition[6] == "O":  
            print("O's WIN!")
            tryAgain()
        while definition[7] == "X" and definition[8] == "X" and definition[9] == "X":
            print("X's WIN!")
            tryAgain()
        while definition[7] == "O" and definition[8] =="O" and definition[9] == "O":  
            print("O's WIN!")
            tryAgain()
        while definition[1] == "X" and definition[4] == "X" and definition[7] == "X":
            print("X's WIN!")
            tryAgain()
        while definition[1] == "O" and definition[4] =="O" and definition[7] == "O":  
            print("O's WIN!")
            tryAgain()
        while definition[2] == "X" and definition[5] == "X" and definition[8] == "X":
            print("X's WIN!")
            tryAgain()
        while definition[2] == "O" and definition[5] =="O" and definition[8] == "O":  
            print("O's WIN!")
            tryAgain()
        while definition[3] == "X" and definition[6] == "X" and definition[9] == "X":
            print("X's WIN!")
            tryAgain()
        while definition[3] == "O" and definition[6] =="O" and definition[9] == "O":  
            print("O's WIN!")
            tryAgain()
        while definition[1] == "X" and definition[5] == "X" and definition[9] == "X":
            print("X's WIN!")
            tryAgain()
        while definition[1] == "O" and definition[5] =="O" and definition[9] == "O":  
            print("O's WIN!")
            tryAgain()
        while definition[3] == "X" and definition[5] == "X" and definition[7] == "X":
            print("X's WIN!")
            tryAgain()
        while definition[3] == "O" and definition[5] =="O" and definition[7] == "O":  
            print("O's WIN!")
            tryAgain()
        
        
        
    
        

            
#game start rules 
    
    if firsecTurn == "first":
        print("You are the X's")
        TicTacToeGameplay(firsecTurn)
        
        
    else :
        print("You are the O's")
        winBool = TicTacToeGameplay(firsecTurn)
        





main()
    
