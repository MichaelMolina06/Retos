###CDT en Python

Problema
-------------
**Descripción del problema:** Una entidad Bancaria o entidad financiera, requiere calcular el valor de los intereses ganados y el total final de dinero para diferentes clientes, de acuerdo, a una cantidad de dinero invertida en un CDT. Un CDT por su parte, es un producto financiero que ofrece la posibilidad de guardar dinero durante un tiempo determinado para recibir posteriormente sus intereses devengados, asimismo, ofrece rendimientos a una tasa fija, asegurando una rentabilidad libre de riesgo en un tiempo determinado que por lo general debe ser mayor a dos (2) meses. Si, este dinero se retira antes de este periodo se aplica una penalidad del 2%.

En ese sentido, el valor de los intereses ganados por un periodo de tiempo superior a dos meses se determina a través de la siguiente formula:

![](https://i.imgur.com/XkcsT0z.png)

Donde:
- Cantidad = dinero ingresado en el CDT
- Porcentaje_interes = 3% (0.03).
- Tiempo = cantidad de tiempo

En consecuencia, el valor total del dinero será calculado a través de la siguiente formula:

![](https://i.imgur.com/wY6EdHl.png)

Se debe determinar el valor total a retirar por el cliente que invirtió en el CDT al final del periodo.

Por otra parte, para un periodo de tiempo inferior o igual a dos meses se debe aplicar la siguiente formula:

![](https://i.imgur.com/ADjUZZs.png)

Donde:
- Cantidad = dinero ingresado en el CDT
- Porcentaje a perder = 2% (0.02)

En consecuencia, el valor total del dinero será calculado a través de la siguiente formula:

![](https://i.imgur.com/TiN7962.png)

Reto
-------------
Para responder a este planteamiento, escriba una función que reciba como parámetros: una cadena con el usuario del cliente como dato alfanumérico, el capital aportado y el tiempo del CDT y, en consecuencia, retorne una cadena de caracteres que le proporcione al banco la información que desea obtener.
