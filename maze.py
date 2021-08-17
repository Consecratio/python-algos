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

def mazeFinder(maze, startRow, startCol, endRow, endCol):
    print(maze)
    print(startRow)
    print(startCol)
    print(endRow)
    print(endCol)

    return 0


maze = [
    [0,0,1,1,1],
    [1,0,0,0,1],
    [0,0,1,0,1],
    [1,1,0,0,1],
]

startRow = 1
startCol = 1
endRow = 3
endCol = 2

print(mazeFinder(maze, startRow, startCol, endRow, endCol))