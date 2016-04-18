import random
class game:
    def __init__(self,name,player1,player2):
        self.name=name
        self.player1=player1
        self.player2=player2
    def getHumanChoice(self):
        playerChoice= input('enter # for choice 1:rock 2:paper 3:scissors 4:Spock 5:lizard: ')
        if int(playerChoice) in range(1,6):
            return (playerChoice)
        else:
            print('not a valid selection please choose again')
            return(self.getHumanChoice())
    def getComputerChoice(self):
        playerChoice=str(random.randint(1,5))
        return (playerChoice)
    def calcResult(self,player1Choice,player2Choice):
            print(self.player1.name+' chose: '+str(self.player1.choice))
            print(self.player2.name+' chose: '+str(self.player2.choice))
            if player1Choice == player2Choice:
                return('Draw! ')
            elif ((player1Choice - player2Choice)%5) in [1,3]:
                return('Player 1 Wins! ')
            else:
                return('Player 2 Wins! ')
    def getrResult(self):
        players=(self.player1,self.player2)
        for player in players:
            if player.isHuman == True:
                player.choice=self.getHumanChoice()
            elif player.isHuman == False:    
                player.choice=self.getComputerChoice()
        print(self.calcResult((int(self.player1.choice)),(int(self.player2.choice))))
   