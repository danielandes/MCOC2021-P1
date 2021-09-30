from reticulado import Reticulado
from barra import Barra
from graficar3d import ver_reticulado_3d
from constantes import *
from math import sqrt
from secciones import SeccionICHA


L = 2.*m_
H = 2.*m_
B = 1.*m_

#Inicializar modelo
ret = Reticulado()

#Nodos

cero_x = -1.404922251873611572e+01*m_
cero_y = 4.281724747887941618e+01*m_


L_total = 177.48*m_
L_barra_inf = L_total/10
L = L_barra_inf
ret.agregar_nodo(cero_x ,0, cero_y)        # 0
ret.agregar_nodo(cero_x + 1*L,0, cero_y)   # 1 
ret.agregar_nodo(cero_x + 2*L,0, cero_y)   # 2
ret.agregar_nodo(cero_x + 3*L,0, cero_y)   # 3 
ret.agregar_nodo(cero_x + 4*L,0, cero_y)   # 4 
ret.agregar_nodo(cero_x + 5*L,0, cero_y)   # 5 
ret.agregar_nodo(cero_x + 6*L,0, cero_y)   # 6 
ret.agregar_nodo(cero_x + 7*L,0, cero_y)   # 7 
ret.agregar_nodo(cero_x + 8*L,0, cero_y)   # 8 
ret.agregar_nodo(cero_x + 9*L,0, cero_y)   # 9 
ret.agregar_nodo(cero_x + 10*L,0, cero_y)  # 10 

ret.agregar_nodo(cero_x,0, cero_y + L)        # 11  
ret.agregar_nodo(cero_x + 1*L,0, cero_y + L)  # 12
ret.agregar_nodo(cero_x + 2*L,0, cero_y + L)  # 13
ret.agregar_nodo(cero_x + 3*L,0, cero_y + L)  # 14
ret.agregar_nodo(cero_x + 4*L,0, cero_y + L)  # 15
ret.agregar_nodo(cero_x + 5*L,0, cero_y + L)  # 16
ret.agregar_nodo(cero_x + 6*L,0, cero_y + L)  # 17
ret.agregar_nodo(cero_x + 7*L,0, cero_y + L)  # 18
ret.agregar_nodo(cero_x + 8*L,0, cero_y + L)  # 19
ret.agregar_nodo(cero_x + 9*L,0, cero_y + L)  # 20
ret.agregar_nodo(cero_x + 10*L,0, cero_y + L) # 21


ret.agregar_nodo(cero_x ,4, cero_y)        # 22
ret.agregar_nodo(cero_x + 1*L,4, cero_y)   # 23
ret.agregar_nodo(cero_x + 2*L,4, cero_y)   # 24
ret.agregar_nodo(cero_x + 3*L,4, cero_y)   # 25
ret.agregar_nodo(cero_x + 4*L,4, cero_y)   # 26
ret.agregar_nodo(cero_x + 5*L,4, cero_y)   # 27
ret.agregar_nodo(cero_x + 6*L,4, cero_y)   # 28
ret.agregar_nodo(cero_x + 7*L,4, cero_y)   # 29 
ret.agregar_nodo(cero_x + 8*L,4, cero_y)   # 30 
ret.agregar_nodo(cero_x + 9*L,4, cero_y)   # 31 
ret.agregar_nodo(cero_x + 10*L,4, cero_y)  # 32 

ret.agregar_nodo(cero_x,4, cero_y + L)        # 33
ret.agregar_nodo(cero_x + 1*L,4, cero_y + L)  # 34
ret.agregar_nodo(cero_x + 2*L,4, cero_y + L)  # 35
ret.agregar_nodo(cero_x + 3*L,4, cero_y + L)  # 36
ret.agregar_nodo(cero_x + 4*L,4, cero_y + L)  # 37
ret.agregar_nodo(cero_x + 5*L,4, cero_y + L)  # 38
ret.agregar_nodo(cero_x + 6*L,4, cero_y + L)  # 39
ret.agregar_nodo(cero_x + 7*L,4, cero_y + L)  # 40
ret.agregar_nodo(cero_x + 8*L,4, cero_y + L)  # 41
ret.agregar_nodo(cero_x + 9*L,4, cero_y + L)  # 42
ret.agregar_nodo(cero_x + 10*L,4, cero_y + L) # 43



