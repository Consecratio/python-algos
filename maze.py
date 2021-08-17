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
    [1,0,0,0,1],
    [0,0,1,0,1],
    [1,1,0,0,1],
]

startRow = 1
startCol = 1
endRow = 3
endCol = 2
'''

def mazeFinder(maze, startRow, startCol, endRow, endCol, memo = {}):
    if len(maze) == 0: return False
    if f"{endRow}{endCol}" not in memo: 
        memo[f'{endRow}{endCol}'] = False
    elif memo[f"{endRow}{endCol}"] is True:
        # base case for finding the end of the maze
        return memo

    
    # N
    if startRow > 0 and memo[f"{endRow}{endCol}"] == False:
        if maze[startRow - 1][startCol] == 0:
            memo = mazeFinder(maze, startRow - 1, startCol, endRow, endCol)
    # E
    if startCol < len(maze[startCol]) - 1 and memo[f"{endRow}{endCol}"] == False:
        if maze[startRow][startCol + 1] == 0:
            memo = mazeFinder(maze, startRow, startCol + 1, endRow, endCol)
    # S
    if startRow < len(maze) - 1:
        if maze[startRow + 1][startCol] == 0 and memo[f"{endRow}{endCol}"] == False:
            memo = mazeFinder(maze, startRow + 1, startCol, endRow, endCol)
    # W
    if startCol > 0:
        if maze[startRow][startCol - 1] == 0 and memo[f"{endRow}{endCol}"] == False:
            memo = mazeFinder(maze, startRow, startCol - 1, endRow, endCol)
    
    if memo[f"{endRow}{endCol}"] is True:
        # base case for finding the end of the maze
        return memo

    return memo

'''
CODE ABOVE THIS AREA
'''

maze = [
    [0,0,1,1,1],
    [1,0,0,0,1],
    [0,0,1,0,1],
    [1,1,0,0,1],
]

startRow = 1
startCol = 1
endRow = 2
endCol = 3

print(mazeFinder(maze, startRow, startCol, endRow, endCol))