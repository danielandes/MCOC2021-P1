from secciones import SeccionICHA

sec1 = SeccionICHA("H1100x350x400.4",base_datos="Perfiles ICHA.xlsx")
print(sec1)

sec2 = SeccionICHA("H1100x350x400.",base_datos="Perfiles ICHA.xlsx")
print(sec2)

sec3 = SeccionICHA("HR1118x405x517.7",base_datos="Perfiles ICHA.xlsx")
print(sec3)

sec4 = SeccionICHA("cR1118x405x517.7",base_datos="Perfiles ICHA.xlsx")
print(sec4)

sec5 = SeccionICHA("O1624,1600,12",base_datos="Perfiles ICHA.xlsx")
print(sec5)

sec6 = SeccionICHA("o12.7,10.9,0.9",base_datos="Perfiles ICHA.xlsx")
print(sec6)