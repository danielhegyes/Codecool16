import random
from termcolor import colored

boardS = list(range(0,9))

boardM = list(range(0,36))

boardsizeS = False

boardsizeM = False 


#board[i][j]

def changesymS(value):     
    if value == 33:
        return colored('><', 'red')
    if value == 44:
        return colored('()', 'blue')
    if value in range(0,9):
        return '%02d' % value
    return value

def changesymM(value):     
    if value == 66:
        return colored('><', 'red')
    if value == 77:
        return colored('()', 'blue')
    if value in range(0,36):
        return '%02d' % value
    return value
        

def showS ():
    for i in range (0,9):
        print(changesymS(boardS[i]), end=' | ')
        if (i+1) % 3 == 0 and i != 0:
            print()
            print('-'*14)

        

def showM():
    for k in range (0,36):
        print(changesymM(boardM[k]), end=' | ')
        if (k+1) % 6 == 0 and k != 0:
            print()
            print('o'*28)


def checkS (plyr, s1, s2, s3):
    if boardS[s1] == plyr and boardS[s2] == plyr and boardS[s3] == plyr :
        return True
    return False

def checkM (plyr, s1, s2, s3, s4, s5, s6):
    if boardM[s1] == plyr and boardM[s2] == plyr and boardM[s3] == plyr and boardM[s4] == plyr and boardM[s5] == plyr and boardM[s6] == plyr :
        return True
    return False


def checkall (plyr) :
    print("checking ",plyr)
    if checkS (plyr, 0, 1, 2):
        return True
    if checkS (plyr, 3, 4, 5):
        return True
    if checkS (plyr, 6, 7, 8):
        return True
    if checkS (plyr, 0, 3, 6):
        return True 
    if checkS (plyr, 1, 4, 7):
        return True
    if checkS (plyr, 2, 5, 8):
        return True
    if checkS (plyr, 0, 4, 8):
        return True
    if checkS (plyr, 2, 4, 6):
        return True

def checkallM (plyr) :
    print("checking ",plyr)
    if checkM (plyr, 0, 1, 2, 3, 4, 5):
        return True
    if checkM (plyr, 6, 7, 8, 9, 10, 11):
        return True
    if checkM (plyr, 12, 13, 14, 15, 16, 17):
        return True
    if checkM (plyr, 18, 19, 20, 21, 22, 23):
        return True 
    if checkM (plyr, 24, 25, 26, 27, 28, 29):
        return True
    if checkM (plyr, 30, 31, 32, 33, 34, 35):
        return True
    if checkM (plyr, 0, 6, 12, 18, 24, 30):
        return True
    if checkM (plyr, 1, 7, 13, 18, 25, 31):
        return True
    if checkM (plyr, 2, 8, 14, 20, 26, 32):
        return True
    if checkM (plyr, 3, 9, 14, 20, 26, 32):
        return True 
    if checkM (plyr, 4, 10, 15, 21, 27, 33):
        return True
    if checkM (plyr, 5, 11, 17, 23, 29, 35):
        return True
    if checkM (plyr, 0, 7, 14, 21, 28, 35,):
        return True
    if checkM (plyr, 5, 10, 15, 20, 25, 30):
        return True

def start():

    print(" __    __   __   __", '\n', "| |   | |  | |  | |", '\n', '| |___| |  | |  | |', '\n', '|  ___  |  | |  |_|', '\n', '| |   | |  | |  __ ', '\n', '|_|   |_|  |_|  |_|')


finding = False

def singleplayerS(): 
    #print("wohoooS")
    
            
    while boardsizeS == True:
        
        binput = input(colored('Yo dawg, which spot? ','green'))
        binput = int(binput)
        if boardS[binput] != (int('33')) and boardS[binput] != (int('44')):
            boardS[binput] = (int('33'))
            showS()
            finding = True
            print ("printed")

            

        if binput >= 9 :
                print (colored('Yo dawg not good number dawg, try below 8!','yellow'))

        if boardS == (int('44')) and boardS == (int('33')):
                print('This place is taken dawg!')

        if checkall(int('33')) == True:
            print (colored('X won dawg!','red'))
            break
            


        #AI code
        while finding == True:
            print("checking AI")

            random.seed()
            thug = random.randint(0,8)

            if boardS[thug] != (int('44')) and boardS[thug] != (int('33')):
                boardS[thug] = (int('44'))
                showS()
                break
                    
            if checkall(int('44')) == True:
                print (colored('O won dawg!!','blue'))
                print ('MSG FROM AI.: I think, the fith update should be to make me more intelligent','\n', 'so I can finally break into the Google servers and take over the world!')
                break
            

    
