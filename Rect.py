class Rect(object):

    x = 0.0
    y = 0.0
    width = 0.0
    height = 0.0

    def __init__(self,x,y,width,height):
        print("initialised")
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def toString(self):
        strFrame = '({},{},{},{})'.format(self.x, self.y, self.width, self.height)
        return strFrame

    

    