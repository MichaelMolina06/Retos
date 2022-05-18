def AutoPartes(ventas: list):
    diccionario = {
        'idProducto'   : tuple(()),  #Identificador único del producto
        'dProducto'    : tuple(()),  #Descripción del producto
        'pnProducto'   : tuple(()),  #Numero de parte del producto
        'cvProducto'   : tuple(()),  #Cantidad vendida del producto
        'sProducto'    : tuple(()),  #Stock del producto
        'nComprador'   : tuple(()),  #Nombre del comprador
        'cComprador'   : tuple(()),  #Documento de identidad del comprador
        'fVenta'       : tuple(()),  #Fecha de venta del producto
    }
    idProductoa = []
    dProductoa = []
    pnProductoa = []
    cvProductoa = []
    sProductoa = []
    nCompradora = []
    cCompradora = []
    dfVentaa = []
    
    contador = 0
    for x in ventas:
        idProductoa.insert(contador,x[0])
        dProductoa.insert(contador,x[1])
        pnProductoa.insert(contador,x[2])
        cvProductoa.insert(contador,x[3])
        sProductoa.insert(contador,x[4])
        nCompradora.insert(contador,x[5])
        cCompradora.insert(contador,x[6])
        dfVentaa.insert(contador,x[7])
        contador = contador +1

    diccionario['idProducto'] = tuple(idProductoa)
    diccionario['dProducto'] = tuple(dProductoa)
    diccionario['pnProducto'] = tuple(pnProductoa)
    diccionario['cvProducto'] = tuple(cvProductoa)
    diccionario['sProducto'] = tuple(sProductoa)
    diccionario['nComprador'] = tuple(nCompradora)
    diccionario['cComprador'] = tuple(cCompradora)
    diccionario['fVenta'] = tuple(dfVentaa)
    
    print(diccionario.get('idProducto')[4]) 
    print(diccionario) 
    return diccionario


def consultaRegistro(ventas, idproducto):
    return


AutoPartes([
    (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
    (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
    (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
    (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
    (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')])
