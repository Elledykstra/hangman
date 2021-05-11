x = 300
y = 300

def setup():
    size(600, 600)

def draw():
    background(0, 122, 41)
    display()

# Man
def display():
    # Pole
    stroke(200)
    line(x+80, y+130, x+80, y-160)
    line(x+130, y+130, x+30, y+130)
    line(x+80, y-160, x-20, y-160)
    line(x-20, y-160, x-20, y-120)
    
    # Head
    noFill()
    circle(x-20, y-90, 60);
    
    # Body
    line(x-20, y-60, x-20, y+50)
    
    # Left Leg
    line(x-20, y+50, x-60, y+110)
    # Right Leg
    line(x-20, y+50, x+20, y+110)
    
    # Left Arm
    line(x-20, y-30, x-60, y+15)
    # Right Arm
    line(x-20, y-30, x+20, y+15)
