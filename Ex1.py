#lab4 Ex1
class Firstcylinder ():
    height = 10
    Radius = 5
    pi =3.14
    
    def calculate(self):
        self.Measure = self.pi*(self.Radius*self.Radius)*self.height
        return self.Measure
     
class Secondcylinder (): 
    Radius = 7
    height = 13
    pi =3.14
    
    def calculate(self):
        self.Measure = self.pi*(self.Radius*self.Radius)*self.height
        return self.Measure
        
FirstBox = Firstcylinder()
SecondBox = Secondcylinder()

print(" ## Class with initial function ##")

print ("Firstbox cylinder  = " + str (FirstBox.calculate()))
print ("Secondbox cylinder = " + str (SecondBox.calculate()))

