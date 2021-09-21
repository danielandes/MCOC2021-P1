import numpy as np
from constantes import g_, ρ_acero, E_acero


class Barra(object):

    """Constructor para una barra"""
    def __init__(self, ni, nj, seccion, color=np.random.rand(3)):
        super(Barra, self).__init__()
        self.ni = ni
        self.nj = nj
        self.seccion = seccion
        self.color = color

    def obtener_conectividad(self):
        return [self.ni, self.nj]

    def calcular_largo(self, reticulado):
        """Devuelve el largo de la barra. 
        xi : Arreglo numpy de dimenson (3,) con coordenadas del nodo i
        xj : Arreglo numpy de dimenson (3,) con coordenadas del nodo j
        """
        
        ni = self.ni
        nj = self.nj

        xi = reticulado.xyz[ni,:]
        xj = reticulado.xyz[nj,:]

        # print(f"Barra {ni} a {nj} xi = {xi} xj = {xj}")
        
        largo = np.linalg.norm(xi-xj)

        return largo

    def calcular_peso(self, reticulado):
        
        Peso_seccion= self.seccion.peso()
        largo= self.calcular_largo(reticulado)
        peso_barra =largo*Peso_seccion

        return peso_barra


    def obtener_rigidez(self, ret):
        ni = self.ni
        nj = self.nj

        xi = ret.xyz[ni,:]
        xj = ret.xyz[nj,:]
	
        L=self.calcular_largo(ret)
        cosX=(xj[0]-xi[0])/L
        cosY=(xj[1]-xi[1])/L
        cosZ=(xj[2]-xi[2])/L
        TT=np.array([[-cosX], [-cosY], [-cosZ], [cosX], [cosY], [cosZ]])
        T=np.array([[-cosX, -cosY, -cosZ, cosX, cosY, cosZ],])
        ke=(self.seccion.area()*E_acero/L)*np.matmul(TT,T)
        #print(xi,xj,cosX,cosY,cosZ)
        return ke

    def obtener_vector_de_cargas(self, ret):
        print(self.calcular_peso(ret))
        return (self.calcular_peso(ret)/2)*np.array(ret.factor_peso_propio)


    def obtener_fuerza(self, ret):
        ni = self.ni
        nj = self.nj

        xi = ret.xyz[ni,:]
        xj = ret.xyz[nj,:]
	
        L=self.calcular_largo(ret)
        cosX=(xj[0]-xi[0])/L
        cosY=(xj[1]-xi[1])/L
        cosZ=(xj[2]-xi[2])/L
        T=np.array([[-cosX, -cosY, -cosZ, cosX, cosY, cosZ],])
        """Implementar"""	
        u_e=np.array([ret.u[3*ni],ret.u[3*ni+1],ret.u[3*ni+2],ret.u[3*nj],ret.u[3*nj+1],ret.u[3*nj+2]])
        se=(self.seccion.area()*E_acero/self.calcular_largo(ret))*np.matmul(T,u_e)
        #print(se)
        
        return float(se)




    def chequear_diseño(self, Fu, ret, ϕ=0.9):
        
        """Implementar"""	
        
        return 0





    def obtener_factor_utilizacion(self, Fu, ϕ=0.9):
        
        """Implementar"""	
        
        return 0


    def rediseñar(self, Fu, ret, ϕ=0.9):
        
        """Implementar"""	
        
        return 0


