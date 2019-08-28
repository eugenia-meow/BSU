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
        #drawCircleBresenham()
        drawCircleMidpoint()
        for i in range(2, len(line)):
            x = int(round(line[i][0]))
            y = int(round(line[i][1]))
            if x >= 0 and x <= S - 1 and y >= 0 and y <= S - 1:
                grid[x][y] = 1

def addPoints(x1, y1, x, y):
    line.append((x1 + x,y1 + y))
    line.append((x1 + x,y1 - y))
    line.append((x1 - x,y1 + y))
    line.append((x1 - x,y1 - y))
    line.append((x1 + y,y1 + x))
    line.append((x1 + y,y1 - x))
    line.append((x1 - y,y1 + x))
    line.append((x1 - y,y1 - x))
    
    
        
def drawCircleBresenham():
    x1, y1, x2, y2 = line[0][0], line[0][1], line[1][0], line[1][1]
    R = dist(x1, y1, x2, y2)
    if R == 0:
        return
    x = 0
    y = R
    delta = 3 - 2* R
    addPoints(x1, y1, x, y)
    while (y >= x):
        x += 1
        if delta > 0:
            y -= 1  
            delta = delta + 4 * (x - y) + 10
        else:
            delta = delta + 4 * x + 6
        addPoints(x1, y1, x, y)
        
def drawCircleMidpoint():
    x1, y1, x2, y2 = line[0][0], line[0][1], line[1][0], line[1][1]
    R = dist(x1, y1, x2, y2)
    if R == 0:
        return
    x = R
    y = 0
    P = 1 - R
    line.append((x1 + x,y1 + y))
    line.append((x1 + y,y1 - x))
    line.append((x1 + y,y1 + x))
    line.append((x1 - x,y1 + y))
    while (x > y):
        y += 1
        if P <= 0:
            P += 2*y + 1
        else:
            x -= 1
            P += 2*(y - x) + 1
        if x < y:
            break
        line.append((x1 + x,y1 + y))
        line.append((x1 - x,y1 + y))
        line.append((x1 - x,y1 - y))
        line.append((x1 + x,y1 - y))
        if x != y:
            line.append((x1 + y,y1 + x))
            line.append((x1 - y,y1 + x))
            line.append((x1 + y,y1 - x))
            line.append((x1 - y,y1 - x))
