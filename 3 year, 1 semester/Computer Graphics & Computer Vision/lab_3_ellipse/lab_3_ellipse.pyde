S = 60
grid = [ [-1]*S  for n in range(S)] # list comprehension

w = 20 # width of each cell

line = []

def setup():
    size(1200,1200)
    
def draw():
    
    x,y = 0,0 # starting position

    for row in grid:
        for col in row:
          if col == 1:
              fill(250,0,0)
          else:
              fill(255)
          rect(x, y, w, w)
          x = x + w  # move right
        y = y + w # move down
        x = 0 # rest to left edge
        
        
def mousePressed():
    if len(line) >= 2:
        for i in range(len(line)):
            x = int(round(line[i][0]))
            y = int(round(line[i][1]))
            if x >= 0 and x <= S - 1 and y >= 0 and y <= S - 1:
                grid[x][y] = -1
        line[:] = []
    line.append((mouseY/w,mouseX/w))
    if len(line) == 1:
        grid[mouseY/w][mouseX/w] = 1 
    if len(line) == 2:
        drawEllipseMidpoint()
        for i in range(2, len(line)):
            x = int(round(line[i][0]))
            y = int(round(line[i][1]))
            if x >= 0 and x <= S - 1 and y >= 0 and y <= S - 1:
                grid[x][y] = 1

def addPoints(x1, y1, x, y):
    line.append((x1 + x,y1 + y))
    line.append((x1 - x,y1 + y))
    line.append((x1 - x,y1 - y))
    line.append((x1 + x,y1 - y))
        
def drawEllipseMidpoint():
    x1, y1, x2, y2 = line[0][0], line[0][1], line[1][0], line[1][1]
    a = abs(x2-x1)
    b = abs(y2-y1)
    x = 0
    y = b
    fx = 0
    fy = 2*a*a*b
    P = b*b - a*a*b + a*a/4
    while (fx < fy):
        addPoints(x1, y1, x, y)
        x += 1
        fx = fx + 2*b*b
        if P < 0:
            P += fx + b*b
        else:
            y -= 1
            fy -= 2*a*a
            P += fx + b*b - fy
    addPoints(x1, y1, x, y)
    p = (b*(x+0.5))**2 + (a*(y-1))**2 - (a*b)**2
    while y > 0:
        y -= 1
        fy -= 2*a*a
        if P >= 0:
            P = P - fy + a*a
        else:
            x += 1
            fx += 2*b*b
            P += fx - fy + a*a
        addPoints(x1, y1, x, y)
