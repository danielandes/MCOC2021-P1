from reticulado import Reticulado
from barra import Barra
from graficar3d import ver_reticulado_3d
from constantes import *
from math import sqrt
from secciones import SeccionICHA


ret = Reticulado()


cero_x = 5.075777986710320100e+00*m_
cero_y = 4.281724747887941618e+01*m_


L_total = 117.48*m_
L_barra_inf = L_total/20
L = L_barra_inf

ret.agregar_nodo(cero_x ,0, cero_y)         # 0
ret.agregar_nodo(cero_x + 1*L,0, cero_y)    # 1 
ret.agregar_nodo(cero_x + 2*L,0, cero_y)    # 2
ret.agregar_nodo(cero_x + 3*L,0, cero_y)    # 3 
ret.agregar_nodo(cero_x + 4*L,0, cero_y)    # 4 
ret.agregar_nodo(cero_x + 5*L,0, cero_y)    # 5 
ret.agregar_nodo(cero_x + 6*L,0, cero_y)    # 6 
ret.agregar_nodo(cero_x + 7*L,0, cero_y)    # 7 
ret.agregar_nodo(cero_x + 8*L,0, cero_y)    # 8 
ret.agregar_nodo(cero_x + 9*L,0, cero_y)    # 9 
ret.agregar_nodo(cero_x + 10*L,0, cero_y)   # 10 
ret.agregar_nodo(cero_x + 11*L,0, cero_y)   # 11
ret.agregar_nodo(cero_x + 12*L,0, cero_y)   # 12
ret.agregar_nodo(cero_x + 13*L,0, cero_y)   # 13 
ret.agregar_nodo(cero_x + 14*L,0, cero_y)   # 14 
ret.agregar_nodo(cero_x + 15*L,0, cero_y)   # 15 
ret.agregar_nodo(cero_x + 16*L,0, cero_y)   # 16 
ret.agregar_nodo(cero_x + 17*L,0, cero_y)   # 17 
ret.agregar_nodo(cero_x + 18*L,0, cero_y)   # 18 
ret.agregar_nodo(cero_x + 19*L,0, cero_y)   # 19 
ret.agregar_nodo(cero_x + 20*L,0, cero_y)   # 20 

ret.agregar_nodo(cero_x,0, cero_y + L)         # 21 
ret.agregar_nodo(cero_x + 1*L,0, cero_y + L)   # 22
ret.agregar_nodo(cero_x + 2*L,0, cero_y + L)   # 23
ret.agregar_nodo(cero_x + 3*L,0, cero_y + L)   # 24
ret.agregar_nodo(cero_x + 4*L,0, cero_y + L)   # 25
ret.agregar_nodo(cero_x + 5*L,0, cero_y + L)   # 26
ret.agregar_nodo(cero_x + 6*L,0, cero_y + L)   # 27
ret.agregar_nodo(cero_x + 7*L,0, cero_y + L)   # 28
ret.agregar_nodo(cero_x + 8*L,0, cero_y + L)   # 29
ret.agregar_nodo(cero_x + 9*L,0, cero_y + L)   # 30
ret.agregar_nodo(cero_x + 10*L,0, cero_y + L)  # 31
ret.agregar_nodo(cero_x + 11*L,0, cero_y + L)  # 32
ret.agregar_nodo(cero_x + 12*L,0, cero_y + L)  # 33
ret.agregar_nodo(cero_x + 13*L,0, cero_y + L)  # 34
ret.agregar_nodo(cero_x + 14*L,0, cero_y + L)  # 35
ret.agregar_nodo(cero_x + 15*L,0, cero_y + L)  # 36
ret.agregar_nodo(cero_x + 16*L,0, cero_y + L)  # 37
ret.agregar_nodo(cero_x + 17*L,0, cero_y + L)  # 38
ret.agregar_nodo(cero_x + 18*L,0, cero_y + L)  # 39
ret.agregar_nodo(cero_x + 19*L,0, cero_y + L)  # 40
ret.agregar_nodo(cero_x + 20*L,0, cero_y + L)  # 41



