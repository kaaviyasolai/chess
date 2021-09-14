''' Written by: Kaaviya Solai '''
''' Published August 2020'''

''' 
By utilizing the Python coding language, I was able to program a code 
that accurately returns the number of moves a chess piece can make at any given location on a chess board. 
The user is prompted to enter the type of piece they would like to move, the row and column 
in which the piece is located, and the color of the piece. 

My program also stores data on the pieces placed on the board and makes sure 
future pieces cannot be moved to a spot on the board that already holds a piece. 
'''

'''
The function "piece" contains user input questions such as the type of chess piece, the color of the piece 
and the location of the piece. Based on the user's input, this function will call the corresponding function
which will retrieve the number of moves the user can make on an empty board given the location and piece the
user entered.
'''

def piece():
    #Check if user is still interested in playing.
    play = "Y"
    #Creates a board dictionary that stores the chess pieces the user enters 
    board = { }
    
    while play == "Y":
        piece_type =input("What type of piece would you like to move?")
        row =input("which row is your piece located in (from 0-7)?")
        col =input("Which column is your piece located in? (from 0-7)")
        color=input("What color is your piece?")

        #check if the location the user wants to put the piece in is empty
        key = str(row) + "," + str(col)
        while key in board.keys():
            print("There is already a piece on that square. Try again!")
            row =input("which row is your piece located in (from 0-7)?")
            col =input("Which column is your piece located in? (from 0-7)")
            key = str(row) + "," + str(col)


        board[key] = color
            

        #Since the user's input for row and column are stored as strings, we must cast them into integers in order to use them in mathetical operations within other functions. 
        row = int(row) 
        col = int(col)

        #convert piece input to lowercase
        piece_type = piece_type.lower()

        num_moves = None
        
        # Call the appropriate helper function based on which type of piece the user entered.
        if (piece_type == "king"):
            num_moves = king(board,row,col,color)
        elif piece_type == "rook":
            num_moves = rook(board,row,col,color)
        elif piece_type == "pawn":
            num_moves = pawn(board,row,col,color)
        elif piece_type == "bishop":
            num_moves = bishop(board,row,col,color)
        elif piece_type == "knight":
            num_moves = knight(board,row,col,color)
        elif piece_type == "queen":
            num_moves = queen(board,row,col,color)

        #If the user incorrectly enters the name of a chess piece, they will be prompted again. 
        if num_moves is not None:
            print("You can move " + str(num_moves) + " steps")
        else:
            print("You did not correctly enter a chess piece. Try again.")

        play = input("Enter 'Y' if you would like to continue playing. Enter 'N' if you would like to stop playing.")
    
    print("Thank you for playing!")

    
''' 
The function "king" has 4 parameters: board,row,column and color. This function tests edge cases of the 
king piece using if statements and returns the number of moves a king can make at the location 
the user entered.
'''
def king(board,row,col,color):
    # The variable "moves" is an integer that is initially set to 0. 
    # Moves will be incremented as the function finds spots for the piece to move to. 
    moves = 0 

    # Following conditionals check if the king can move in certain directions and if that spot is vacant.

    # top
    if row > 0:
        key = str(row-1) + "," + str(col)
        if key not in board.keys():
            moves+=1
        elif color != board[key]:
            moves+=1
    # bottom    
    if row < 7:
        key = str(row+1) + "," + str(col)
        if key not in board.keys():
            moves+=1
        elif color !=board[key]:
            moves+=1
    # right
    if col + 1 < 8:
        key = str(row) + "," + str(col+1)
        if key not in board.keys():
            moves+=1
        elif color != board[key] :
            moves+=1
    # left
    if col - 1 > -1:
        key = str(row) + "," + str(col-1)
        if key not in board.keys():
            moves+=1
        elif color!= board[key]:
            moves+=1
    # bottom right
    if row + 1 < 8 and col + 1 < 8:
        key = str(row+1) + "," + str(col+1)
        if key not in board.keys():
            moves+=1
        elif color!= board[key]:
            moves+=1
    #top right
    if row - 1 > 0 and col + 1 < 8:
        key = str(row-1) + "," + str(col+1)
        if key not in board.keys():
            moves+=1
        elif color!=board[key]:
            moves+=1
    #bottom left
    if row + 1 < 8 and col - 1 > -1:
        key = str(row+1) + "," + str(col-1)
        if key not in board.keys():
            moves+=1
        elif color!=board[key]:
            moves+=1
    #top left
    if row -1 > 0 and col - 1 > - 1:
        key = str(row-1) + "," + str (col-1)
        if key not in board.keys():
            moves+=1
        elif color!=board[key]:
            moves+=1
        
    return moves


