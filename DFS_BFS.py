import pygame
import numpy as np


# Some Setup For BFS

R = 20
C = 20
r = 0
c = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]
path = []
buttonX = 550
buttonY = 25
buttonWidth = 50
buttonHeight = 50
buttonY2 = buttonY + buttonHeight + 10
buttonY3 = buttonY2 + buttonHeight + 10
visited = np.zeros((R,C))
prev = []

def bfs(s, e):
    # Do BFS staring at s
    prev = solve(s)
    # return reconstructed path from s to e
    return reconstructPath(s, e, prev)



def reconstructPath(s, e, prev):
    path = []
    path.append([prev[0][0]])
    #Add values that are next to each other to path, if it is not then don't add
    for i in prev:
        c1 = path[-1][0][0]
        c2 = path[-1][0][1]
        b1 = i[1][0][0]
        b2 = i[1][0][1]
        if c1 == b1:
            if c2 == b2 +1 or c2 == b2 - 1:
                path.append(i[1])
        if c2 == b2:
            if c1 == b1 + 1 or c1 == b1 - 1:
                path.append(i[1])
    path.reverse()
    #path.pop(0)            
    # Start Path
    for i in path:
        grid[i[0][0]][i[0][1]] = "p"    #Set Value p for path values
        drawGrid()                      # Draw Grid
        #pygame.time.wait(100)           # Slow Time for visual affects  
        pygame.display.flip()           # Update Screen 
    grid[0][0] = "s"                    # Show Start and End Value
    grid[12][12] = "e"    
    prev = []
    return path

def solve(s):
    r = s[0]        # Set Row Value
    c = s[1]        # Set Column Value
    q = []          # Create Queue
    prev = []       # Create Prev Array
    q.append([r,c]) # Append Start Value to Queue
    visited = np.zeros((R,C))   # Create an array of all zeros
    visited[r][c] = 1           # Mark as visited.

    
    while q:
        ##This shows the algorithm working by adding a "y" value to everything in the q
        for i in q:
            grid[q[0][0]][q[0][1]] = "y"
            drawGrid()
            #pygame.time.wait(200)
            pygame.display.flip()
        
        r = q[0][0]
        c = q[0][1]
        # Dequeue from Queue
        parent = q.pop(0)
        
        # For all 4 directions test if they are possible moves
        for i in range(4):
            rr = r +dr[i] 
            cc = c + dc[i]

            if rr < 0 or cc < 0: continue   # if smaller than grid size then no
            if rr >= R or cc >= C: continue # if bigger than grid size then no
            if grid[rr][cc] == "e":         #if end of the maze then continue
                prev.append([[rr,cc], [parent]])
                prev.pop(0)         # remove first element in array
                prev.reverse()      # Reverse Array
                return prev
            if grid[rr][cc] != 0: continue  # if value it not available
            if visited[rr][cc] == 1: continue   
            q.append([rr,cc])               #enqueue this spot
            visited[rr][cc] = 1             # Mark as Visited
            prev.append([[rr,cc], [parent]]) # add the previously visited node.



def dfs(s, e):
  
    prev = solvedfs(s)

    return reconstructPathdfs(s, e, prev)



def reconstructPathdfs(s, e, prev):
    path = []
    path.append([prev[0][0]])
    for i in prev:
        c1 = path[-1][0][0]
        c2 = path[-1][0][1]
        b1 = i[1][0][0]
        b2 = i[1][0][1]
        if c1 == b1:
            if c2 == b2 +1 or c2 == b2 - 1:
                path.append(i[1])
        if c2 == b2:
            if c1 == b1 + 1 or c1 == b1 - 1:
                path.append(i[1])
    path.reverse()    
    # Start Path
    for i in path:
        grid[i[0][0]][i[0][1]] = "p"    #Set Value p for path values
        drawGrid()                      # Draw Grid
        #pygame.time.wait(100)           # Slow Time for visual affects  
        pygame.display.flip()           # Update Screen 
    grid[0][0] = "s"                    # Show Start and End Value
    grid[12][12] = "e"   
    #prev = [] 
    return path

def solvedfs(s):
    stack = []   #LILO
    prev = []
    r = s[0]
    c = s[1]
    visited = np.zeros((R,C))
    stack.append([r, c])


    
    while len(stack) != 0:
        ##This shows the algorithm working by adding a "y" value to everything in the q
        for i in stack:
            grid[stack[-1][0]][stack[-1][1]] = "y"
            drawGrid()
            #pygame.time.wait(200)
            pygame.display.flip()
        
        r = stack[-1][0]
        c = stack[-1][1]
  
        parent = stack.pop(-1)
        
        # For all 4 directions test if they are possible moves
        for i in range(4):
            rr = r +dr[i]
            cc = c + dc[i]

            if rr < 0 or cc < 0: continue
            if rr >= R or cc >= C: continue
            if grid[rr][cc] == "e":
                visited[rr][cc] = 2
                stack.append([rr,cc])
                prev.append([[rr,cc], [parent]])
                prev.pop(0)
                prev.reverse()
                return prev
            if grid[rr][cc] != 0: continue
            if visited[rr][cc] == 1: continue
            stack.append([rr,cc])
            visited[rr][cc] = 1
            prev.append([[rr,cc], [parent]])