ret.agregar_nodo(cero_x ,4, cero_y)         # 42
ret.agregar_nodo(cero_x + 1*L,4, cero_y)    # 43
ret.agregar_nodo(cero_x + 2*L,4, cero_y)    # 44
ret.agregar_nodo(cero_x + 3*L,4, cero_y)    # 45
ret.agregar_nodo(cero_x + 4*L,4, cero_y)    # 46
ret.agregar_nodo(cero_x + 5*L,4, cero_y)    # 47
ret.agregar_nodo(cero_x + 6*L,4, cero_y)    # 48 
ret.agregar_nodo(cero_x + 7*L,4, cero_y)    # 49
ret.agregar_nodo(cero_x + 8*L,4, cero_y)    # 50 
ret.agregar_nodo(cero_x + 9*L,4, cero_y)    # 51 
ret.agregar_nodo(cero_x + 10*L,4, cero_y)   # 52 
ret.agregar_nodo(cero_x + 11*L,4, cero_y)   # 53
ret.agregar_nodo(cero_x + 12*L,4, cero_y)   # 54
ret.agregar_nodo(cero_x + 13*L,4, cero_y)   # 55 
ret.agregar_nodo(cero_x + 14*L,4, cero_y)   # 56 
ret.agregar_nodo(cero_x + 15*L,4, cero_y)   # 57 
ret.agregar_nodo(cero_x + 16*L,4, cero_y)   # 58 
ret.agregar_nodo(cero_x + 17*L,4, cero_y)   # 59 
ret.agregar_nodo(cero_x + 18*L,4, cero_y)   # 60 
ret.agregar_nodo(cero_x + 19*L,4, cero_y)   # 61 
ret.agregar_nodo(cero_x + 20*L,4, cero_y)   # 62 

ret.agregar_nodo(cero_x,4, cero_y + L)         # 63
ret.agregar_nodo(cero_x + 1*L,4, cero_y + L)   # 64
ret.agregar_nodo(cero_x + 2*L,4, cero_y + L)   # 65
ret.agregar_nodo(cero_x + 3*L,4, cero_y + L)   # 66
ret.agregar_nodo(cero_x + 4*L,4, cero_y + L)   # 67
ret.agregar_nodo(cero_x + 5*L,4, cero_y + L)   # 68
ret.agregar_nodo(cero_x + 6*L,4, cero_y + L)   # 69
ret.agregar_nodo(cero_x + 7*L,4, cero_y + L)   # 70
ret.agregar_nodo(cero_x + 8*L,4, cero_y + L)   # 71
ret.agregar_nodo(cero_x + 9*L,4, cero_y + L)   # 72
ret.agregar_nodo(cero_x + 10*L,4, cero_y + L)  # 73
ret.agregar_nodo(cero_x + 11*L,4, cero_y + L)  # 74
ret.agregar_nodo(cero_x + 12*L,4, cero_y + L)  # 75
ret.agregar_nodo(cero_x + 13*L,4, cero_y + L)  # 76
ret.agregar_nodo(cero_x + 14*L,4, cero_y + L)  # 77
ret.agregar_nodo(cero_x + 15*L,4, cero_y + L)  # 78
ret.agregar_nodo(cero_x + 16*L,4, cero_y + L)  # 79
ret.agregar_nodo(cero_x + 17*L,4, cero_y + L)  # 80
ret.agregar_nodo(cero_x + 18*L,4, cero_y + L)  # 81
ret.agregar_nodo(cero_x + 19*L,4, cero_y + L)  # 82
ret.agregar_nodo(cero_x + 20*L,4, cero_y + L)  # 83



