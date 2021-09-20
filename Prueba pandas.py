import pandas as pd
from secciones import SeccionICHA
#nombre="PH400x400x225.7"
#nombre2=nombre.split("1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9")
#print(nombre2)

#df=pd.read_excel("Perfiles ICHA.xlsx")
#print(df.head(15))
#df2=pd.read_excel("Perfiles ICHA.xlsx",sheet_name="PH")
#df2=df2.replace(to_replace="×", value="x")
#
#print(df2.head(17))
#print(df2.iloc[13])
#loc=0
#for i in range(len(df2.index)):
#    a=(str(df2.iloc[i][0])+str(df2.iloc[i][1])+str(df2.iloc[i][2])+str(df2.iloc[i][3])+str(df2.iloc[i][4])+str(df2.iloc[i][5]))
#    #print(a)
#    if str(a)==nombre:
#        loc=i
#        break
#    
#print(i)
#print(df2.iloc[i])
#
#A="2"
#if A=="1" or A=="2":
#    print("hi")
sec1 = SeccionICHA("[s]400x200x45.6",base_datos="Perfiles ICHA.xlsx")
print(sec1.area())
print(sec1.peso())
print(sec1.inercia_xx())
print(sec1.inercia_yy())
a=["1","2","3","4","5","6","7","8","9"]