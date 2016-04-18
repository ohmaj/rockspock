from player import player
from game import game


def main():
    print('Welcome to Rock, Paper, Scissors, Lizard, Spock')
    player1=player('Player 1')
    player2=player('Player 2')
    game1=game('Game 1',player1,player2)
    game2=game('Game 2',player1,player2)
    game3=game('Game 3',player1,player2)
    games=(game1,game2,game3)
    getPlayer2(player2)
    for gameInstance in games:
        game.getrResult(gameInstance)
    playAgain()
def playAgain():
    answer=input('Play again? y/n: ')
    if answer == 'y':
        return(main())
    elif answer == 'n':
        print('Thank You for Playing Rock, Paper, Scissors, Lizard, Spock')
    else:
        print ('not valid')
        return (playAgain())
def getPlayer2(player2): 
    isComputer=input('Play against the computer? (y/n): ')
    if isComputer=='y':
        print('You are playing aginast the computer')
        player2.isHuman=False
    elif isComputer=='n':
        print('You are not playing against the computer')
    else:
        print('not a valid selection please try again')
        return(player2())
if __name__ == "__main__":
    main()


    