#Secciones de las barras
seccion_grande = SeccionICHA("[]350x150x37.8", color="#3A8431")#, debug=True)
seccion_chica = SeccionICHA("[]80x40x8", color="#A3500B")
seccion_chica = seccion_grande

# chacra
seccion_chica = SeccionICHA("H1100x350x400.4", color="#3A8431")#, debug=True)
seccion_chica = SeccionICHA("H350x200x99.5", color="#3A8431")#, debug=True)
# seccion_chica = SeccionICHA("H400x250x69.6", color="#3A8431")#, debug=True)


#Crear y agregar las barras
ret.agregar_barra(Barra(0, 1, seccion_chica))   #0
ret.agregar_barra(Barra(1, 2, seccion_chica))   #1
ret.agregar_barra(Barra(2, 3, seccion_chica))   #2
ret.agregar_barra(Barra(3, 4, seccion_chica))   #3
ret.agregar_barra(Barra(4, 5, seccion_chica))   #4
ret.agregar_barra(Barra(5, 6, seccion_chica))   #5
ret.agregar_barra(Barra(6, 7, seccion_chica))   #6
ret.agregar_barra(Barra(7, 8, seccion_chica))   #7
ret.agregar_barra(Barra(8, 9, seccion_chica))   #8
ret.agregar_barra(Barra(9, 10, seccion_chica))  #9
ret.agregar_barra(Barra(10, 11, seccion_chica)) #10
ret.agregar_barra(Barra(11, 12, seccion_chica)) #11
ret.agregar_barra(Barra(12, 13, seccion_chica)) #12
ret.agregar_barra(Barra(13, 14, seccion_chica)) #13
ret.agregar_barra(Barra(14, 15, seccion_chica)) #14
ret.agregar_barra(Barra(15, 16, seccion_chica)) #15
ret.agregar_barra(Barra(16, 17, seccion_chica)) #16
ret.agregar_barra(Barra(17, 18, seccion_chica)) #17
ret.agregar_barra(Barra(18, 19, seccion_chica)) #18
ret.agregar_barra(Barra(19, 20, seccion_chica)) #19


ret.agregar_barra(Barra(21, 22, seccion_chica)) #20
ret.agregar_barra(Barra(22, 23, seccion_chica)) #21
ret.agregar_barra(Barra(23, 24, seccion_chica)) #22
ret.agregar_barra(Barra(24, 25, seccion_chica)) #23
ret.agregar_barra(Barra(25, 26, seccion_chica)) #24
ret.agregar_barra(Barra(26, 27, seccion_chica)) #25
ret.agregar_barra(Barra(27, 28, seccion_chica)) #26
ret.agregar_barra(Barra(28, 29, seccion_chica)) #27
ret.agregar_barra(Barra(29, 30, seccion_chica)) #28
ret.agregar_barra(Barra(30, 31, seccion_chica)) #29
ret.agregar_barra(Barra(31, 32, seccion_chica)) #30
ret.agregar_barra(Barra(32, 33, seccion_chica)) #31
ret.agregar_barra(Barra(33, 34, seccion_chica)) #32
ret.agregar_barra(Barra(34, 35, seccion_chica)) #33
ret.agregar_barra(Barra(35, 36, seccion_chica)) #34
ret.agregar_barra(Barra(36, 37, seccion_chica)) #35
ret.agregar_barra(Barra(37, 38, seccion_chica)) #36
ret.agregar_barra(Barra(38, 39, seccion_chica)) #37
ret.agregar_barra(Barra(39, 40, seccion_chica)) #38
ret.agregar_barra(Barra(40, 41, seccion_chica)) #39


# triangulos


