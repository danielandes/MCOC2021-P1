from reticulado import Reticulado
from barra import Barra
from graficar2d import ver_reticulado_2d
from constantes import *
from secciones import Circular



#Inicializar modelo
ret = Reticulado()

#Nodos
ret.agregar_nodo(0,0)
ret.agregar_nodo(1,0)
ret.agregar_nodo(1,1)


#Seccion
circular_200_40 = Circular(200*mm_, 4*mm_)

#Barras
b1 = Barra(0, 1, circular_200_40)
b2 = Barra(1, 2, circular_200_40)
b3 = Barra(0, 2, circular_200_40)

#print (b1.calcular_peso(ret))
#print (b2.calcular_peso(ret))
#print (b3.calcular_peso(ret))


ret.agregar_barra(b1)
ret.agregar_barra(b2)
ret.agregar_barra(b3)

print(ret)

peso_total = ret.calcular_peso_total()

print(f"peso_total = {peso_total}")

ver_reticulado_2d(ret)
for i in ret.barras:
#    print(i.obtener_vector_de_cargas(ret))
    print("cosocoso",i.obtener_rigidez(ret))
#    print(i.calcular_largo(ret))
ret.agregar_restriccion(0, 0, 0)
ret.agregar_restriccion(0, 1, 0)
ret.agregar_restriccion(2, 1, 0) 
#diccionario={1:[]}
#diccionario={}
#diccionario[1]=[]
#diccionario[1].append([0,1])
#diccionario[1].append([0,2])
#print(diccionario)
#print(len(diccionario[1]))
print(ret.ensamblar_sistema(factor_peso_propio=[0., 0., 0.]))
print("halo")
#ret.resolver_sistema()
#coso=[0,1,2,3,4,5,6,7,8,9]
#print(coso[:,0:2])