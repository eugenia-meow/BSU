S = 20

grid = [ [-1]*S  for n in range(S)] # list comprehension

w = 1200//S # width of each cell

def setup():
    size(1200,1200)
    
def draw():
    
    x,y = 0,0 # starting position

    for row in grid:
        for col in row:
            if col == 1:
                fill(250,0,0)
            elif col == 2:
                fill(0,250,0)
            else:
                fill(255)
            rect(x, y, w, w)
            x = x + w  # move right
        y = y + w # move down
        x = 0 # rest to left edge
    if mousePressed is True:
        if in_grid(mouseY/w, mouseX/w):
            grid[mouseY/w][mouseX/w] = 1 
        
def mouseClicked():
    flood_fill(mouseY/w, mouseX/w)
    
def in_grid(x,y):
    return x <= S - 1 and y <= S - 1 and x >= 0 and y >= 0
def flood_fill(x, y):
    grid[x][y] = 2
    neighbours = [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]
    for neighbour in neighbours:
        x = neighbour[0]
        y = neighbour[1]
        if in_grid(x,y) and grid[x][y] == -1:
            flood_fill(x,y)
        

    
