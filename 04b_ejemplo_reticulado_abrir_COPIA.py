from reticulado import Reticulado
from graficar3d import ver_reticulado_3d

#Inicializar modelo
ret = Reticulado()

ret.abrir("Grupo_06.h5")

#Visualizar y comprobar las secciones
ret.ensamblar_sistema(factor_peso_propio=[0.,0.,-1.], factor_cargas=0.0)
ret.resolver_sistema()
f_D = ret.obtener_fuerzas()

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



print (ret)


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

print (f"Peso Total: {ret.calcular_peso_total()} kg")
print (f"Peso Total: {ret.calcular_peso_total()/1000} ton")