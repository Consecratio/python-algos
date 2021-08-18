'''
SIMILAR
-------------------------------------------------------------------------


PROMPT
-------------------------------------------------------------------------
Given a Maze array (2D Array), a startRow, startCol, endRow, and endCol. Output if there is a path from the start location
to the end location. Return True if a path can be found, return False if no path exists.

0 = open path
1 = wall

Maze = [
    [0,0,1,1,1],
    [0,0,0,0,1],
    [0,1,1,1,1],
    [0,0,0,0,1],
]

startRow = 1
startCol = 1
endRow = 3
endCol = 2
'''

def mazeFinder(maze, startRow, startCol, endRow, endCol):
    if len(maze) == 0: return False

    found_exit = travel(maze, startRow, startCol, endRow, endCol)

    return found_exit

def travel(maze, startRow, startCol, endRow, endCol, memo = {}):
    first_call = True

    # base case
    if startRow == endRow and startCol == endCol:
        print("FOUND THE END")
        memo[f"{endRow}{endCol}"] = True
        return memo

    # already been here
    if f"{startRow}{startCol}" in memo:
        return memo

    # start with end location
    if f"{endRow}{endCol}" not in memo:
        memo[f"{endRow}{endCol}"] = False
    else:
        first_call = False
 
    # add current location as traveled
    memo[f"{startRow}{startCol}"] = False
    
    # N
    if startRow > 0 and memo[f"{endRow}{endCol}"] == False:
        if maze[startRow - 1][startCol] == 0:
            memo = travel(maze, startRow - 1, startCol, endRow, endCol, memo)
    # E
    if startCol < len(maze[startRow]) - 1 and memo[f"{endRow}{endCol}"] == False:
        if maze[startRow][startCol + 1] == 0:
            memo = travel(maze, startRow, startCol + 1, endRow, endCol, memo)
    # S
    if startRow < len(maze) - 1 and memo[f"{endRow}{endCol}"] == False:
        if maze[startRow + 1][startCol] == 0:
            memo = travel(maze, startRow + 1, startCol, endRow, endCol, memo)
    # W
    if startCol > 0 and memo[f"{endRow}{endCol}"] == False:
        if maze[startRow][startCol - 1] == 0:
            memo = travel(maze, startRow, startCol - 1, endRow, endCol, memo)

    if first_call == True:
        print(memo)
        return memo[f"{endRow}{endCol}"]
    
    return memo

'''
CODE ABOVE THIS AREA
'''

maze = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]

startRow = 1
startCol = 1
endRow = 2
endCol = 3

print(mazeFinder(maze, startRow, startCol, endRow, endCol))