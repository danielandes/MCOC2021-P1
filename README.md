# MCOC2021-P1
Optimización estructural de un puente reticular

![ICHA](https://user-images.githubusercontent.com/88337429/134083833-9b90e7d3-7a1f-4a25-a72f-d368fc45e38d.PNG)

INFORME 

Primer Diseño 
* Inicialmente para el diseño se consideraron como apoyos solo los 2 obligatorios, con barras uniendo estos dos puntos de forma horizontal. Donde luego se trazaron triangulos entre los nodos. Sin embargo este sistema generaba un mecanismo, por lo que añadimos barras verticales en todos los nodos y ademas para unir las dos caras del puente se consideraron barras diagonales. Este diseño es bastante simple, probamos con diversos tipos de secciones, en muchos las barras no resistian. Luego con la seccion H350x200x99.5 se obtuvo un puente funcional con un peso de 149367.0055377983 kg. 
* Se modifico el codigo para obtener los factores de uso como (Fu/(ϕ*Fn)*100 en %, de donde se obtuvo que las barras sometidas a mayores esfuerzos fueron las horizontales (azules), especialmente las superiores, llegando a encontrarse bajo un 81.62% de uso en el medio del puente, mientras que algunas barras diagonales (rojas) alcanzan un 19.62% de uso y otras barras no superan el 5%, dando gran espacio para optimizar el peso.

* Al observar los desplazamientos se obtiene que las deformaciones mas altas ocurren en la direccion "z", con sus desplazamientos mas altos entre -0.21 y -0.29, mientras que los desplazamientos en "x" e "y" raramente superan 0.01

Segundo Diseño
* Se conservó la geometria del reticulado, se cambiaron las secciones en base a los factores de utilizacion de las barras segun su posición. Se reducieron las secciones para asi aprovechar al máximo el acero logrando reducir el peso considerablemente casi a una tercera parte del diseño incial. 
* Se realizaron modificaciones de acuerdo a los usos del primer diseño para optimizar, logrando un uso maximo de 92.7% en las barras horizontales (azules) superiores, 81,79% maximo en las barras diagonales (rojas) y en general un mejor aprovechamiento de las resistencias de los materiales, sin embargo aun existen barras con usos menores al 1% las cuales no se pueden eliminar ya que generarian un mecanismo, por lo que se decidio darles secciones pequeñas pero realistas de acuerdo a las dimensiones de la estructura.
* A medida que se optimizo el peso alcanzando mayores utilizaciones del material aumentaron las deformaciones, con el eje "y" presentando desplazamientos entre 3.4 y 3.56 en los casos mas extremos, mientras que el eje "x" son las mas altas entre 0.35 y 0.45, y en el eje "z" las mas altas se encuentran entre 0.35 y 0.4

Resultando en las siguientes secciones para las diferentes barras.
- Barras horizontales: H350x200x81.1 (azules)
- Barras diagonales: []350x150x23 (rojas)
- Barras verticales: []250x100x10.8 (amarillas)
- Barras: que unen las caras: []100x50x6.5 (verdes)
- Se llegó a un peso final de 56047.560906224804 kg

![](https://github.com/VicenteOtaegui/MCOC2021-P1/blob/main/Puente_colores.png)




