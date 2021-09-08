from numpy import pi, sqrt
from constantes import g_, ρ_acero
 
class Circular(object):
    """define una seccion Circular"""

    def __init__(self, D, Dint):
        super(Circular, self).__init__()
        """Implementar"""	

        self.D = D
        self.Dint = Dint

    def area(self):
        

        """Implementar"""	

        return pi*(self.D**2 - self.Dint**2)/4
    

    def peso(self):

        
        """Implementar"""	
        
        return self.area()*ρ_acero*g

    def inercia_xx(self):

        
        """Implementar"""	
        
        return pi*(self.D**4 - self.Dint**4)/4

    def inercia_yy(self):

        
        """Implementar"""	
        
        return self.inercia_xx()

    def __str__(self):

        
        """Implementar"""   
        
        return f"Sección Circular D = {self.D} Dint = {self.Dint}"