''' 
The function "rook" has 4 parameters: board,row,column and color. This function uses for loops to check for possible moves the user's piece
can make and returns the total number of moves. 
'''

def rook(board,row,col,color):
    # Moves will be incremented as the function finds spots for the piece to move to. 
    moves = 0

    # Following conditionals check if the rook can move in certain directions and check if those spots are vacant.

    #down
    r_temp = row +1
    key = str(r_temp) + " " + str(col)
    while key not in board.keys() and r_temp < 8:
        moves+=1
        r_temp+=1
    
    if r_temp < 8:
        if color!=board[key]:
            moves+=1

    #up
    r_temp = row -1
    key = str(r_temp) + " " + str(col)
    while key not in board.keys() and r_temp > -1:
        moves+=1
        r_temp-=1
    
    if r_temp > -1:
        if color!=board[key]:
            moves+=1
  
    
    #right
    c_temp = col + 1
    key = str(row) + " " + str(c_temp)
    while key not in board.keys() and c_temp < 8:
        moves +=1
        c_temp+= 1
    
    if c_temp < 8:
        if color!= board[key]:
            moves+=1
    

    #left
    c_temp = col-1
    key = str(row) + " " + str(c_temp)
    while key not in board.keys() and c_temp>-1:
        moves+=1 
        c_temp-=1
    
    if c_temp>-1:
        if color!= board[key]:
            moves+=1

    ''' 
    returns the number of moves the user can make at the moment.
    '''
    return moves

''' 
The function "queen" has 4 parameters: board,row,column and color. Since the queen can move in any direction (vertically, horizontally,
and vertically), I figured that the total number of moves would be equal to the sum of the number of moves a rook and a bishop
can make from that location. This function uses the function "rook" and "bishop and adds the moves from
each of these functions to return the total number of moves a queen piece can make. 
'''
def queen(board,row,col,color):
    a = rook(board,row,col,color) #a stores the number of moves a rook can make given the row and column.
    b = bishop(board,row,col,color)#b stores the number of moves a bishop can make given the row and column.
    ''' 
    returns the number of moves the user can make at the moment.
    '''
    return a+b
    

''' 
The function "bishop" has 4 parameters: board,color, row and column. I found that finding the minimum between the distances to the edges of the board 
from the row and column the bishop is located and summing these minimums gives the total number of moves of a bishop. 
'''
def bishop(board,row,col,color):
    # Moves will be incremented as the function finds spots for the piece to move to. 
    moves =0
    
    # Following conditionals check if the bishop can move in certain directions and if those spots are vacant.
    
    #top right
    topright = min(row-0,7-col)
    r_temp = row - 1
    c_temp = col + 1
    while topright>0 and r_temp > -1 and c_temp <8:
        key = str(r_temp) + " " + str(c_temp)
        if key not in board.keys():
            moves+=1
            r_temp-=1
            c_temp+=1
            topright-=1
        
        else: # piece exists on that square, now check if color matches or does not match the piece
            if color != board [key]:
                moves+=1
                topright = 0
            
            else:
                moves=0
                topright = 0
        

    #top left
    topleft = min (row -0,col-0)
    r_temp = row - 1
    c_temp = col - 1
    while topleft>0 and r_temp>-1 and c_temp>-1:
        key = str(r_temp) + " " + str(c_temp)
        if key not in board.keys():
            moves+=1
            r_temp-=1
            c_temp-=1
            topleft-=1
        
        else:# piece exists on that square, now check if color matches or does not match the piece
            if color!= board[key]:
                moves+=1
                topleft = 0
            else:
                moves=0
                topleft = 0

    #bottom right
    botright = min(7-row,7-col)
    r_temp = row + 1
    c_temp = col + 1
    while botright>0 and r_temp < 8 and c_temp < 8:
        key = str(r_temp) + " " + str(c_temp)
        if key not in board.keys():
            moves+=1
            r_temp+=1
            c_temp+=1
            botright-=1
        else: # piece exists on that square, now check if color matches or does not match the piece
            if color!= board[key]:
                moves+=1
                botright = 0
            else:
                moves=0
                botright = 0

    #bottom left
    botleft = min(7-row, col-0)
    r_temp = row + 1
    c_temp = col - 1
    while botleft>0 and r_temp < 8 and c_temp > -1:
        key = str(r_temp) + " " + str(c_temp)
        if key not in board.keys():
            moves+=1
            r_temp+=1
            c_temp-=1
            botleft-=1
        else: # piece exists on that square, now check if color matches or does not match the piece
            if color!= board[key]:
                moves+=1
                botleft = 0
            else:
                moves=0
                botleft = 0
    ''' 
    returns the number of moves the user can make at the moment.
    '''
    return moves