# Define Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (100, 100, 200)
YELLOW = (255, 255, 0)

 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20
# This sets the margin between each cell
MARGIN = 5
 
grid = []
for row in range(20):
    # Add an empty array that will hold each cell in this row
    grid.append([])
    for column in range(20):
        grid[row].append(0)  # Append a cell
 
# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
grid[0][0] = "s"
grid[12][12] = "e"
# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
#WINDOW_SIZE = [510, 510]
WINDOW_SIZE = [700, 700]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set Title
pygame.display.set_caption("BFS Select Left Arrow To start")
 
# Boolean for Game Loop
done = False
 
# Set Clock for Screen Updates
clock = pygame.time.Clock()



 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        #Run Alg if LEFT is broken
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                for i in range(len(grid)):
                    for j in range(len(grid)):
                        if grid[i][j] == "p" or grid[i][j] == "y":
                            grid[i][j] = 0
                        
                    
                drawGrid()
                pygame.display.flip()
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Exit Loop
        elif event.type == pygame.MOUSEBUTTONDOWN:

            # User clicks the mouse. Returns Position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)

           # If you click inside of the button this also runs the Algorithm
            if pos[0] > buttonX and pos[0] < buttonX + buttonWidth: 
                if pos[1] > buttonY and pos[1] < buttonY + buttonHeight:
                    s = [0,0]
                    e = [12, 12]
                    dfs(s, e)
            if pos[0] > buttonX and pos[0] < buttonX + buttonWidth: 
                if pos[1] > buttonY2 and pos[1] < buttonY2 + buttonHeight:
                    s = [0,0]
                    e = [12, 12]
                    bfs(s, e)
            if pos[0] > buttonX and pos[0] < buttonX + buttonWidth: 
                if pos[1] > buttonY3 and pos[1] < buttonY3 + buttonHeight:

                    for i in range(len(grid)):
                        for j in range(len(grid)):
                            if grid[i][j] == "p" or grid[i][j] == "y":
                                grid[i][j] = 0

            
            
            # Must click in grid
            if pos[0] > 510 or pos[1] > 510: continue


            # Set's location to 1, Creates "WALL"
            if grid[row][column] == 1:
                grid[row][column] = 0
            else:
                grid[row][column] = 1
        if event.type == pygame.MOUSEBUTTONUP:

            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column1 = pos[0] // (WIDTH + MARGIN)
            row1 = pos[1] // (HEIGHT + MARGIN)

            if row1 == row:
                if column1 > column:
                    for i in range(column, column1 + 1):
                        try:
                            grid[row][i] = 1
                        except IndexError:
                            continue
                if column > column1:
                    for i in range(column1, column + 1):
                        try:
                            grid[row][i] = 1
                        except IndexError:
                            continue

            if column1 == column:    
                if row1 > row:
                    for i in range(row, row1 + 1):
                        try:
                            grid[i][column] = 1
                        except IndexError:
                            continue
                if row > row1:
                    for i in range(row1, row + 1):
                        try:
                            grid[i][column] = 1
                        except IndexError:
                            continue

   
                

 
    # Set the screen background
    screen.fill(BLACK)
    # Draw Rectangle

    pygame.draw.rect(screen, GREEN,(buttonX,buttonY,buttonWidth,buttonHeight)) 
    pygame.draw.rect(screen, RED,(buttonX,buttonY2,buttonWidth,buttonHeight)) 
    pygame.draw.rect(screen, WHITE,(buttonX,buttonY3,buttonWidth,buttonHeight))

    font = pygame.font.Font('freesansbold.ttf', 20) 
  
    # create a text suface object, 
    # on which text is drawn on it. 
    text = font.render('DFS', True, BLACK)
    screen.blit(text, (buttonX ,buttonY))
    text = font.render('BFS', True, BLACK)
    screen.blit(text, (buttonX , buttonY2)) 
    font = pygame.font.Font('freesansbold.ttf', 15) 
    text = font.render('Clear', True, BLACK)
    screen.blit(text, (buttonX , buttonY3)) 
    

    # Draw the grid
    def drawGrid():
        for row in range(20):
            for column in range(20):
                color = WHITE
                if grid[row][column] == 1:
                    color = GREEN
                if grid[row][column] == "s":
                    color = BLACK
                if grid[row][column] == "e":
                    color = RED
                if grid[row][column] == "p":
                    color = GREY
                if grid[row][column] == "y":
                    color = YELLOW
                if grid[row][column] == 0:
                    color = WHITE
                pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
 
    #Call drawGrid()
    drawGrid()
    # Framer Per Second
    clock.tick(30)
 
    # Update Screen
    pygame.display.flip()
 
pygame.quit()
