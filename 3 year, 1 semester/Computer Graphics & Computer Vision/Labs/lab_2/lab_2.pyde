grid = [ [-1]*30  for n in range(30)] # list comprehension

w = 40 # width of each cell

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
        for point in line:
            grid[point[0]][point[1]] = -1 
        line[:] = []
    line.append((mouseY/w,mouseX/w))
    grid[mouseY/w][mouseX/w] = 1 
    if len(line) == 2:
        drawLine()

        
def drawLine():
    x1, y1, x2, y2 = line[0][0], line[0][1], line[1][0], line[1][1]
    grid[x2][y2] = -1 * grid[x2][y2] 
    dx = x2 - x1
    dy = y2 - y1
    
    sign_x = 1 if dx>0 else -1 if dx<0 else 0
    sign_y = 1 if dy>0 else -1 if dy<0 else 0
    
    if dx < 0: dx = -dx
    if dy < 0: dy = -dy
    
    if dx > dy:
        pdx, pdy = sign_x, 0
        es, el = dy, dx
    else:
        pdx, pdy = 0, sign_y
        es, el = dx, dy
    
    x, y = x1, y1
    
    error, t = el/2, 0        
    
    while t < el:
        error -= es
        if error < 0:
            error += el
            x += sign_x
            y += sign_y
        else:
            x += pdx
            y += pdy
        t += 1
        grid[x][y] = -1 * grid[x][y] 
        line.append((x,y))
    