''' 
The function "pawn" has 4 parameters: board,row, column and color. 
This function returns the number of moves a pawn can make depending on it's color and location on the board. 
'''
def pawn (board,row,col,color):
    #White pawns only move down on the board.
    moves = 0
    if color == "white":
        a = str(row-1) + " " + str(col-1)
        b = str(row-1) + " " + str(col+1)
        c = str(row-1) + " " + str(col)
        d = str(row-2) + " " + str(col)
        if row!=0:
            if c not in board.keys():
                moves+=1
            if a in board.keys() and color!= board[a]:
                moves+=1
            if b in board.keys() and color!=board[b]:
                moves+=1
            if row == 6 and c not in board.keys() and d not in board.keys():
                moves+=2
        else:
            print("This is an illegal position for a white pawn.")
            moves=0
   
    #Black pawns only move up on the board. 
    if color == "black":
        a = str(row+1) + " " + str(col-1)
        b = str(row+1) + " " + str(col+1)
        c = str(row+1) + " " + str(col)
        d = str(row+2) + " " + str(col)
        if row!=7:
            if c not in board.keys():
                moves+=1
            if a in board.keys() and color!= board[a]:
                moves+=1
            if b in board.keys() and color!=board[b]:
                moves+=1
            if row == 1 and c not in board.keys() and d not in board.keys():
                moves+=2
        else:
            print("This is an illegal position for a black pawn.")
            moves=0

    
    ''' 
    returns the number of moves the user can make at the moment.
    '''
    return moves

''' 
The function "knight" has 4 parameters: board,row,column and color. 
This function tests edge cases of the knight piece using if statements and returns the total number of moves 
the knight can make at the given location.
'''
def knight(board,row,col,color):
    # Moves will be incremented as the function finds spots for the piece to move to. 
    moves =0
    
    # Following conditionals check if the knight can move in certain directions.

    #right up 
            
    key = str(row-1) + " " + str(col+2)
    if row > 1 and key not in board.keys():
        moves+=1
    elif row > 1 and color!=board[key]:
        moves+=1
    #left up
    key = str(row-1) + " " + str(col-2)
    if row > 1  and key not in board.keys():
        moves+=1
    elif row >1 and color!=board[key]:
        moves+=1

    #left down
    key = str(row+1) + " " + str(col-2)

    if col > 1 and key not in board.keys() and row < 8 :
        moves+=1
    elif col>1 and row<8 and color!=board[key]:
        moves+=1

    #right down
    key = str(row+1) + " " + str(col+2)

    if col < 6 and key not in board.keys() and row < 7 :
        moves+=1
    elif col < 6 and row<7 and color!=board[key]:
        moves+=1  

    #top right
    key = str(row-2) + " " + str(col+1)

    if row>1 and col <7 and key not in board.keys():
        moves+=1
    elif row>1 and col<7 and color!=board[key]:
        moves+=1
    
    #top left
    key = str(row-2) + " " + str(col-1)

    if row>1 and col >0 and key not in board.keys():
        moves+=1
    elif row>1 and col>0 and color!=board[key]:
        moves+=1
    
    #bottom right
    key = str(row+2) + " " + str(col+1)
    if row<6 and col <7 and key not in board.keys():
        moves+=1
    elif row<6 and col<7 and color!=board[key]:
        moves+=1

    #bottom left
    key = str(row+2) + " " + str(col-1)
    if row<6 and col >0 and key not in board.keys():
        moves+=1
    elif row<6 and col>0 and color!=board[key]:
        moves+=1
    
    ''' 
    returns the number of moves the user can make at the moment.
    '''
    return moves

piece()