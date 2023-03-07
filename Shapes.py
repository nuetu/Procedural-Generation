class Shapes:
    def __init__(self, window, x1, y1, width):
        self.window = window
        self.x1 = x1
        self.y1 = y1
        self.x2 = x1 + width
        self.y2 = y1 + width
        self.xb = x1 + width/3
        self.xc = x1 + (2*width)/3
        self.yb = y1 + width/3
        self.yc = y1 + (2*width)/3
        
    def zero(self): #display nothing
        self.window.create_rectangle(self.x1,self.y1,self.x2,self.y2, outline="")
        
    def one(self):
        self.window.create_rectangle(self.x1,self.yb,self.xc,self.yc, fill="black", outline="black")
        
    def two(self):
        self.window.create_rectangle(self.xb,self.yb,self.xc,self.y2, fill="black", outline="black")
        
    def three(self):
        self.one()
        self.two()
        
    def four(self):
        self.window.create_rectangle(self.xb,self.yb,self.x2,self.yc, fill="black", outline="black")

    def five(self):
        self.one()
        self.four()
        
    def six(self):
        self.two()
        self.four()
        
    def seven(self):
        self.one()
        self.two()
        self.four()

    def eight(self):
        self.window.create_rectangle(self.xb,self.y1,self.xc,self.yc, fill="black", outline="black")

    def nine(self):
        self.one()
        self.eight()

    def ten(self):
        self.two()
        self.eight()

    def eleven(self):
        self.one()
        self.ten()

    def twelve(self):
        self.four()
        self.eight()

    def thirteen(self):
        self.five()
        self.eight()

    def fourteen(self):
        self.four()
        self.ten()

    def fifteen(self):
        self.three()
        self.twelve()
