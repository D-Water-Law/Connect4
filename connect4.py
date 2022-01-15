def showBoard (board):
    print("  0 1 2 3 4 5")
    num = -1
    for row in board:
        num += 1
        print(str(num)+"|"+" ".join(row)+"|")

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
        return 1
    

    # checks for vertical win
    count = 0
    row = last_dr

    while last_dr <= 2 and count != 4:
        if board[row][last_dc] == disc:
            count += 1
        
        else:
            row += 1

        if count == 4:
            print("Vertical win")
            return 1

    return 0
            
    
            


            

      
 

    

############### Main Game ################
myBoard = [[".",".",".",".",".","."],[".",".",".",".",".","."],[".",".",".",".",".","."],["Y",".",".",".",".","."],["Y",".",".",".",".","."],["Y",".",".",".",".","."]]
run = True
player = 1
scores = [0,0]

print("Player 1 is Y\nPlayer 2 is R\n")

while run:
    showScore(scores)
    
    print("##########  Player",player,"Turn  ############")
    showBoard(myBoard)
    col = int(input("Drop a disk\n"))
    
    myBoard, last_dc = dropD(myBoard,player,col)

    scores[player-1] += checkall(myBoard,last_dc)
    


    if player == 1:
        player += 1
    else:
        player -= 1


    


####### Test ########
print("Out of loop")

## just a git test ##