ret.agregar_barra(Barra(0, 22, seccion_chica)) #40
ret.agregar_barra(Barra(2, 24, seccion_chica)) #41
ret.agregar_barra(Barra(4, 26, seccion_chica)) #42
ret.agregar_barra(Barra(6, 28, seccion_chica)) #43
ret.agregar_barra(Barra(8, 30, seccion_chica)) #44
ret.agregar_barra(Barra(10, 32, seccion_chica)) #45
ret.agregar_barra(Barra(12, 34, seccion_chica)) #46
ret.agregar_barra(Barra(14, 36, seccion_chica)) #39
ret.agregar_barra(Barra(16, 38, seccion_chica)) #39
ret.agregar_barra(Barra(18, 40, seccion_chica)) #39
ret.agregar_barra(Barra(22, 2, seccion_chica)) #39
ret.agregar_barra(Barra(24, 4, seccion_chica)) #39
ret.agregar_barra(Barra(26, 6, seccion_chica)) #39
ret.agregar_barra(Barra(28, 8, seccion_chica)) #39
ret.agregar_barra(Barra(30, 10, seccion_chica)) #39
ret.agregar_barra(Barra(32, 12, seccion_chica)) #39
ret.agregar_barra(Barra(34, 14, seccion_chica)) #39
ret.agregar_barra(Barra(36, 16, seccion_chica)) #39
ret.agregar_barra(Barra(38, 18, seccion_chica)) #39
ret.agregar_barra(Barra(40, 20, seccion_chica)) #60

# verticales

ret.agregar_barra(Barra(0, 21, seccion_chica))   #0
ret.agregar_barra(Barra(1, 22, seccion_chica))   #1
ret.agregar_barra(Barra(2, 23, seccion_chica))   #2
ret.agregar_barra(Barra(3, 24, seccion_chica))   #3
ret.agregar_barra(Barra(4, 25, seccion_chica))   #4
ret.agregar_barra(Barra(5, 26, seccion_chica))   #5
ret.agregar_barra(Barra(6, 27, seccion_chica))   #6
ret.agregar_barra(Barra(7, 28, seccion_chica))   #7
ret.agregar_barra(Barra(8, 29, seccion_chica))   #8
ret.agregar_barra(Barra(9, 30, seccion_chica))  #9
ret.agregar_barra(Barra(10, 31, seccion_chica)) #10
ret.agregar_barra(Barra(11, 32, seccion_chica)) #11
ret.agregar_barra(Barra(12, 33, seccion_chica)) #12
ret.agregar_barra(Barra(13, 34, seccion_chica)) #13
ret.agregar_barra(Barra(14, 35, seccion_chica)) #14
ret.agregar_barra(Barra(15, 36, seccion_chica)) #15
ret.agregar_barra(Barra(16, 37, seccion_chica)) #16
ret.agregar_barra(Barra(17, 38, seccion_chica)) #17
ret.agregar_barra(Barra(18, 39, seccion_chica)) #18
ret.agregar_barra(Barra(19, 40, seccion_chica)) #19
ret.agregar_barra(Barra(20, 41, seccion_chica)) #80


## otro marco ##

ret.agregar_barra(Barra(42, 43, seccion_chica)) #20
ret.agregar_barra(Barra(43, 44, seccion_chica)) #21
ret.agregar_barra(Barra(44, 45, seccion_chica)) #22
ret.agregar_barra(Barra(45, 46, seccion_chica)) #23
ret.agregar_barra(Barra(46, 47, seccion_chica)) #24
ret.agregar_barra(Barra(47, 48, seccion_chica)) #25
ret.agregar_barra(Barra(48, 49, seccion_chica)) #26
ret.agregar_barra(Barra(49, 50, seccion_chica)) #27
ret.agregar_barra(Barra(50, 51, seccion_chica)) #28
ret.agregar_barra(Barra(51, 52, seccion_chica)) #29
ret.agregar_barra(Barra(52, 53, seccion_chica)) #30
ret.agregar_barra(Barra(53, 54, seccion_chica)) #31
ret.agregar_barra(Barra(54, 55, seccion_chica)) #32
ret.agregar_barra(Barra(55, 56, seccion_chica)) #33
ret.agregar_barra(Barra(56, 57, seccion_chica)) #34
ret.agregar_barra(Barra(57, 58, seccion_chica)) #35
ret.agregar_barra(Barra(58, 59, seccion_chica)) #36
ret.agregar_barra(Barra(59, 60, seccion_chica)) #37
ret.agregar_barra(Barra(60, 61, seccion_chica)) #38
ret.agregar_barra(Barra(61, 62, seccion_chica)) #100


