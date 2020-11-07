import random

class Mastermind:
    """A class representing Mastermind
    ...
    Attributes:
    list of players that is used to store player names
    """
    gameMode = ['A', 'B', 'C', 'D']
    listOfPlayers = []

    def __init__(self):
        '''initialising class with a welcome message'''
        WelcomeString = input('''
        Welcome to Mastermind! 
        Developed by Steven Harris
        COMP 1046 Object-Oriented Programming 
        Press Enter to Continue ''')

    def play(self):
        """the main class to run, specified in assignment 2
        i used a while loop here to get the function to repeat if a 
        """
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
                    player1Name = input("Player 1 please enter your name: ")
                    player2Name = input("Player 2 please enter your name: ")
                    player1 = Player(player1Name)
                    player2 = Player(player2Name)
                    self.listOfPlayers.append(player1.name)
                    self.listOfPlayers.append(player2.name)
                    break
                elif  choseGameMode  in ["B" ,"b"]:
                    player1 = Player(input("Player 1 please enter your name: "))
                    self.listOfPlayers.append(player1.name)
                    break
                elif  choseGameMode  in ["C" ,"c"]:
                    player1Name = input("Player 1 please enter your name: ")
                    player2Name = input("Player 2 please enter your name: ")
                    player3Name = input("Player 3 please enter your name: ")
                    player4Name = input("Player 4 please enter your name: ")
                    player1 = Player(player1Name)
                    player2 = Player(player2Name)
                    player3 = Player(player3Name)
                    player4 = Player(player4Name)
                    self.listOfPlayers.append(player1.name)
                    self.listOfPlayers.append(player2.name)
                    self.listOfPlayers.append(player3.name)
                    self.listOfPlayers.append(player4.name)
                    break 
                else:
                    print("INVALID INPUT!")
                    print('Please choose from above option')
                    continue

            elif choice in ['Q','q']:
                print("You Have Chosen to Exit")
                quit()
                playing == False
            else:
                print('INVALID INPUT!')
                print('Please choose from above option')
                continue

    def getPlayerName(self,name):
        '''Function to return player name
        '''
        self.name = name
        return name
        
        
        
    def showList(self):
        "mehthod for showing elements in list "
        for i in self.listOfPlayers:
            print(i)
            

    def printList(self):
        '''method for printing entire list'''
        print(self.listOfPlayers)

class Player:
    """a class reprensenting a player
    this class is inherited when a player is created in the Mastermind game
    """
    def __init__(self, name):
        self.name = name




class board:
    '''A board class containing the board for the game

    Attributes
    
    Contains a list with colours to choose from
    
    '''
    masterCodeList = ["R","l","G","y","W","B","A"]

    def __init__(self):
        self.masterCodeList = masterCodeList 


    def generateMasterCode(self):
        for i in masterCodeList:
            print(random(i))














m = Mastermind()
#m.play()

b = board()

b.generateMasterCode




