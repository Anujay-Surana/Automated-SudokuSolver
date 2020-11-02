gameBoard = [
  [0,0,4,0,0,0,0,6,7],
  [3,0,0,4,7,0,0,0,5],
  [1,5,0,8,2,0,0,0,3],
  [0,0,6,0,0,0,0,3,1],
  [8,0,2,1,0,5,6,0,4],
  [4,1,0,0,0,0,9,0,0],
  [7,0,0,0,8,0,0,4,6],
  [6,0,0,0,1,2,0,0,0],
  [9,3,0,0,0,0,7,1,0]
  ] #Sudoku Board in the format of 9*9 2D Array

def printBoard(board):#Function to Display the Board, With a few touch-ups for visual appeal
  count = 0
  for rows in range(len(board)):
    if(count == 3):
      print('\n------------------')
      count = 0

    else:
      print()

    count += 1

    for columns in range(len(board[rows])):
      print(board[rows][columns],end = " ")

def findEmpty(board):#Function to find any empty/unfilled spaces in the Sudoku Board[Empty Spaces are in the form of 0]
  for rows in range(len(board)):
    for columns in range(len(board[rows])):
      if board[rows][columns] == 0:
        return rows,columns

def checkValidity(board,pos,num):#Function to check the validity of Inputing a certain number in a paticular board in the passed in Coordinate Poistion
    row = pos[0]
    column = pos[1]

    if board[row][column]  == num:
        return True
    
    for nums in range(len(board)):
        if num == board[nums][column]:
            return False
        if num == board[row][nums]:
            return False
    boxRows = pos[1] // 3
    boxCols = pos[0] // 3

    for i in range(boxCols*3, boxCols*3 + 3):
        for j in range(boxRows * 3, boxRows*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False
    return True

def solveBoard(board):#Function to Solve the Board using the Backtracking Algorithm
    if findEmpty(board) == None:  
        return True
    coordinates = findEmpty(board)
    row = coordinates[0]
    column = coordinates[1]
    for possibleNums in range(1,10):
        if checkValidity(board,(row,column),possibleNums):
            board[row][column] = possibleNums
            if solveBoard(board):
                return True
            board[row][column] = 0
    return False

print('Original Board :')
printBoard(gameBoard)#Displaying the Original Board
solveBoard(gameBoard)#Calling the solveBoard() Function to solve the Passed in gameBoard
print('\n\nSolved Board :')
printBoard(gameBoard)#Displaying the Solved Board
input()

							