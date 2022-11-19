class cylinders():
    def __init__(self,Radius,Height):
        self.Radius = Radius
        self.Height = Height
    def getHeight(self):
        return self.Height
    def getRadius(self):
        return self.Radius
    def calculate(self):
        self.measure = (self.Radius) * (self.Radius) * 3.14 * (self.Height)
        return self.measure
cylin1 = cylinders(5,10)
cylin2 = cylinders(7,3)

print("Cylinder[1]")
print("Radius is :",cylin1.Radius)
print("Height is :",cylin1.Height)
print("Result of first measure is :",cylin1.calculate())
print(" ")
print("Cylinder[2]")
print("Radius is :",cylin2.Radius)
print("Height is :",cylin2.Height)
print("Result of first measure is :",cylin2.calculate())