#Secciones de las barras
seccion_grande = SeccionICHA("[]350x150x37.8", color="#3A8431")#, debug=True)
seccion_chica = SeccionICHA("[]80x40x8", color="#A3500B")


#Crear y agregar las barras
ret.agregar_barra(Barra(0, 1, seccion_chica)) #0
ret.agregar_barra(Barra(1, 2, seccion_chica)) #1
ret.agregar_barra(Barra(2, 3, seccion_chica)) #2
ret.agregar_barra(Barra(3, 4, seccion_chica)) #3
ret.agregar_barra(Barra(4, 5, seccion_chica)) #4
ret.agregar_barra(Barra(5, 6, seccion_chica)) #5
ret.agregar_barra(Barra(6, 7, seccion_chica)) #6
ret.agregar_barra(Barra(7, 8, seccion_chica)) #7
ret.agregar_barra(Barra(8, 9, seccion_chica)) #8
ret.agregar_barra(Barra(9, 10, seccion_chica)) #9

ret.agregar_barra(Barra(0, 11, seccion_chica)) #10

ret.agregar_barra(Barra(11, 12, seccion_chica)) #11
ret.agregar_barra(Barra(12, 13, seccion_chica)) #12
ret.agregar_barra(Barra(13, 14, seccion_chica)) #13
ret.agregar_barra(Barra(14, 15, seccion_chica)) #14
ret.agregar_barra(Barra(15, 16, seccion_chica)) #15
ret.agregar_barra(Barra(16, 17, seccion_chica)) #15
ret.agregar_barra(Barra(17, 18, seccion_chica)) #15
ret.agregar_barra(Barra(18, 19, seccion_chica)) #15
ret.agregar_barra(Barra(19, 20, seccion_chica)) #15
ret.agregar_barra(Barra(20, 21, seccion_chica)) #15

ret.agregar_barra(Barra(10, 21, seccion_chica)) #15

ret.agregar_barra(Barra(0, 12, seccion_chica)) #15
ret.agregar_barra(Barra(12, 2, seccion_chica)) #15
ret.agregar_barra(Barra(2, 14, seccion_chica)) #15
ret.agregar_barra(Barra(14, 4, seccion_chica)) #15
ret.agregar_barra(Barra(4, 16, seccion_chica)) #15
ret.agregar_barra(Barra(16, 6, seccion_chica)) #15
ret.agregar_barra(Barra(6, 18, seccion_chica)) #15
ret.agregar_barra(Barra(18, 8, seccion_chica)) #15
ret.agregar_barra(Barra(8, 20, seccion_chica)) #15
ret.agregar_barra(Barra(20, 10, seccion_chica)) #15
ret.agregar_barra(Barra(1, 12, seccion_chica)) #15
ret.agregar_barra(Barra(3, 14, seccion_chica)) #15
ret.agregar_barra(Barra(5, 16, seccion_chica)) #15
ret.agregar_barra(Barra(7, 18, seccion_chica)) #15
ret.agregar_barra(Barra(9, 20, seccion_chica)) #15




ret.agregar_barra(Barra(22, 23, seccion_chica)) #15
ret.agregar_barra(Barra(23, 24, seccion_chica)) #15
ret.agregar_barra(Barra(24, 25, seccion_chica)) #15
ret.agregar_barra(Barra(25, 26, seccion_chica)) #15
ret.agregar_barra(Barra(26, 27, seccion_chica)) #15
ret.agregar_barra(Barra(27, 28, seccion_chica)) #15
ret.agregar_barra(Barra(28, 29, seccion_chica)) #15
ret.agregar_barra(Barra(29, 30, seccion_chica)) #15
ret.agregar_barra(Barra(30, 31, seccion_chica)) #15
ret.agregar_barra(Barra(31, 32, seccion_chica)) #15
ret.agregar_barra(Barra(23, 24, seccion_chica)) #15

ret.agregar_barra(Barra(22, 33, seccion_chica)) #15

ret.agregar_barra(Barra(33, 34, seccion_chica)) #15
ret.agregar_barra(Barra(34, 35, seccion_chica)) #15
ret.agregar_barra(Barra(35, 36, seccion_chica)) #15
ret.agregar_barra(Barra(36, 37, seccion_chica)) #15
ret.agregar_barra(Barra(37, 38, seccion_chica)) #15
ret.agregar_barra(Barra(38, 39, seccion_chica)) #15
ret.agregar_barra(Barra(39, 40, seccion_chica)) #15
ret.agregar_barra(Barra(40, 41, seccion_chica)) #15
ret.agregar_barra(Barra(41, 42, seccion_chica)) #15
ret.agregar_barra(Barra(42, 43, seccion_chica)) #15

