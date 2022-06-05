### Consultor Cinematografico

Problema
-------------

Como consultor en recursos cinematográficos se le ha solicitado que organice la información necesaria que contenga:

**Entrada:**

![](https://i.imgur.com/pB7rwzG.png)

Esto, con el fin de conocer los recursos que han salido de nuestro suelo y, en consecuencia, tomar en un futuro próximo la decisión de contratar recursos locales e iniciar la reactivación económica producto de la crisis pandémica

En adición, usted cuenta con el archivo de datos *"movies.csv"* disponible desde:

https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true

En ese sentido, escriba una función que contenga la ruta de este archivo (descrita arriba) para su consulta y/o manipulación. A partir de estos datos, utilice los métodos *pd.read_csv()* y *pivot_table()* y cualquier otro método que ud. necesite para importar los datos del archivo .csv y crear una tabla dinámica en base a los datos solicitados, finalmente, mostrar los resultados finales.

**Salida:**

![](https://i.imgur.com/UTogaDt.png)

![](https://i.imgur.com/X0t1IWq.png)
**Figura 1: Tabla resultados (Solo 10 registros del total)**

**Esqueleto:**

![](https://i.imgur.com/0ykV46O.png)

**Valide:**
Que la extensión del nombre del archivo sea de tipo *"csv"*. En caso contrario, retorne la siguiente cadena: *"Extensión inválida"*. Utilice un bloque *try* except para leer el archivo. En caso de *error*, retorne la siguiente cadena: *"Error al leer el archivo de datos."*
Resultado pruebas:

Tenga en cuenta las siguientes consideraciones:

- Debe crear un subconjunto del dataframe (Figura 3) con las columnas "*Country*", "*Language*" y "*Gross Earnings*". Seguidamente, usar las columnas "*Country*" y "*Language*" como índice para la tabla dinámica y "*Gross Earnings*" (Figura 1) como tabla de resumen.

![](https://i.imgur.com/LHU1O5q.png)
**Figura 3: Subconjunto del dataframe**
