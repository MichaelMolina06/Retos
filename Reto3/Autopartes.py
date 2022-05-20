def AutoPartes(ventas : list):
        dic = {}
        dic['registroVentas']=ventas
        return dic
def consultaRegistro(ventas, idProducto):
        idValue = 0
        for id in ventas['registroVentas']:
                if (idProducto == id[0]):
                        idValue = 1
                        print(f"Producto consultado : {id[0]}  Descripción  {id[1]}  #Parte  {id[2]}  Cantidad vendida  {id[3]}  Stock  {id[4]}  Comprador {id[5]}  Documento  {id[6]}  Fecha Venta  {id[7]}")
        if idValue == 0:
                print("No hay registro de venta de ese producto")
        return