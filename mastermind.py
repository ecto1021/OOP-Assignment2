import random
#from board import 


class Mastermind:
    gameMode = ['A', 'B', 'C', 'D']
    listOfPlayers = []

    def __init__(self):
        WelcomeString = input(
        '''
        Welcome to Mastermind! 
        Developed by Steven Harris
        COMP 1046 Object-Oriented Programming 
        Press Enter to Continue 
        ''')
        
    def player(self,name):
        self.name = name

    def play(self):
        players = []
        choseGameMode = str(input('''
                Select which game you want to play: 
                (A) Original Mastermind for 2 Players 
                (B) Original Mastermind for 1 Player 
                (C) Mastermind44 for 4 Players 
                *Enter A, B, or C to continue* 
                '''))

        if choseGameMode in ['A','a']:
           self.name = input("Player 1 please enter your name: ")
           self.listOfPlayers.append(self.name)
           self.name = input("Player 2 please enter your name: ")
           self.listOfPlayers.append(self.name)
        elif choseGameMode in ["B" ,"b"]:
            createName = input("Player 1 please enter your name: ")
            self.listOfPlayers.append(self.name)
        else:
            print("please restart the game")
            quit()
            

    def getPlayerName(self):
        return self.name









m = Mastermind()


m.play()
print(m.getPlayerName())
print(m.listOfPlayers)