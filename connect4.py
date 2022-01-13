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
        
    return board

def checkland(board):
    countY = 0
    countR = 0
    
    for row in board:
        if countY == 4 or countR == 4:
            return 1
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
                
    return 0
    


            
            
            


    


myBoard = [[".",".",".",".",".","."],[".",".",".",".",".","."],[".",".",".",".",".","."],[".",".",".",".",".","."],[".",".",".",".",".","."],["Y","Y","Y",".",".","."]]
run = True
player = 1
scores = [0,0]

print("Player 1 is Y\n Player 2 is R")

while run:
    showScore(scores)
    
    print("##########  Player",player,"Turn  ############")
    showBoard(myBoard)
    col = int(input("Drop a disk\n"))
    
    myBoard = dropD(myBoard,player,col)

    showBoard(myBoard)

    scores[player-1] += checkland(myBoard)


    if player == 1:
        player += 1
    else:
        player -= 1


    


####### Test ########
print("Out of loop")
