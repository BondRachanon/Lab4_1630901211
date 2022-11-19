class Pyramid():
    def __init__(self,Length,Width,Height):
        self.Length = Length
        self.Width = Width
        self.Height = Height
class getLength():
    Length = "10"
class getWidth():
    Width = "7"
class getHeight():
    Height = "17"
class Calculate ():
    def Calvolume(self,Length,Width,Height):
        py = Pyramid(Length,Width,Height)
        self.volume = (py.Length*py.Width*py.Height)/3
        return self.volume

PRM = Calculate()
print("[ Volume of pyramid] is",PRM.Calvolume(10,7,17))
