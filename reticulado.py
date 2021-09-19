import numpy as np
from scipy.linalg import solve

class Reticulado(object):
    """Define un reticulado"""
    __NNodosInit__ = 100

    #constructor
    def __init__(self):
        super(Reticulado, self).__init__()
        
        # print("Constructor de Reticulado")
        
        self.xyz = np.zeros((Reticulado.__NNodosInit__,3), dtype=np.double)
        self.Nnodos = 0
        self.barras = []
        self.cargas = {}
        self.restricciones = {}
        """Implementar"""	
        


    def agregar_nodo(self, x, y, z=0):
        

        # print(f"Quiero agregar un nodo en ({x} {y} {z})")
        numero_de_nodo_actual = self.Nnodos

        self.xyz[numero_de_nodo_actual,:] = [x, y, z]

        self.Nnodos += 1
        
        return 0

    def agregar_barra(self, barra):
        
        self.barras.append(barra)        
        
        return 0

    def obtener_coordenada_nodal(self, n):
        
        return self.xyz[n]

    def calcular_peso_total(self):
        
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
        
        if no_existe_restriccion_pal_nodo:
            self.restricciones[nodo] = []

        self.restricciones[nodo].append(gdl,valor)

        return 0

    def agregar_fuerza(self, nodo, gdl, valor):
        
        """Implementar"""	
 
        if no_existe_fuerza_pal_nodo:
            self.cargas[nodo] = []

        self.cargas[nodo].append(gdl,valor)

        return 0


    def ensamblar_sistema(self, factor_peso_propio=0.):
        
        """Implementar"""

        # Ensablmar rigidez y vector de cargas

        for e in self.barras: #recorrer barras
            ni = 2500
            nj = 2333

            ke = e.obtener_rigidez()
            fe = e.obtener_vector_de_carga()

            d = [3*ni, 3*ni+1, 3*ni+2, 3*nj, 3*nj+1, 3*nj+2]
        
            for i in range(6):
                p = d[i]
                for j in range(6):
                    q = d[j]
                    K[p,q] += k_e[i,j]

                f[p] += f_e[i]

        #agregar cargas puntuales

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

        #s = "Soy un reticulado :)"

        #s += "\n"
        
        #s += str(self.xyz[0 : self.Nnodos,:])+"\n"*2

        s ="nodos:"+"\n"
        
        for i in range(self.Nnodos):
            pos=(self.obtener_coordenada_nodal(i))
            agregar=(str(i)+" : "+"( "+str(pos[0])+", "+str(pos[1])+", "+str(pos[2])+")")
            s+=str(agregar)+"\n"
            
        s += "\n"+"barras:"+"\n"    
  
        for i in range(len(self.barras)):
            nodo=self.barras[i].obtener_conectividad()
            agregar=(str(i)+" : "+"[ "+str(nodo[0])+" "+str(nodo[1])+" ]")
            s+=str(agregar)+"\n"
            
        return s
