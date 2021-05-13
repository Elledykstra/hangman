class RightLeg:
    #Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
     
    #Display Method
    def displayRightLeg(self):
        line(self.x-20, self.y+50, self.x+20, self.y+110)
