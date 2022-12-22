import random 
class Point():
    def __init__(self, x ,y):
        self.x = x
        self.y = y   

class Transform():
    def __init__(self):
        self.x = 0 
        self.y = 0
        
    def Translate(self , direction = str("")):
        match direction:
            case "Forward":
                self.y += 1
            case "Backward":
                self.y -= 1
            case "Left":
                self.x -= 1
            case "Right":
                self.x += 1
            case _:
                print("need input in translation")

    def GetPosition(self):
        return self.x, self.y
    
    def SetPosition(self, x, y):
        self.x = x
        self.y = y
        
    def SetRandomPosition(self, max):
        self.x, self.y = random.randint(0,max)
        
    def MoveTward(_trans):
        self.GetPosition[0]
        