ret.agregar_barra(Barra(63, 64, seccion_chica)) #20
ret.agregar_barra(Barra(64, 65, seccion_chica)) #21
ret.agregar_barra(Barra(65, 66, seccion_chica)) #22
ret.agregar_barra(Barra(66, 67, seccion_chica)) #23
ret.agregar_barra(Barra(67, 68, seccion_chica)) #24
ret.agregar_barra(Barra(68, 69, seccion_chica)) #25
ret.agregar_barra(Barra(69, 70, seccion_chica)) #26
ret.agregar_barra(Barra(70, 71, seccion_chica)) #27
ret.agregar_barra(Barra(71, 72, seccion_chica)) #28
ret.agregar_barra(Barra(72, 73, seccion_chica)) #29
ret.agregar_barra(Barra(73, 74, seccion_chica)) #30
ret.agregar_barra(Barra(74, 75, seccion_chica)) #31
ret.agregar_barra(Barra(75, 76, seccion_chica)) #32
ret.agregar_barra(Barra(76, 77, seccion_chica)) #33
ret.agregar_barra(Barra(77, 78, seccion_chica)) #34
ret.agregar_barra(Barra(78, 79, seccion_chica)) #35
ret.agregar_barra(Barra(79, 80, seccion_chica)) #36
ret.agregar_barra(Barra(80, 81, seccion_chica)) #37
ret.agregar_barra(Barra(81, 82, seccion_chica)) #38
ret.agregar_barra(Barra(82, 83, seccion_chica)) #39


# triangulos


ret.agregar_barra(Barra(42, 64, seccion_chica)) #39
ret.agregar_barra(Barra(44, 66, seccion_chica)) #39
ret.agregar_barra(Barra(46, 68, seccion_chica)) #39
ret.agregar_barra(Barra(48, 70, seccion_chica)) #39
ret.agregar_barra(Barra(50, 72, seccion_chica)) #39
ret.agregar_barra(Barra(52, 74, seccion_chica)) #39
ret.agregar_barra(Barra(54, 76, seccion_chica)) #39
ret.agregar_barra(Barra(56, 78, seccion_chica)) #39
ret.agregar_barra(Barra(58, 80, seccion_chica)) #39
ret.agregar_barra(Barra(60, 82, seccion_chica)) #39
ret.agregar_barra(Barra(64, 44, seccion_chica)) #39
ret.agregar_barra(Barra(66, 46, seccion_chica)) #39
ret.agregar_barra(Barra(68, 48, seccion_chica)) #39
ret.agregar_barra(Barra(70, 50, seccion_chica)) #39
ret.agregar_barra(Barra(72, 52, seccion_chica)) #39
ret.agregar_barra(Barra(74, 54, seccion_chica)) #39
ret.agregar_barra(Barra(76, 56, seccion_chica)) #39
ret.agregar_barra(Barra(78, 58, seccion_chica)) #39
ret.agregar_barra(Barra(80, 60, seccion_chica)) #39
ret.agregar_barra(Barra(82, 62, seccion_chica)) #39



# verticales

