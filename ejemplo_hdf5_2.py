from matplotlib.pylab import *
import h5py

fid = h5py.File("04a_ejemplo_reticulado_guardar.h5", "r")


# for i in fid["cargas_val"]:
# 	print (i)


# valor = fid["cargas_val"][0]

# print (double(valor))

# for i in range(10):
# 	valor_r = double(fid["restricciones_val"][i])
# 	print (valor_r)
cont_2=0
for i in fid["restricciones"]:
    valor = double(fid["restricciones_val"][cont_2])
    # ret.agregar_fuerza(i[0],i[1],valor)
    print (i[0],i[1],valor)
    cont_2 += 1

for i in fid["xyz"]:
    #ret.agregar_nodo(i[0],i[1],i[2])
    print(i[0],i[1],i[2])






# A = fid["barras"][:, :]

#print(A)