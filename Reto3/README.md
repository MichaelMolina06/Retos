### Aventuras Extremas (AE)

Problema
-------------
En el parque de diversiones "AE" se requiere implementar una funcion en la cual reciba como parametro un diccionario, el cual va a tener las variables que a continuacion se muestran:

![](https://i.imgur.com/QrgDoT3.png)

En la siguiente tabla se muestra la atraccion y el valor de la boleta para cada una de ellas, en la cual los clientes podran ingresar dependiendo de su edad, posteriormente el parque de atracciones ha decidido otorgar un descuento al valor de la boleta si cumple con el rango de edad y es la primera vez que el cliente ingresa.

![](https://i.imgur.com/5nxx2R5.png)

Reto
-------------
La función debe retornar un nuevo diccionario con las llaves nombre, edad, atracción, primer_ingreso, total_boleta y apto del cliente:

- En donde apto tendrá como valor una variable booleana, será verdadera si su edad cumple con los rangos exigidos en la tabla anterior, en el caso contrario será falsa.
- En el caso de atraccion y total_boleta, si no se cumple el rango de edades se le asignara un valor de ‘N/A’ a cada uno.
- Si primer_ingreso es verdadero, el total_boleta será el valor de la boleta menos el descuento de lo contrario se pagará el valor neto de la boleta.

![](https://i.imgur.com/qmLdPf4.png)

**Ejemplo:**

![](https://i.imgur.com/FzZhyKE.png)
