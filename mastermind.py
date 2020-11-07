import random



class Mastermind:
    gameMode = ['A', 'B', 'C', 'D']
    listOfPlayers = []

    def __init__(self):
        #initialising class with a welcome message
        WelcomeString = input('''
        Welcome to Mastermind! 
        Developed by Steven Harris
        COMP 1046 Object-Oriented Programming 
        Press Enter to Continue ''')
        
    def player(self,name):
        self.name = name

    def setGameMode(self):
        pass 

    def play(self):
        playing = True
        while playing == True:
            choice = input("""
            What would you like to do?
            (P)lay the game
            (q)uit the game
            """)
            if choice in ["p","P"]:
                choseGameMode = str(input('''
                    Select which game you want to play: 
                    (A) Original Mastermind for 2 Players 
                    (B) Original Mastermind for 1 Player 
                    (C) Mastermind44 for 4 Players 
                    *Enter A, B, or C to continue* 
                        '''))    
                        
                if  choseGameMode  in ['A','a']:
                    counter = 1 
                    while counter < 3:
                        self.name = input("Player {counter} please enter your name: ".format(counter = counter))
                        counter += 1
                        self.listOfPlayers.append(self.name)
                    break

                elif  choseGameMode  in ["B" ,"b"]:
                    self.name = input("Please enter your name: ")
                    self.listOfPlayers.append(self.name)
                elif  choseGameMode  in ["C" ,"c"]:
                    counter = 1 
                    while counter < 5:
                        self.name = input("Player {counter} please enter your name: ".format(counter = counter))
                        counter += 1
                        self.id += 1
                        self.listOfPlayers.append(self.name)
                    break 
                else:
                    print("please restart the game")
                    quit()
            elif choice in ['Q','q']:
                quit()
                playing == False


    def getPlayerName(self):
        return self.name
        
        
        
    def showList(self):
        for i in self.listOfPlayers:
            print(i)









m = Mastermind()

m.play()
m.showList()
