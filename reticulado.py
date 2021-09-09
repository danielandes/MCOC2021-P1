import numpy as np
from scipy.linalg import solve

class Reticulado(object):
    """Define un reticulado"""
    __NNodosInit__ = 100

    #constructor
    def __init__(self):
        super(Reticulado, self).__init__()
        
        print ("Constructor de Reticulado")
        
        self.xyz = np.zeros((Reticulado.__NNodosInit__,3), dtype = np.double)
        self.Nnodos = 0
        self.barras = []
        self.cargas = {}
        self.restricciones = {}
        """Implementar"""	
        


    def agregar_nodo(self, x, y, z=0):
        
        """Implementar"""	
         
        #print(f"Quiero agregar un nodo en ({x} {y} {z})")
        numero_de_nodo_actual = self.Nnodos
        self.xyz[numero_de_nodo_actual,:] = [x,y,z]
        self.Nnodos += 1

        return 0

    def agregar_barra(self, barra):
        
        """Implementar"""	
        
        self.barras.append(barra)

        return 0

    def obtener_coordenada_nodal(self, n):
        
        """Implementar"""	

        return self.xyz[n]

    def calcular_peso_total(self):
        
        """Implementar"""	
        Peso_Total = 0
        for i in self.barras:
            Peso_Total += i.calcular_peso(self)
            
        return Peso_Total

    def obtener_nodos(self):
        
        return self.xyz

    def obtener_barras(self):
        
        return self.barras



    def agregar_restriccion(self, nodo, gdl, valor=0.0):
        
        """Implementar"""	
        
        return 0

    def agregar_fuerza(self, nodo, gdl, valor):
        
        """Implementar"""	
        
        return 0


    def ensamblar_sistema(self):
        
        """Implementar"""	
        
        return 0



    def resolver_sistema(self):
        
        """Implementar"""	
        
        return 0

    def obtener_desplazamiento_nodal(self, n):
        
        """Implementar"""	
        
        return 0


    def obtener_fuerzas(self):
        
        """Implementar"""	
        
        return 0


    def obtener_factores_de_utilizacion(self, f):
        
        """Implementar"""	
        
        return 0

    def rediseñar(self, Fu, ϕ=0.9):
        
        """Implementar"""	
        
        return 0



    def chequear_diseño(self, Fu, ϕ=0.9):
        
        """Implementar"""	
        
        return 0







    def __str__(self):

        s = "Soy un reticulado :)"

        s += "\n"

        s += str(self.xyz[0 : self.Nnodos,:])

        # print (s)

        # print ("nodos:")
        print("nodos:")
        for i in range(self.Nnodos):
            pos=(self.obtener_coordenada_nodal(i))
            print(i,":","(",pos[0],pos[1],pos[2],")")
        print("barras:")
        for i in range(len(self.barras)):
            nodo=self.barras[i].obtener_conectividad()
            print(i,":","[",nodo[0],nodo[1],"]")
        return s
