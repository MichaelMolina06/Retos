def consultaRegistro(ventas, idproducto):
    contador = 0
    for x in ventas:
        if idproducto in x:
            print("Producto consultado : {}  Descripción  {}  #Parte  {}  Cantidad vendida  {}  Stock  {}  Comprador {}  Documento  {}  Fecha Venta  {}"
                    .format(idproducto,x[1],x[2],x[3],x[4],x[5],x[6],x[7]))
            contador = 1
    if contador == 0:
        print("No hay registro de venta de ese producto") 
    return ""

def AutoPartes(ventas: list):
    lista = list(ventas) 
    return lista

print()

def run():
    consultaRegistro(AutoPartes([
        (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
        (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
        (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
        (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
        (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]), 2010)

if __name__ == '__main__':
    run()