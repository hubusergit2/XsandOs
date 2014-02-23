# x's and o's

import random
import pygame, sys
from pygame.locals import *

#start pygame
pygame.init()


#window constants
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 500
WINDOW_CENTER_X = WINDOW_WIDTH/2
WINDOW_CENTER_Y = WINDOW_HEIGHT / 2


#set up the window
windowSurface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT),0, 32)
pygame.display.set_caption("X's and O's")

# set up colours
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)


#Set up fonts
TITLEFONT = pygame.font.SysFont(None,36)
LETTERFONT = pygame.font.SysFont('Arial',36,True)
MESSAGEFONT = pygame.font.SysFont('Arial', 16, True)

#text constants
TITLE = TITLEFONT.render("Coder Dojo X's and O's", True, BLUE, WHITE)
titleRect = TITLE.get_rect()
titleRect.centerx = int(WINDOW_WIDTH /2)
titleRect.centery = int(WINDOW_HEIGHT / 8)

CHECKMESSAGE = MESSAGEFONT.render("Choose your letter X or O", True, BLUE, WHITE)
CheckRect = CHECKMESSAGE.get_rect()
CheckRect.centerx = int(WINDOW_WIDTH /2)
CheckRect.centery = int(WINDOW_HEIGHT / 8 * 7)

#player Wins Message
pWinMess = MESSAGEFONT.render("Congratulations. You beat the computer", True, BLUE, WHITE)
pWinRect = pWinMess.get_rect()
pWinRect.centerx = int(WINDOW_WIDTH /2)
pWinRect.centery = int(WINDOW_HEIGHT / 8 * 6)

#computer wins message
cWinMess = MESSAGEFONT.render("Hard luck.  The Computer Won",True, BLUE, WHITE)
cWinRect = cWinMess.get_rect()
cWinRect.centerx = int(WINDOW_WIDTH /2)
cWinRect.centery = int(WINDOW_HEIGHT / 8 * 7) - 40

#players tied message
tiedMess = MESSAGEFONT.render("That game was a tie.", True, BLUE, WHITE)
tiedRect = tiedMess.get_rect()
tiedRect.centerx = int(WINDOW_WIDTH /2)
tiedRect.centery = int(WINDOW_HEIGHT / 8 * 7) - 40

#play again message
playAgainMess = MESSAGEFONT.render("Do you want to play again? (y/n)", True, BLUE, WHITE)
playAgainRect = playAgainMess.get_rect()
playAgainRect.centerx = int(WINDOW_WIDTH /2)
playAgainRect.centery = int(WINDOW_HEIGHT / 8 * 7)


X = LETTERFONT.render('X',True,BLACK,WHITE)
O = LETTERFONT.render('O',True,BLACK,WHITE)

# declare global variables
gameState = 0
board = []
playerTurn = None


def drawBoard(board):
    '''draws the board to the window'''
    
    #clear the screen and set the background to white
    windowSurface.fill(WHITE)
    
    #draw the title and the lines
    windowSurface.blit(TITLE, titleRect)
    pygame.draw.line(windowSurface, BLACK, (WINDOW_CENTER_X - 30, WINDOW_CENTER_Y - 90),
                                            (WINDOW_CENTER_X - 30, WINDOW_CENTER_Y + 90),2)
    pygame.draw.line(windowSurface, BLACK, (WINDOW_CENTER_X + 30, WINDOW_CENTER_Y - 90),
                                            (WINDOW_CENTER_X + 30, WINDOW_CENTER_Y + 90),2)
    pygame.draw.line(windowSurface, BLACK, (WINDOW_CENTER_X - 90, WINDOW_CENTER_Y - 30),
                                            (WINDOW_CENTER_X + 90, WINDOW_CENTER_Y - 30),2)
    pygame.draw.line(windowSurface, BLACK, (WINDOW_CENTER_X - 90, WINDOW_CENTER_Y + 30),
                                            (WINDOW_CENTER_X + 90, WINDOW_CENTER_Y + 30),2)                                           
    
    
    #draw the x's and o's
    for i in range(3):
        for j in range(3):
            if (board[j + i*3+1] == "X"):
                windowSurface.blit(X, Rect(WINDOW_CENTER_X-90+15 + (j)*60, WINDOW_CENTER_Y + 30 + 15 - (i)*60, 60, 60))
            if (board[j + i*3 +1] == "O"):
                windowSurface.blit(O, Rect(WINDOW_CENTER_X-90+15 + (j)*60, WINDOW_CENTER_Y + 30+ 15 - (i)*60, 60, 60))            
    
    #draw the choose letter message
    if gameState == 0:
        windowSurface.blit(CHECKMESSAGE, CheckRect)

    #draw the Winners message
    if gameState == 2:
        if winner == 'player':
            windowSurface.blit(pWinMess, pWinRect)
        elif winner == 'computer':
            windowSurface.blit(cWinMess, cWinRect)
        else:
            windowSurface.blit(tiedMess, tiedRect)
        windowSurface.blit(playAgainMess, playAgainRect)