ret.agregar_barra(Barra(42, 63, seccion_chica)) #20
ret.agregar_barra(Barra(43, 64, seccion_chica)) #21
ret.agregar_barra(Barra(44, 65, seccion_chica)) #22
ret.agregar_barra(Barra(45, 66, seccion_chica)) #23
ret.agregar_barra(Barra(46, 67, seccion_chica)) #24
ret.agregar_barra(Barra(47, 68, seccion_chica)) #25
ret.agregar_barra(Barra(48, 69, seccion_chica)) #26
ret.agregar_barra(Barra(49, 70, seccion_chica)) #27
ret.agregar_barra(Barra(50, 71, seccion_chica)) #28
ret.agregar_barra(Barra(51, 72, seccion_chica)) #29
ret.agregar_barra(Barra(52, 73, seccion_chica)) #30
ret.agregar_barra(Barra(53, 74, seccion_chica)) #31
ret.agregar_barra(Barra(54, 75, seccion_chica)) #32
ret.agregar_barra(Barra(55, 76, seccion_chica)) #33
ret.agregar_barra(Barra(56, 77, seccion_chica)) #34
ret.agregar_barra(Barra(57, 78, seccion_chica)) #35
ret.agregar_barra(Barra(58, 79, seccion_chica)) #36
ret.agregar_barra(Barra(59, 80, seccion_chica)) #37
ret.agregar_barra(Barra(60, 81, seccion_chica)) #38
ret.agregar_barra(Barra(61, 82, seccion_chica)) #39
ret.agregar_barra(Barra(62, 83, seccion_chica)) #39



## union entre marcos


ret.agregar_barra(Barra(0, 42, seccion_chica))   #0
ret.agregar_barra(Barra(1, 43, seccion_chica))   #1
ret.agregar_barra(Barra(2, 44, seccion_chica))   #2
ret.agregar_barra(Barra(3, 45, seccion_chica))   #3
ret.agregar_barra(Barra(4, 46, seccion_chica))   #4
ret.agregar_barra(Barra(5, 47, seccion_chica))   #5
ret.agregar_barra(Barra(6, 48, seccion_chica))   #6
ret.agregar_barra(Barra(7, 49, seccion_chica))   #7
ret.agregar_barra(Barra(8, 50, seccion_chica))   #8
ret.agregar_barra(Barra(9, 51, seccion_chica))  #9
ret.agregar_barra(Barra(10, 52, seccion_chica)) #10
ret.agregar_barra(Barra(11, 53, seccion_chica)) #11
ret.agregar_barra(Barra(12, 54, seccion_chica)) #12
ret.agregar_barra(Barra(13, 55, seccion_chica)) #13
ret.agregar_barra(Barra(14, 56, seccion_chica)) #14
ret.agregar_barra(Barra(15, 57, seccion_chica)) #15
ret.agregar_barra(Barra(16, 58, seccion_chica)) #16
ret.agregar_barra(Barra(17, 59, seccion_chica)) #17
ret.agregar_barra(Barra(18, 60, seccion_chica)) #18
ret.agregar_barra(Barra(19, 61, seccion_chica)) #19
ret.agregar_barra(Barra(20, 62, seccion_chica)) #19



ret.agregar_barra(Barra(21, 63, seccion_chica)) #20
ret.agregar_barra(Barra(22, 64, seccion_chica)) #20
ret.agregar_barra(Barra(23, 65, seccion_chica)) #21
ret.agregar_barra(Barra(24, 66, seccion_chica)) #22
ret.agregar_barra(Barra(25, 67, seccion_chica)) #23
ret.agregar_barra(Barra(26, 68, seccion_chica)) #24
ret.agregar_barra(Barra(27, 69, seccion_chica)) #25
ret.agregar_barra(Barra(28, 70, seccion_chica)) #26
ret.agregar_barra(Barra(29, 71, seccion_chica)) #27
ret.agregar_barra(Barra(30, 72, seccion_chica)) #28
ret.agregar_barra(Barra(31, 73, seccion_chica)) #29
ret.agregar_barra(Barra(32, 74, seccion_chica)) #30
ret.agregar_barra(Barra(33, 75, seccion_chica)) #31
ret.agregar_barra(Barra(34, 76, seccion_chica)) #32
ret.agregar_barra(Barra(35, 77, seccion_chica)) #33
ret.agregar_barra(Barra(36, 78, seccion_chica)) #34
ret.agregar_barra(Barra(37, 79, seccion_chica)) #35
ret.agregar_barra(Barra(38, 80, seccion_chica)) #36
ret.agregar_barra(Barra(39, 81, seccion_chica)) #37
ret.agregar_barra(Barra(40, 82, seccion_chica)) #38
ret.agregar_barra(Barra(41, 83, seccion_chica)) #39


