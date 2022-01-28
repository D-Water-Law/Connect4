class Board:
    def __init__(self):
        self.board = [
            [".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "."]
        ]

    def getBoard(self):
        return self.board
        
    def showBoard(self):
        print("  0 1 2 3 4 5")
        num = -1
        for row in self.board:
            num += 1
            print(str(num)+"|"+" ".join(row)+"|")

    def resetBoard(self):
        self.board = [[".", ".", ".", ".", ".", "."],
                      [".", ".", ".", ".", ".", "."],
                      [".", ".", ".", ".", ".", "."],
                      [".", ".", ".", ".", ".", "."],
                      [".", ".", ".", ".", ".", "."],
                      [".", ".", ".", ".", ".", "."]]
 # Check if column is not full   
    def checkTopCol(self,col):
        if self.board[0][col] != ".":
            print("Collumn full !! Select another collumn\n")
            return False
        else:
            return True

            

    def dropD(self, user, col):
        row = 5
        check = True
            

        while check:
            if self.board[row][col] == ".":
                if user == 1:
                    self.board[row][col] = "Y"
                else:
                    self.board[row][col] = "R"
                check = False
            else:
                row -= 1

        return [row, col]

    def checkall(self, last_d): #returns 1 if 4 in a row in all directions

        # last_d [0] = row of the last disc dropped
        # last_d[1] = collumn of the last disc dropped
        last_dr = last_d[0]
        last_dc = last_d[1]

        disc = self.board[last_dr][last_dc]
        # disc = last disc letter

        # checks for horizontal win
        countY = 0
        countR = 0

        for row in self.board:
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
                if self.board[row][last_dc] == disc:
                    count += 1

                row += 1

            if count == 4:
                print("Vertical win !!")
                return 1

        ##################### check positive horizontal win

        if last_dr <= 2:
            count = 1
            pos = 1

            while count != 4 and last_dr - pos > -1 and last_dc + pos < 6:
                if self.board[last_dr - pos][last_dc + pos] == disc:
                    count += 1
                    pos += 1
                else:
                    break

            pos = 1

            while count != 4 and last_dr + pos < 6 and last_dc - pos > -1:
                if self.board[last_dr + pos][last_dc - pos] == disc:
                    count += 1
                    pos += 1
                else:
                    break

            if count == 4:
                print("Diagonal win")
                return 1

            ############# check for negative diagonal ###################

            count = 1
            pos = 1

            while count != 4 and last_dr - pos > -1 and last_dc - pos > -1:
                if self.board[last_dr - pos][last_dc - pos] == disc:
                    count += 1
                    pos += 1
                else:
                    break

            pos = 1

            while count != 4 and last_dr + pos < 6 and last_dc + pos < 6:
                if self.board[last_dr + pos][last_dc + pos] == disc:
                    count += 1
                    pos += 1
                else:
                    break

            if count == 4:
                print("Diagonal win")
                return 1

        return 0


def showScore(points):
    print("Player 1:", points[0])
    print("Player 2:", points[1])


############### Main Game ################
# myBoard = Board()

# run = True
# player = 1
# scores = [0, 0]

# print("Player 1 is Y\nPlayer 2 is R")

# while run:
#     showScore(scores)

#     print("##########  Player", player, "Turn  ############")
#     myBoard.showBoard()
#     col = int(input("Drop a disk\n"))

#     

#     myBoard.showBoard()

#     if myBoard.checkall(last_dc) == 1:
#         choice = int(input("Do you want to play again?\n1.Yes\n2.No\n"))
#         if choice == 2:
#             run = False
#             scores[player-1] += 1
#         else:
#             scores[player-1] += 1
#             myBoard.resetBoard()

#     if player == 1:
#         player += 1
#     else:
#         player -= 1


# ####### Out of loop ########
# print("Game Over")
# showScore(scores)

# # test from personal computer
