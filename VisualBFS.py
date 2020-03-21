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
    path.pop(0)            
    # Start Path
    for i in path:
        grid[i[0][0]][i[0][1]] = "p"    #Set Value p for path values
        drawGrid()                      # Draw Grid
        pygame.time.wait(200)           # Slow Time for visual affects  
        pygame.display.flip()           # Update Screen 
    grid[0][0] = "s"                    # Show Start and End Value
    grid[12][12] = "e"    
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


# Define Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (100, 200, 200)
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
WINDOW_SIZE = [510, 510]
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
                s = [0,0]
                e = [12, 12]
                bfs(s, e)
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Exit Loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Returns Position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)

        
            # Set's location to 1, Creates "WALL"
            if grid[row][column] == 1:
                grid[row][column] = 0
            else:
                grid[row][column] = 1

                

 
    # Set the screen background
    screen.fill(BLACK)
 
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
    clock.tick(10)
 
    # Update Screen
    pygame.display.flip()
 
pygame.quit()