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
        self.restricciones[numero_de_nodo_actual]=[] 
        self.cargas[numero_de_nodo_actual]=[]  
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
        if nodo not in self.restricciones:
            self.restricciones[nodo] = []

        self.restricciones[nodo].append([gdl,valor])

        return 0

    def agregar_fuerza(self, nodo, gdl, valor):
        
        """Implementar"""	
        if nodo not in self.cargas:
            self.cargas[nodo] = []
    
        self.cargas[nodo].append([gdl,valor])
        
        return 0


    def ensamblar_sistema(self, factor_peso_propio=0.):
      
        self.K=np.zeros((self.Nnodos*3,self.Nnodos*3))
        f=np.zeros(self.Nnodos*3)
        """Implementar"""
        for barra in self.barras:
            ni=barra.ni
            nj=barra.nj
            K_e=barra.obtener_rigidez(self)
            f_e=barra.obtener_vector_de_cargas(self)
            d=[3*ni,3*ni+1,3*ni+2,3*nj,3*nj+1,3*nj+2]
            for i in range(6):
                p=d[i]
                for j in range(6):
                    q=d[j]
                    self.K[p,q] += K_e[i,j]
                f[p]+=f_e[i]
        for i in range(self.Nnodos):
            #print(i)
            print(self.cargas)
            #print(self.restricciones)
            Ncargas=len(self.cargas[i])
            #print(Ncargas)
            for carga in self.cargas[i]:
                print(carga)
                if len(carga)>0:
                    #print(carga)
                    gdl= carga[0]
                    fi= carga[1]
                    print(f"agregando carga de {fi} en GDL {gdl}")
                    gdl_global=3*i + gdl
                    f[gdl_global]+=fi
        self.K=K
        self.F=f
        self.u=np.zeros(self.Nnodos*3)        

        return 0



    def resolver_sistema(self):
        gdl_=[]
        u=self.u
        for i in range(self.Nnodos*3):
            gdl_.append(i)
        gdl_fijos=[]
        for i in range(self.Nnodos):
            res_nodo=(self.restricciones[i])
            if len(res_nodo)>0:
                for j in res_nodo:
                    print(i*3+j[0])
                    gdl_fijos.append(i*3+j[0])
                    u[i*3+j[0]]=j[1]
        gdl_libres=np.setdiff1d(gdl_,gdl_fijos)
        print(gdl_libres)
        print(gdl_fijos)
        Kff=self.K[np.ix_(gdl_libres,gdl_libres)]
        Kcc=self.K[np.ix_(gdl_fijos,gdl_fijos)]
        Kcf=self.K[np.ix_(gdl_fijos,gdl_libres)]
        Kfc=self.K[np.ix_(gdl_libres,gdl_fijos)]
        #print(Kff)
        #print(Kcc)
        uc=u[gdl_fijos]
        Ff=self.F[gdl_libres]-(Kfc@uc)
        u[gdl_libres]=solve(Kff,Ff)
        R=Kcf@u[gdl_libres]+Kcc@u[gdl_fijos]-self.F[gdl_fijos]
        self.u=u
        self.Ff=Ff
        self.Kcc=Kcc
        self.Kff=Kff
        self.Kcf=Kcf
        self.Kfc=Kfc
        self.R=R
        self.Fc=self.F[gdl_fijos]
        self.uc=u[gdl_fijos]
        self.uf=u[gdl_libres]
                
        """Implementar"""	
    
        return 0

    def obtener_desplazamiento_nodal(self, n):
        
        """Implementar"""	
        
        return self.u


    def obtener_fuerzas(self):
        
        lista=[]
        for i in self.barras:
            agregar=i.obtener_fuerza(self)
            lista.append(float(agregar))
        return lista


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
