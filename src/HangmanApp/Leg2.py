class Leg2:
    #Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
     
    #Display Method
    def displayLeg2(self):
        line(self.x-20, self.y+50, self.x+20, self.y+110)
