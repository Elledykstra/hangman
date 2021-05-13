class Body:
    #Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
     
    #Display Method
    def displayBody(self):
        line(self.x-20, self.y-60, self.x-20, self.y+50)
