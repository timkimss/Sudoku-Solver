

puzzle1 = [
    [0, 0, 0, 1, 0, 5, 0, 6, 8],
    [0, 0, 0, 0, 0, 0, 7, 0, 1],
    [9, 0, 1, 0, 0, 0, 0, 3, 0],
    [0, 0, 7, 0, 2, 6, 0, 0, 0],
    [5, 0, 0, 0, 0, 0, 0, 0, 3],
    [0, 0, 0, 8, 7, 0, 4, 0, 0],
    [0, 3, 0, 0, 0, 0, 8, 0, 5],
    [1, 0, 5, 0, 0, 0, 0, 0, 0],
    [7, 9, 0, 4, 0, 1, 0 , 0, 0]]

# Print a given puzzle.
def printPuzzle(puzzle):

    for i in range(9):
        if i % 3 == 0 and i != 0:
            print ("- - - - - - - - - -")
        
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end = '')

            if j == 8:
                print (str(puzzle[i][j]))
            
            else:
                print (str(puzzle[i][j]) + " ", end = "")
    print()

# Returns the first empty value in the puzzle. Starts from top left corner, goes left to right, and then moves down.
def findEmpty(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return (i, j)
    return None

def isValid(puzzle, value, position):
    for i in range(9):
        if puzzle[position[0]][i] == value and position[1] != i:
            return False
        
    for j in range(9):
        if puzzle[j][position[1]] == value and position[0] != j:
            return False
    
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if puzzle[i][j] == value and (position[0] != i and position[1] != j):
                return False
    
    return True

def algorithm(puzzle):
    empty = findEmpty(puzzle)
    if empty == None:
        return True
    
    row, col = empty
    
    for i in range(1, 10):
        if isValid(puzzle, i, (row, col)):
            puzzle[row][col] = i

            if algorithm(puzzle): 
                return True
            puzzle[row][col] = 0

    return False

printPuzzle(puzzle1)
algorithm(puzzle1)
print ('--------------------')
printPuzzle(puzzle1)