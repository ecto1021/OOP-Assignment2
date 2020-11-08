import random

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
    masterCodelist = ["R","l","G","y","W","B","A"]

    def __init__(self):
        masterCodelist = []

       
    def generateMasterCode(self, numberOfPegs):
        '''a randomly generated code from the masterCodelist
        the random code is equal to the number of pegs
        '''
        empCode = []
        self.numberOfPegs = numberOfPegs
        empCode.append(random.sample(self.masterCodelist, self.numberOfPegs))
        return empCode



class row:
    player = Player
    attemptNumber = 0
    guessCodeList = []
    feedbackList = ["w", "R"]

    def __init__(self):
        self.player = Player
        self.attemptNumber
        self.guessCodeList
        self.feedbackList

    def checkAnswer(self,masterCodelist):
        '''Checks answer against guess code '''
        empBoard = board()
        self.masterCodelist = empBoard.masterCodelist
        guess = Mastermind.getGuessCode
        if(guess == self.masterCodelist):              
            print("Great! You guessed the number in just 1 try! You're a Mastermind!") 
        else: 
            # ctr variable initialized. It will keep count of  
            # the number of tries the Player takes to guess the number. 
            ctr = 0    


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
    
    def setGameMode(self):
        '''i used a while loop here to get the function to repeat if a '''
        playing = True
        while playing == True:
            choseGameMode = str(input('''
Select which game you want to play:
(A) Original Mastermind for 2 Players 
(B) Original Mastermind for 1 Player 
(C) Mastermind44 for 4 Players 
*Enter A, B, or C to continue* '''))    
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

    def play(self):

        """the main class to run, specified in assignment 2"""
        playing = True
        while playing == True:
            choice = input("""
What would you like to do ?
(P)lay
(Q)uit
""")
            if choice in ["p", 'p']:
                    self.setGameMode()
                    codeMaker.makeMasterCode(self)
                    row.checkAnswer(self,codeMaker.makeMasterCode)
                    playAgain = input("do you want to continue: y or n ?")
                    if playAgain in ['n','N']:
                        print("Thanks for playing! ")
                        playing == False
                    if playAgain in ['y','Y']:
                        playing == True
                        continue
            elif choice in['Q', "q"]:
                print("thanks for playing!")
                quit()
            break
        if playing == False:
           playAgain = input("do you want to continue")


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

    def getMasterCode(self,numberOfPegs):
        self.numberOfPegs = numberOfPegs
        b = board()
        b.generateMasterCode(numberOfPegs)
        return b.generateMasterCode(numberOfPegs)

    def getGuessCode(self,guess):
        self.guess = guess

class codeMaker:
    "Class that allows for creation of code"
    options = ['R','L','G','W','B']

    def __init__(self):
        self.options 

    def makeMasterCode(self):
        code1 = input("input code: ")
        codeToBeStored = input('Enter the same code Again ')
        if codeToBeStored == code1:
            row.guessCodeList.append(codeToBeStored)
        print(row.guessCodeList)




class originalMasterMind(Mastermind):
    withSupport = bool
    playerAttempts = 0
    numberOfPlayers = 0
    def __init__(self):
        WelcomeString = input('''
        Welcome to Mastermind! 
        Developed by Steven Harris
        COMP 1046 Object-Oriented Programming 
        Press Enter to Continue ''')
        super()




m2 = originalMasterMind()
m2.play()
#print(b.generateMasterCode(4))