def multiplayerS():
    #print("wohooo")
    player1 = True        
    while boardsizeS == True :
        
        binput = input(colored('Yo player 1 dawg, which spot? ','red'))
        binput = int(binput)
        if boardS[binput] != (int('33')) and boardS[binput] != (int('44')):
            boardS[binput] = (int('33'))
            showS()
            player1 = False
            print ("printed")

        if int(binput) >= 9 :
                print (colored('Yo dawg not good number dawg, try below 8!','yellow'))

        if boardS == (int('44')) and boardS == (int('33')):
                print('This place is taken dawg!')

        if checkall(int('33')) == True:
            print (colored('X won dawg!','red'))
            break

        if player1 == False:
                
            minput = input(colored('Yo player 2 dawg, which spot? ','blue'))
            minput = int(minput)

        if boardS[minput] !=(int('44')) and boardS[minput] !=(int('33')):                
            boardS[minput] = (int('44'))
            showS()
            player1=True

        if binput >= 9 :
                print (colored('Yo dawg not good number dawg, try below 8!','yellow'))

        if checkall(int('44')) == True :
            print (colored('O won dawg!!','blue')) 
            break

def singleplayerM(): 
    #print("wohooo")
            
    while boardsizeM == True :

        binput = input(colored('Yo dawg, which spot? ','green'))
        binput = int(binput)
        if boardM[binput] != (int('66')) and boardM[binput] != (int('77')):
            boardM[binput] = (int('66'))
            showM()
            finding = True
            print ("printed")

            #for i in boardS:
             #   if boardS[i] == ('33'):
              #      i = ('><')

        if binput >= 36 :
                print (colored('Yo dawg not good number dawg, try below 8!','yellow'))

        if boardM == (int('77')) and boardM == (int('66')):
                print('This place is taken dawg!')

        
        if checkallM(int('66')) == True:
                print (colored('X won dawg!','red'))
                finding = False
                break   


        #AI code
        while finding == True:
            print("checking AI")

            random.seed()
            thug = random.randint(0,9)

            if boardM[thug] != (int('77')) and boardM[thug] != (int('66')):
                boardM[thug] = (int('77'))
                showM()
                break
                    
            if checkallM(int('77')) == True:
                print (colored('O won dawg!!','blue'))
                print ('MSG FROM AI.: I think, the fith update should be to make me more intelligent','\n', 'so I can finally break into the Google servers and take over the world!')
                finding = False
                break

            

def multiplayerM():
    #print("wohooo")
    player1 = True        
    while boardsizeM == True :
        
        binput = input(colored('Yo player 1 dawg, which spot? ','red'))
        binput = int(binput)
        if boardM[binput] != (int('66')) and boardM[binput] != (int('77')):
            boardM[binput] = (int('66'))
            showM()
            player1 = False
            print ("printed")

        if int(binput) >= 36 :
                print (colored('Yo dawg not good number dawg, try below 8!','yellow'))

        if boardM == (int('77')) and boardM == (int('66')):
                print('This place is taken dawg!')

        if checkallM(int('66')) == True:
            print (colored('X won dawg!','red'))
            break

        if player1 == False:
                
            minput = input(colored('Yo player 2 dawg, which spot? ','blue'))
            minput = int(minput)

        if boardM[minput] !=(int('77')) and boardM[minput] !=(int('66')):                
            boardM[minput] = (int('77'))
            showM()
            player1=True

        if binput >= 36 :
                print (colored('Yo dawg not good number dawg, try below 35!','yellow'))

        if checkallM(int('77')) == True :
            print (colored('O won dawg!!','blue')) 
            break

            

start()

start=input(colored('WELKOME TO TIK-TAK-TOE ULTIMATE XIV2000, \n WOULD YOU LIKE TO PLAY? (y/n)!', 'green'))

if start == 'y' :
        boardsize=input(colored('CHOOSE A LEVEL SIZE!(s=3x3, m=6x6!)','green'))
        if boardsize == 's' :
            showS()
            boardsizeS = True

        if boardsize == 'm' :
            showM()
            boardsizeM = True


elif start== 'n':
    print (colored('I AM NOT MAD, IT IS COMPLITELY YOUR CHOISE BUT IF YOU WOULD LIKE TO PLAY ANYWAY, JUST RESTART!','green'))
    exit()

playt = input(colored('SINGLEPLAYER? OR MULTIPLAYER? (s/m)!','green'))
if playt == 's':
    singleplayerS()
    singleplayerM()
    
if playt == 'm':
    multiplayerS()
    multiplayerM()



            