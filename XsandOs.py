# Tic Tac Toe

import random

def drawBoard(board):
    '''This function prints out the board that it was passed.
    "board" is a list of 10 strings representing the board (ignore index 0)'''
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter():
    # Let's the player type which letter they want to be.
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.
    letter= ""
    while letter != 'X' and letter != 'O':
        print 'Choose a letter, X or O'
        letter = raw_input().upper()
        
        #the first element is the players letter
    if letter == "X":
        return ["X", "O"]
    else:
        return ['O', 'X']

def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0,1) == 0:
        return 'player'
    else:
        return 'computer'
    #return 'player'

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print 'Do you want to play again (y/n)'
    return raw_input().lower().startswith('y')
    #return False

def makeMove(board, letter, move):
    board[move] = letter
    #return

def isWinner(bo, le):
    '''Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.'''
    return (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[4] == le and bo[5] ==  le and bo[6] ==  le) or (bo[7] == le and bo[8] ==  le and bo[9] ==  le) or (bo[1] == le and bo[4] ==  le and bo[7] ==  le)or (bo[2] == le and bo[5] ==  le and bo[8] ==  le) or (bo[3] == le and bo[6] ==  le and bo[9] ==  le) or (bo[1] == le and bo[5] ==  le and bo[9] ==  le) or (bo[3] == le and bo[5] ==  le and bo[7] ==  le)

def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    #return []
    dupeBoard =  []
    
    for i in board:
        dupeBoard.append(i)
    return dupeBoard

def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '

def getPlayerMove(board):
    # Let the player type in his move.
    move = ''
    while move not in "1 2 3 4 5 6 7 8 9".split() or not isSpaceFree(board, int(move)):
        print"Input move (1 - 9): "
        move = raw_input()
    return int(move)    
    #return 3

def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    return None

def getComputerMove(board, computerLetter):
    return getPlayerMove(board)

def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    #return False
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True



print('Welcome to Xs and Os!')

while True:
    # Reset the board
    theBoard = [' ']*10
    playerLetter, computerLetter = inputPlayerLetter()
    
    turn = whoGoesFirst()
    print 'The ' + turn + ' will go first.'
    
    gameIsPlaying = True
    
    while gameIsPlaying:
        if turn == 'player':
            #players turn
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print 'Hooray! You have won'
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print 'The game is a tie'
                    break
                else:
                    turn = 'computer'
        else:
            #computer's Turn
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            
            #check to see if the computer won
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print "The computer has won. Loser!!!"
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print 'The game is a tie'
                    break
                else:
                    turn =   'player'          
            

    if not playAgain():
        break
    
    