def showBoard (board):
    print("  0 1 2 3 4 5")
    num = -1
    for row in board:
        num += 1
        print(str(num)+"|"+" ".join(row)+"|")

def resetBoard ():
    return  [[".",".",".",".",".","."],
             [".",".",".",".",".","."],
             [".",".",".",".",".","."],
             [".",".",".",".",".","."],
             [".",".",".",".",".","."],
             [".",".",".",".",".","."]]

def showScore (points):
    print("Player 1:",points[0])
    print("Player 2:",points[1])

def dropD(board,user,col):
    row = 5
    check = True
    while board[0][col] != ".":
        col = int(input("Collumn full !! Select another collumn\n"))

    while check:
        if board[row][col] == ".":
            if user == 1:
                board[row][col] = "Y"
            else:
                board[row][col] = "R"
            check = False
        else:
            row -= 1
        
    return board, [row, col]

def checkall(board,last_d):

    #last_d [0] = row of the last disc dropped
    #last_d[1] = collumn of the last disc dropped
    last_dr = last_d[0]
    last_dc = last_d[1]

    disc = board[last_dr][last_dc]
    # disc = last disc letter

    # checks for horizontal win
    countY = 0
    countR = 0
    
    for row in board:
        if countY == 4 or countR == 4:
            win_hor = 1
            break
        else:
            countY = 0
            countR = 0
            for col in row:
                if col == "Y":
                    countY += 1
                    countR = 0
    
                if col == "R":
                    countR += 1
                    countY = 0

    if countY == 4 or countR == 4:
        print("Horizontal win !!!")
        return 1
        
    

    # checks for vertical win
    count = 0
    
    row = last_dr

    if last_dr <= 2:
        for i in range(4):
            if board[row][last_dc] == disc:
                count += 1
            
            row += 1
        

        if count == 4:
            print("Vertical win !!")
            return 1

    ################## TO DO ##################### check positive horizontal win
            
    if last_dr <= 2:
        count = 1  
        pos = 1
        
        while count != 4 and last_dr - pos > -1 and last_dc + pos < 6:
            if board[last_dr - pos][last_dc + pos] == disc:
                count += 1
                pos += 1
            else:
                break
        
        pos = 1

        while count != 4 and last_dr + pos < 6 and last_dc - pos > -1:
            if board[last_dr + pos][last_dc - pos] == disc:
                count += 1
                pos += 1
            else:
                break

        if count == 4:
            print("Diagonal win")
            return 1
                
            
            



    return 0
            
    
            
    

############### Main Game ################
myBoard = [[".",".",".",".",".","."]
          ,[".",".",".",".",".","."],
           [".",".",".",".",".","."],
           [".",".","Y","R",".","."],
           [".","Y",".","R",".","."],
           ["Y",".",".","R",".","."]]
run = True
player = 1
scores = [0,0]

print("Player 1 is Y\nPlayer 2 is R")

while run:
    showScore(scores)
    
    print("##########  Player",player,"Turn  ############")
    showBoard(myBoard)
    col = int(input("Drop a disk\n"))
    
    myBoard, last_dc = dropD(myBoard,player,col)

    if checkall(myBoard,last_dc) == 1:
        showBoard(myBoard)
        choice = int(input("Do you want to play again?\n1.Yes\n2.No\n"))
        if choice == 2:
            run = False
            scores[player-1] += 1
        else:
            scores[player-1] += 1
            myBoard = resetBoard()
        
    
    

    if player == 1:
        player += 1
    else:
        player -= 1



####### Out of loop ########
print("Game Over")
print("Player 1 scored",scores[0])
print("Player 2 scored",scores[1])

