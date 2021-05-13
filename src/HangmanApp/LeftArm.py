class LeftArm:
    #Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
     
    #Display Method
    def displayLeftArm(self):
        line(self.x-20, self.y-30, self.x-60, self.y+15)
        
