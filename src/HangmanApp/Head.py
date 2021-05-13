class Head:
    #Member Variable

    
    #Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
     
    #Display Method
    def displayHead(self):
        noFill()
        ellipse(self.x-20, self.y-90, 60, 60)
        