## diagonales inferiores

ret.agregar_barra(Barra(0, 43, seccion_chica))   #0
ret.agregar_barra(Barra(1, 44, seccion_chica))   #1
ret.agregar_barra(Barra(2, 45, seccion_chica))   #2
ret.agregar_barra(Barra(3, 46, seccion_chica))   #3
ret.agregar_barra(Barra(4, 47, seccion_chica))   #4
ret.agregar_barra(Barra(5, 48, seccion_chica))   #5
ret.agregar_barra(Barra(6, 49, seccion_chica))   #6
ret.agregar_barra(Barra(7, 50, seccion_chica))   #7
ret.agregar_barra(Barra(8, 51, seccion_chica))   #8
ret.agregar_barra(Barra(9, 52, seccion_chica))  #9
ret.agregar_barra(Barra(10, 53, seccion_chica)) #10
ret.agregar_barra(Barra(11, 54, seccion_chica)) #11
ret.agregar_barra(Barra(12, 55, seccion_chica)) #12
ret.agregar_barra(Barra(13, 56, seccion_chica)) #13
ret.agregar_barra(Barra(14, 57, seccion_chica)) #14
ret.agregar_barra(Barra(15, 58, seccion_chica)) #15
ret.agregar_barra(Barra(16, 59, seccion_chica)) #16
ret.agregar_barra(Barra(17, 60, seccion_chica)) #17
ret.agregar_barra(Barra(18, 61, seccion_chica)) #18
ret.agregar_barra(Barra(19, 62, seccion_chica)) #19

## diagonales superiores


ret.agregar_barra(Barra(21, 64, seccion_chica)) #20
ret.agregar_barra(Barra(22, 65, seccion_chica)) #20
ret.agregar_barra(Barra(23, 66, seccion_chica)) #21
ret.agregar_barra(Barra(24, 67, seccion_chica)) #22
ret.agregar_barra(Barra(25, 68, seccion_chica)) #23
ret.agregar_barra(Barra(26, 69, seccion_chica)) #24
ret.agregar_barra(Barra(27, 70, seccion_chica)) #25
ret.agregar_barra(Barra(28, 71, seccion_chica)) #26
ret.agregar_barra(Barra(29, 72, seccion_chica)) #27
ret.agregar_barra(Barra(30, 73, seccion_chica)) #28
ret.agregar_barra(Barra(31, 74, seccion_chica)) #29
ret.agregar_barra(Barra(32, 75, seccion_chica)) #30
ret.agregar_barra(Barra(33, 76, seccion_chica)) #31
ret.agregar_barra(Barra(34, 77, seccion_chica)) #32
ret.agregar_barra(Barra(35, 78, seccion_chica)) #33
ret.agregar_barra(Barra(36, 79, seccion_chica)) #34
ret.agregar_barra(Barra(37, 80, seccion_chica)) #35
ret.agregar_barra(Barra(38, 81, seccion_chica)) #36
ret.agregar_barra(Barra(39, 82, seccion_chica)) #37
ret.agregar_barra(Barra(40, 83, seccion_chica)) #38


##  RESTRICCIONES  ##



ret.agregar_restriccion(0, 0, 0)
ret.agregar_restriccion(0, 1, 0)
ret.agregar_restriccion(0, 2, 0)
ret.agregar_restriccion(20, 0, 0)
ret.agregar_restriccion(20, 2, 0)
# ret.agregar_restriccion(10, 2, 0)

