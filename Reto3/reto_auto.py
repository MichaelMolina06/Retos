def consultaRegistro(ventas, idproducto):
    registro = 0
    for i in ventas:
        if idproducto in i:
            print("Producto consultado :  " + str(idproducto) + "  Descripción  " + i[1] + "  #Parte  " + str(i[2]) + " Cantidad vendida  " + str(i[3]) + "  Stock  " + str(i[4]) + "  Comprador " + i[5] + "  Documento  " + str(i[6]) + "  Fecha Venta  " + str(i[7]))
            registro = 1

    if registro == 0:
        print("No hay registro de venta de ese producto") 
    return ""

def AutoPartes(ventas: list):
    lista = list(ventas) 
    return lista

def run():
    print(consultaRegistro(AutoPartes([
        (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
        (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
        (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
        (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
        (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]), 2010))

if __name__ == '__main__':
    run()