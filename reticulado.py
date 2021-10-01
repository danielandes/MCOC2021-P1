import numpy as np
from scipy.linalg import solve
from matplotlib.pylab import *
import h5py


class Reticulado(object):
    """Define un reticulado"""
    __NNodosInit__ = 1

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
        self.xyz.resize((numero_de_nodo_actual+1,3))
        self.xyz[numero_de_nodo_actual,:] = [x, y, z]
        self.restricciones[numero_de_nodo_actual]=[] 
        self.cargas[numero_de_nodo_actual]=[]  
        self.Nnodos += 1
        
        return 0

    def agregar_barra(self, barra):
        
        self.barras.append(barra) 

        return 0

    def obtener_coordenada_nodal(self, n):
        
        return (self.xyz[n][0],self.xyz[n][1],self.xyz[n][2])

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
        self.restricciones[nodo].append([gdl,valor])
        
        return 0

    def agregar_fuerza(self, nodo, gdl, valor):
        
        """Implementar"""   
        self.cargas[nodo].append([gdl,valor])
        
        return 0


    def ensamblar_sistema(self, factor_peso_propio=0., factor_cargas=1):
        self.factor_peso_propio=[]
        for i in range(2):
            for j in range(len(factor_peso_propio)):
                self.factor_peso_propio.append(factor_peso_propio[j])
        #print(self.factor_peso_propio)
        K=np.zeros((self.Nnodos*3,self.Nnodos*3),dtype=np.double)
        f=np.zeros((self.Nnodos*3),dtype=np.double)
        #print(len(f))
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
                    K[p,q]+=K_e[i,j]
                f[p]+=f_e[i]
        #print("hola",f)
        for i in range(self.Nnodos):
            #print(i)
            #print(self.cargas)
            #print(self.restricciones)
            #Ncargas=len(self.cargas[i])
            #print(Ncargas)
            for carga in self.cargas[i]:
                #print(carga)
                if len(carga)>0:
                    #print(carga)
                    gdl= carga[0]
                    fi= carga[1]*factor_cargas
                    print(f"agregando carga de {fi} en GDL {gdl}")
                    gdl_global=3*i + gdl
                    f[gdl_global]+=fi
        #print("holo",f)
        self.K=K
        self.F=f
        self.u=np.zeros(self.Nnodos*3)
        #print(self.F) 
        #print(self.K)

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
                    #print(i*3+j[0])
                    gdl_fijos.append(i*3+j[0])
                    u[i*3+j[0]]=j[1]
        gdl_libres=np.setdiff1d(gdl_,gdl_fijos)
        #print(gdl_libres)
        #print(gdl_fijos)
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
        #print("prueba",Kcc@u[gdl_fijos])
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
        #print(self.u)
        #print(self.F)
        #print(self.K@self.u)
        #print(R)
        #print(self.Kff@self.uf)
        """Implementar"""   
        #print("halo")
        #cont=0
        xyz = np.zeros((self.Nnodos,3), dtype=np.double)
        cont=0

        for i in range(self.Nnodos):
            for pos in range(3):
                #print(pos)
                xyz[i][pos]=self.xyz[i,pos]
                cont+=1
            #print(xyz) 
        self.xyz=xyz
        return 0

    def obtener_desplazamiento_nodal(self, n):
        
        """Implementar"""   
        a,b,c=self.u[3*n],self.u[3*n+1],self.u[3*n+2]
        return a,b,c#self.u[3*n,3*n+1,3*n+2]


    def obtener_fuerzas(self):
        
        fuerzas = np.zeros((len(self.barras)), dtype=np.double)
        for i,b in enumerate(self.barras):
            fuerzas[i] = b.obtener_fuerza(self)

        return fuerzas


    def obtener_factores_de_utilizacion(self, f, ϕ=0.9):
        
        FU = np.zeros((len(self.barras)), dtype=np.double)
        for i,b in enumerate(self.barras):
            FU[i] = b.obtener_factor_utilizacion(f[i], ϕ)

        return FU

    def rediseñar(self, Fu, ϕ=0.9):
        
        """Implementar"""   
        
        return 0



    def chequear_diseño(self, Fu, ϕ=0.9):
        
        cumple = True
        for i,b in enumerate(self.barras):
            if not b.chequear_diseño(Fu[i], self, ϕ):
                print(f"----> Barra {i} no cumple algun criterio. ")
                cumple = False
        return cumple



    def guardar(self,nombre):
        nombre = str(nombre)
        fid = h5py.File(nombre, "w")

        # creacion de los datasets
        xyz = fid.create_dataset(("xyz"), shape=(1, 3), maxshape=(None, 3), dtype=float64)     
        barras = fid.create_dataset(("barras"), shape=(1, 2), maxshape=(None, 2), dtype=int32) 
        secciones = fid.create_dataset(("secciones"), shape=(1, 1), maxshape=(None, 1), dtype=h5py.string_dtype()) 
        restricciones = fid.create_dataset(("restricciones"), shape=(1, 2), maxshape=(None, 2), dtype=int32) 
        restricciones_val = fid.create_dataset(("restricciones_val"), shape=(1, 1), maxshape=(None, 1), dtype=float64) 
        cargas = fid.create_dataset(("cargas"), shape=(1, 2), maxshape=(None, 2), dtype=int32) 
        cargas_val = fid.create_dataset(("cargas_val"), shape=(1, 1), maxshape=(None, 1), dtype=float64) 
       
        cont_coord = 0
        for coord in self.xyz:
            #print (barra)
            xyz.resize((cont_coord+1,3))  #hago crecer el dataset
            xyz[cont_coord,0] = self.xyz[cont_coord,0]
            xyz[cont_coord,1] = self.xyz[cont_coord,1]
            xyz[cont_coord,2] = self.xyz[cont_coord,2]
            cont_coord += 1  
        
        
        cont_barra = 0
        for barra in self.barras:
            #print (barra)
            barras.resize((cont_barra+1,2))  #hago crecer el dataset
            barras[cont_barra,0] = barra.ni
            barras[cont_barra,1] = barra.nj
            cont_barra += 1   


        cont_sec = 0
        #print(self.barras[0].seccion.denominacion,self.barras[2].seccion.denominacion)
        for i in range(len(self.barras)):
            # print(i)
            secciones.resize((cont_sec+1,1))  #hago crecer el dataset
            secciones[cont_sec,0] = str(self.barras[i].seccion.denominacion)
            # print(self.barras[i].seccion.denominacion)
            cont_sec += 1

        cont_rest = 0
        for i in self.restricciones:
            for j in self.restricciones[i]:
                restricciones.resize((cont_rest+1,2))  #hago crecer el dataset
                restricciones_val.resize((cont_rest+1,1))  #hago crecer el dataset
                restricciones[cont_rest,0] = i
                restricciones[cont_rest,1] = j[0]

                restricciones_val[cont_rest,0] = j[1]
                cont_rest += 1 

        cont_cargas = 0
        for i in self.cargas:
            for j in self.cargas[i]:
                cargas.resize((cont_cargas+1,2))  #hago crecer el dataset
                cargas_val.resize((cont_cargas+1,1))  #hago crecer el dataset
                cargas[cont_cargas,0] = i
                cargas[cont_cargas,1] = j[0]
                
                cargas_val[cont_cargas,0] = j[1]
                cont_cargas += 1 
        # print (self.cargas)

        return 0


    def abrir(self,nombre):
        nombre = str(nombre)
        fid = h5py.File(nombre, "r")
        ret = self
        from barra import Barra
        from secciones import SeccionICHA

        for i in fid["xyz"]:
            ret.agregar_nodo(i[0],i[1],i[2])
            # print(i[0],i[1],i[2])
        

        dict_secciones = {}

        cont_1 = 0
        for i in fid["barras"]:
            seccion = str(fid["secciones"][cont_1])
            seccion = seccion[1:]
            seccion = seccion[1:]
            seccion = seccion[:-1]            
            seccion = seccion[1:]
            seccion = seccion[:-1]

            if not seccion in dict_secciones:
                dict_secciones[seccion] = SeccionICHA(str(seccion))

            

            #print (seccion)

            # print(fid["secciones"][cont_1])
            Barra_i = Barra(i[0],i[1],dict_secciones[seccion])
            # print(Barra(i[0],i[1],SeccionICHA(str(seccion))))
            ret.agregar_barra(Barra_i)
            cont_1 += 1

        cont_2 = 0
        for i in fid["cargas"]:
            valor = double(fid["cargas_val"][cont_2])
            ret.agregar_fuerza(int(i[0]),int(i[1]),valor)
            cont_2 += 1
        
        cont_3 = 0
        for i in fid["restricciones"]:
            valor_r = double(fid["restricciones_val"][cont_3])
            ret.agregar_restriccion(int(i[0]),int(i[1]),valor_r)
            cont_3 += 1

        return ret

    # def guardar(self, nombre):
    #     import h5py

    #     fid = h5py.File(nombre, "w")

    #     fid["xyz"] = self.xyz

    #     Nbarras = len(self.barras)
    #     barras = np.zeros((Nbarras,2), dtype=np.int32)
    #     secciones = fid.create_dataset("secciones", shape=(Nbarras,1), dtype=h5py.string_dtype())

    #     for i, b in enumerate(self.barras):
    #         barras[i,0] = b.ni
    #         barras[i,1] = b.nj
    #         secciones[i] = b.seccion.nombre()

    #     fid["barras"] = barras

    #     data_rest = fid.create_dataset("restricciones", (1,2), maxshape=(None,2), dtype=np.int32)
    #     data_rest_val = fid.create_dataset("restricciones_val", (1,), maxshape=(None,), dtype=np.double)
    #     nr = 0
    #     for nodo in  self.restricciones:
    #         for gdl, val in self.restricciones[nodo]:
    #             data_rest.resize((nr+1,2))
    #             data_rest_val.resize((nr+1,))
    #             data_rest[nr, 0] = nodo
    #             data_rest[nr, 1] = gdl
    #             data_rest_val[nr] = val
    #             nr += 1


    #     data_cargas = fid.create_dataset("cargas", (1,2), maxshape=(None,2), dtype=np.int32)
    #     data_cargas_val = fid.create_dataset("cargas_val", (1,), maxshape=(None,), dtype=np.double)
    #     nr = 0
    #     for nodo in  self.cargas:
    #         for gdl, val in self.cargas[nodo]:
    #             data_cargas.resize((nr+1,2))
    #             data_cargas_val.resize((nr+1,))
    #             data_cargas[nr, 0] = nodo
    #             data_cargas[nr, 1] = gdl
    #             data_cargas_val[nr] = val
    #             nr += 1


    # def abrir(self, nombre):

    #     import h5py
    #     from secciones import SeccionICHA
    #     from barra import Barra

    #     fid = h5py.File(nombre, "r")

    #     xyz = fid["xyz"][:,:]

    #     Nnodos = xyz.shape[0]

    #     for i in range(Nnodos):
    #         self.agregar_nodo(xyz[i,0], xyz[i,1], xyz[i,2])

    #     barras = fid["barras"]
    #     secciones = fid["secciones"]
    #     cargas = fid["cargas"]
    #     cargas_val = fid["cargas_val"]
    #     restricciones = fid["restricciones"]
    #     restricciones_val = fid["restricciones_val"]

    #     Nbarras = fid["barras"].shape[0]

    #     dict_secciones = {}

    #     for i in range(Nbarras):
    #         ni = barras[i,0]
    #         nj = barras[i,1]

    #         den = secciones[i][0]

    #         if not den in dict_secciones:
    #             dict_secciones[den] = SeccionICHA(den)

    #         self.agregar_barra(Barra(ni,nj,dict_secciones[den]))
            

    #     for i in range(restricciones.shape[0]):
    #         nodo = restricciones[i,0]
    #         gdl = restricciones[i,1]
    #         val = restricciones_val[i]

    #         self.agregar_restriccion(nodo, gdl, val)

    #     for i in range(cargas.shape[0]):
    #         nodo = cargas[i,0]
    #         gdl = cargas[i,1]
    #         val = cargas_val[i]

    #         self.agregar_fuerza(nodo, gdl, val)


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
        s+="\n"+"restricciones:"+"\n"
        c=0
        for i in self.restricciones:
            if len(self.restricciones[i])>0:
                 s+=str(c)+" : "+str(self.restricciones[i])+"\n"
            c+=1
        c=0
        s+="\n"+"cargas:"+"\n"
        for i in self.cargas:
            if len(self.cargas[i])>0:
                 s+=str(c)+" : "+str(self.cargas[i])+"\n"
            c+=1
        s+="\n"+"desplazamientos:"+"\n"
        for i in range(self.Nnodos):
            s+=str(i)+" : "+str(self.obtener_desplazamiento_nodal(i))+"\n"
        s+="\n"+"fuerzas:"+"\n"
        for i in range(len(self.barras)):
            s+=str(i)+" : "+str(self.obtener_fuerzas()[i])+"\n"
        return s
