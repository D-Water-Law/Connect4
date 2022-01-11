def showBoard (board):
    print("  0 1 2 3 4 5")
    num = -1
    for row in board:
        num += 1
        print(str(num)+"|"+" ".join(row)+"|")

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

def checkland(board,user):
    countY = 0
    countR = 0
    


    for row in board:
        countY = 0
        countR = 0
        for col in row:
            if col == "Y":
                countY += 1
            elif col == "R":
                countR += 1

            
            


    


myBoard = [[".",".",".",".",".","."],[".",".",".",".",".","."],[".",".",".",".",".","."],[".",".",".",".",".","."],[".",".",".",".",".","."],[".",".",".",".",".","."]]
run = True
player = 1

print("Player 1 is Y\n Player 2 is R")

while run:
    
    print("##########  Player",player,"Turn  ############")
    showBoard(myBoard)
    col = int(input("Drop a disk\n"))
    
    myBoard = dropD(myBoard,player,col)

    showBoard(myBoard)

    if player == 1:
        player += 1
    else:
        player -= 1

    run = checkland(myBoard,player)


####### Test ########
print("Out of loop")