ret.agregar_restriccion(42, 0, 0)
ret.agregar_restriccion(42, 1, 0)
ret.agregar_restriccion(42, 2, 0)
ret.agregar_restriccion(62, 0, 0)
ret.agregar_restriccion(62, 2, 0)
# ret.agregar_restriccion(32, 2, 0)



#Visualizar y comprobar las secciones
opciones_barras = {
	# "ver_secciones_en_barras": True,
	"color_barras_por_seccion": True,
}
ver_reticulado_3d(ret,opciones_barras=opciones_barras)

# exit(0)



#Resolver el problema peso_propio
ret.ensamblar_sistema(factor_peso_propio=[0.,0.,-1.], factor_cargas=0.0)
ret.resolver_sistema()
f_D = ret.obtener_fuerzas()

q = 400*kgf_/m_**2

F = 4*L*q

#Agregar fuerzas tablero

for i in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61]:
	ret.agregar_fuerza(i, 2, -F/2)

ret.agregar_fuerza(0, 2, -F/4)
ret.agregar_fuerza(20, 2, -F/4)
ret.agregar_fuerza(42, 2, -F/4)
ret.agregar_fuerza(62, 2, -F/4)


#Resolver el problema peso_propio
ret.ensamblar_sistema(factor_peso_propio=[0.,0.,0], factor_cargas=1.0)
ret.resolver_sistema()
f_L = ret.obtener_fuerzas()



#Visualizar f_L en el reticulado
opciones_nodos = {
	"usar_posicion_deformada": False,
}

opciones_barras = {
	"color_barras_por_dato": True,
	"ver_dato_en_barras" : True,
	"dato":f_L
}

ver_reticulado_3d(ret, 
	opciones_nodos=opciones_nodos, 
	opciones_barras=opciones_barras,
	titulo="Carga Viva")


#Visualizar f_L en el reticulado
opciones_nodos = {
	"usar_posicion_deformada": False,
}

opciones_barras = {
	"color_barras_por_dato": True,
	"ver_dato_en_barras" : True,
	"dato":f_D
}

ver_reticulado_3d(ret, 
	opciones_nodos=opciones_nodos, 
	opciones_barras=opciones_barras,
	titulo="Carga Muerta")


#Calcular carga ultima (con factores de mayoracion)
fu = 1.2*f_D + 1.6*f_L



#Visualizar combinacion en el reticulado
opciones_nodos = {
	"usar_posicion_deformada": False,
}

opciones_barras = {
	"color_barras_por_dato": True,
	"ver_dato_en_barras" : True,
	"dato":fu
}

ver_reticulado_3d(ret, 
	opciones_nodos=opciones_nodos, 
	opciones_barras=opciones_barras,
	titulo="1.2D + 1.6L")





cumple = ret.chequear_diseño(fu, ϕ=0.9)

if cumple:
	print(":)  El reticulado cumple todos los requisitos")
else:
	print(":(  El reticulado NO cumple todos los requisitos")

#Calcular factor de utilizacion para las barras
factores_de_utilizacion = ret.obtener_factores_de_utilizacion(fu, ϕ=0.9)


#Visualizar FU en el reticulado
opciones_nodos = {
	"usar_posicion_deformada": False,
	# "factor_amplificacion_deformada": 1.,
}

opciones_barras = {
	"color_barras_por_dato": True,
	"ver_dato_en_barras" : True,
	"dato":factores_de_utilizacion
}


ver_reticulado_3d(ret, 
	opciones_nodos=opciones_nodos, 
	opciones_barras=opciones_barras,
	titulo="Factor Utilizacion")


ret.guardar("Grupo_06.h5")

print (f"Peso Total: {ret.calcular_peso_total()} kg")
print (f"Peso Total: {ret.calcular_peso_total()/1000} ton")