ret.agregar_barra(Barra(32, 43, seccion_chica)) #15

ret.agregar_barra(Barra(22, 34, seccion_chica)) #15
ret.agregar_barra(Barra(34, 24, seccion_chica)) #15
ret.agregar_barra(Barra(24, 36, seccion_chica)) #15
ret.agregar_barra(Barra(26, 38, seccion_chica)) #15
ret.agregar_barra(Barra(38, 28, seccion_chica)) #15
ret.agregar_barra(Barra(28, 40, seccion_chica)) #15
ret.agregar_barra(Barra(40, 30, seccion_chica)) #15
ret.agregar_barra(Barra(30, 42, seccion_chica)) #15
ret.agregar_barra(Barra(42, 32, seccion_chica)) #15
ret.agregar_barra(Barra(23, 34, seccion_chica)) #15
ret.agregar_barra(Barra(25, 36, seccion_chica)) #15
ret.agregar_barra(Barra(27, 38, seccion_chica)) #15
ret.agregar_barra(Barra(29, 40, seccion_chica)) #15
ret.agregar_barra(Barra(31, 42, seccion_chica)) #15



ret.agregar_barra(Barra(0, 22, seccion_chica)) #15
ret.agregar_barra(Barra(1, 23, seccion_chica)) #15
ret.agregar_barra(Barra(2, 24, seccion_chica)) #15
ret.agregar_barra(Barra(3, 25, seccion_chica)) #15
ret.agregar_barra(Barra(4, 26, seccion_chica)) #15
ret.agregar_barra(Barra(5, 27, seccion_chica)) #15
ret.agregar_barra(Barra(6, 28, seccion_chica)) #15
ret.agregar_barra(Barra(7, 29, seccion_chica)) #15
ret.agregar_barra(Barra(8, 30, seccion_chica)) #15
ret.agregar_barra(Barra(9, 31, seccion_chica)) #15
ret.agregar_barra(Barra(10, 32, seccion_chica)) #15

ret.agregar_barra(Barra(11, 33, seccion_chica)) #15
ret.agregar_barra(Barra(12, 34, seccion_chica)) #15
ret.agregar_barra(Barra(13, 35, seccion_chica)) #15
ret.agregar_barra(Barra(14, 36, seccion_chica)) #15
ret.agregar_barra(Barra(15, 37, seccion_chica)) #15
ret.agregar_barra(Barra(16, 38, seccion_chica)) #15
ret.agregar_barra(Barra(17, 39, seccion_chica)) #15
ret.agregar_barra(Barra(18, 40, seccion_chica)) #15
ret.agregar_barra(Barra(19, 41, seccion_chica)) #15
ret.agregar_barra(Barra(20, 42, seccion_chica)) #15
ret.agregar_barra(Barra(21, 43, seccion_chica)) #15








ret.agregar_restriccion(0, 0, 0)
ret.agregar_restriccion(0, 1, 0)
ret.agregar_restriccion(0, 2, 0)
ret.agregar_restriccion(10, 0, 0)
ret.agregar_restriccion(10, 2, 0)
# ret.agregar_restriccion(10, 2, 0)

ret.agregar_restriccion(22, 0, 0)
ret.agregar_restriccion(22, 1, 0)
ret.agregar_restriccion(22, 2, 0)
ret.agregar_restriccion(32, 0, 0)
ret.agregar_restriccion(32, 2, 0)
# ret.agregar_restriccion(32, 2, 0)



#Cargar el nodo 4 en la direccion 1 (Y)
#ret.agregar_fuerza(4, 2, -100*KN_)

#Visualizar y comprobar las secciones
opciones_barras = {
	"ver_secciones_en_barras": False,
	"color_barras_por_seccion": True,
}

ver_reticulado_3d(ret,opciones_barras=opciones_barras)




#Resolver el problema
ret.ensamblar_sistema(factor_peso_propio=[0.,0.,-1.])
ret.resolver_sistema()
f = ret.obtener_fuerzas()

#Ver todo el reticulado en texto
print(ret)

ret.guardar("PRUEBA_PUENTE.h5")
