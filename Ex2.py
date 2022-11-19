#lab4 Ex2
class Pyramid ():
    Base_len = 10
    Base_wid = 7
    Pyramid_hei = 17
    
    def calculate(self):
        self.Measure = (self.Base_len*self.Base_wid*self.Pyramid_hei)/3
        return self.Measure

Pyramid_A = Pyramid()
print ("volume of pyramid = " + str(Pyramid_A.calculate()))