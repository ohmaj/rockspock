class result:
    def __init__(self,player1Choice,player2Choice):
        
        self.player1Choice=player1Choice
        self.player2Choice=player2Choice
    
    def calcResult():
        if self.player1Choice == self.player2Choice:
            self.output='Draw! '
        elif ((self.player1Choice - self.player2Choice)%5 == 1):
            self.output='Player 1 Wins! '
        else:
            self.output='Player 2 Wins! '
    