import random;
import getpass;
def player1():
    player1 = getpass.getpass("Player 1 enter your choice (rock/paper/scissors/lizard/spock): ");
    player1 = player1.lower();
    while (player1 != "rock" and player1 != "paper" and player1 != "scissors"and player1 != "lizard" and player1 != "spock"):
        player1 = getpass.getpass("That choice is not valid. Enter your choice (rock/paper/scissors/lizard/spock): ");
        player1 = player1.lower();
    return player1    
def player2():
    player2 = getpass.getpass("Player 2 enter your choice (rock/paper/scissors/lizard/spock): ");
    player2 = player2.lower();
    while (player2 != "rock" and player2 != "paper" and player2 != "scissors" and player2 != "lizard" and player2 != "spock"):
        player2 = getpass.getpass("That choice is not valid. Enter your choice (rock/paper/scissors/lizard/spock): ");
        player2 = player2.lower();
    return player2
def computer():
    computerInt = random.randint(0,4);
    if (computerInt == 0):
        computer = "rock";
    elif (computerInt == 1):
        computer = "paper";
    elif (computerInt == 2):
        computer = "scissors";
    elif (computerInt == 3):
        computer = "lizard";
    elif (computerInt == 4):
        computer = "spock";
    else:
        computer = "Huh? Error...";
    return (computer)
def winner(player1,player2):
    if (player1 == player2):
        return("Draw!");
    elif (player1 == "rock"):
        if (player2 == "lizard" or "scissors"):
            return("player 1 wins!");
        else:
            return("player 2 win!");
    elif (player1 == "paper"):
        if (player2 == "rock" or "spock"):
            return("player 1 win!");
        else:
            return("player 2 wins!")
    elif (player1 == "scissors"):
        if (player2 == "paper" or "lizard"):
            return("player 1 wins!");
        else:
            return("player 2 win!");
    elif (player1 == "lizard"):
        if (player2 == "spock" or "paper"):
            return("player 1 wins!");
        else:
            return("player 2 win!");
    elif (player1 == "spock"):
        if (player2 == "paper" or "lizard"):
            return("player 1 wins!");
        else:
            return("player 2 win!");
def runGame():
    opponent=input('play against the computer y/n?')
    inputPlayer1=str(player1())
    if opponent=='n':
        inputPlayer2=str(player2())
    elif opponent=='y':
        inputPlayer2=str(computer())
    whoWins=winner(inputPlayer1,inputPlayer2)
    print('player 1 chooses: '+inputPlayer1)
    print('player 2 chooses: '+inputPlayer2)
    print (whoWins)
    playAgain=input('play again y/n?: ')
    if playAgain=='y':
        return (runGame())
(runGame())