def init():
    global turn, board, gameState
    # Reset the board
    board = ([' '] * 10)
    gameState = 0 # gamestate 0 => get player letter, 1 => game playing, 2 => game over
    turn = whoGoesFirst()
    
    
    

def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '



def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # Check if the player could win on his next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True   

    
init()     
    
while (True):
   
    for event in pygame.event.get():

        #check for game quits
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONUP:

            #if the game is playing get the mouse clicks on the board
            if gameState == 1:
                move = None
                mousex, mousey = event.pos
                if (mousex > WINDOW_CENTER_X - 90 and mousex < WINDOW_CENTER_X - 30 and mousey > WINDOW_CENTER_Y + 30 and mousey < WINDOW_CENTER_Y + 90):
                        move = 1
                elif (mousex > WINDOW_CENTER_X - 30 and mousex < WINDOW_CENTER_X + 30 and mousey > WINDOW_CENTER_Y + 30 and mousey < WINDOW_CENTER_Y + 90):
                        move = 2
                elif (mousex > WINDOW_CENTER_X + 30 and mousex < WINDOW_CENTER_X + 90 and mousey > WINDOW_CENTER_Y + 30 and mousey < WINDOW_CENTER_Y + 90):
                        move = 3 
                elif (mousex > WINDOW_CENTER_X - 90 and mousex < WINDOW_CENTER_X - 30 and mousey > WINDOW_CENTER_Y - 30 and mousey < WINDOW_CENTER_Y + 30):
                        move = 4
                elif (mousex > WINDOW_CENTER_X - 30 and mousex < WINDOW_CENTER_X + 30 and mousey > WINDOW_CENTER_Y - 30 and mousey < WINDOW_CENTER_Y + 30):
                        move = 5
                elif (mousex > WINDOW_CENTER_X + 30 and mousex < WINDOW_CENTER_X + 90 and mousey > WINDOW_CENTER_Y - 30 and mousey < WINDOW_CENTER_Y + 30):
                        move = 6             
                elif (mousex > WINDOW_CENTER_X - 90 and mousex < WINDOW_CENTER_X - 30 and mousey > WINDOW_CENTER_Y - 90 and mousey < WINDOW_CENTER_Y - 30):
                        move = 7
                elif (mousex > WINDOW_CENTER_X - 30 and mousex < WINDOW_CENTER_X + 30 and mousey > WINDOW_CENTER_Y - 90 and mousey < WINDOW_CENTER_Y - 30):
                        move = 8
                elif (mousex > WINDOW_CENTER_X + 30 and mousex < WINDOW_CENTER_X + 90 and mousey > WINDOW_CENTER_Y - 90 and mousey < WINDOW_CENTER_Y - 30):
                        move = 9 

                #if the move is valid and it's the player turn make the players move
                if move != None and turn == 'player' :
                    makeMove(board, playerLetter, move)
                    turn = 'computer'
                if isWinner(board, playerLetter):
                    winner = 'player'
                    gameState = 2
                
                #check if there is a tie
                elif isBoardFull(board):
                    winner = 'tied'
                    gameState = 2                
                    
        elif event.type == KEYUP:

            #if the game is in start up get the players letter
            if gameState == 0: 
                if event.key == ord('x') or event.key == ord('X'):
                    playerLetter = 'X'
                    computerLetter = 'O'
                    gameState = 1
                elif event.key == ord('o') or event.key == ord('O'):
                    playerLetter = 'O'
                    computerLetter = 'X'
                    gameState = 1
            elif gameState == 2:
                if event.key == ord('y') or event.key == ord('Y'):
                    init()
                else:
                    pygame.quit()
                    sys.exit()

        # if it is the computers move, make the move
        if gameState == 1 and turn == "computer":
            makeMove(board, computerLetter, getComputerMove(board, computerLetter))
            turn = 'player'
            if isWinner(board, computerLetter):
                winner = 'computer'
                gameState = 2            
            #check if there is a tie
            elif isBoardFull(board):
                winner = 'tied'
                gameState = 2
            
          


               
    #draw the board
    drawBoard(board)
    
    #update the window
    pygame.display.update()
